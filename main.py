"""
FastAPI E-commerce Product Recommender API
Main application file with all endpoints
"""
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime, timedelta
import os
from pydantic import BaseModel

# Import database models and session
from seed_database import get_db, User, Product, Interaction, ProductTag, UserPreference

# Import LLM service
from llm_service import llm_service, generate_explanation as generate_llm_explanation

app = FastAPI(
    title="E-commerce Product Recommender API",
    description="AI-powered product recommendations with explanations",
    version="1.0.0"
)

# CORS middleware for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models for request/response
class ProductResponse(BaseModel):
    id: int
    name: str
    category: str
    price: float
    rating: float
    brand: str
    description: str
    tags: List[str]
    stock: int

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    name: str
    persona: str
    age: int
    interests: List[str]
    budget_range: List[float]

    class Config:
        from_attributes = True

class InteractionCreate(BaseModel):
    user_id: int
    product_id: int
    interaction_type: str
    device: Optional[str] = "desktop"
    session_duration_seconds: Optional[int] = None

class RecommendationResponse(BaseModel):
    product_id: int
    product_name: str
    price: float
    rating: float
    category: str
    score: float
    explanation: str
    tags: List[str]

# Health check endpoint
@app.get("/")
def read_root():
    return {
        "message": "E-commerce Product Recommender API",
        "version": "1.0.0",
        "status": "healthy",
        "endpoints": {
            "docs": "/docs",
            "users": "/users",
            "products": "/products",
            "recommendations": "/recommendations/{user_id}"
        }
    }

# User endpoints
@app.get("/users", response_model=List[UserResponse])
def get_all_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Get all users"""
    users = db.query(User).offset(skip).limit(limit).all()
    
    result = []
    for user in users:
        result.append({
            "id": user.id,
            "name": user.name,
            "persona": user.persona,
            "age": user.age,
            "interests": [p.interest for p in user.preferences],
            "budget_range": [user.budget_min, user.budget_max]
        })
    
    return result

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Get user by ID"""
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "id": user.id,
        "name": user.name,
        "persona": user.persona,
        "age": user.age,
        "interests": [p.interest for p in user.preferences],
        "budget_range": [user.budget_min, user.budget_max]
    }

@app.get("/users/{user_id}/history")
def get_user_history(
    user_id: int,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    """Get user's interaction history"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    interactions = (
        db.query(Interaction, Product)
        .join(Product)
        .filter(Interaction.user_id == user_id)
        .order_by(Interaction.timestamp.desc())
        .limit(limit)
        .all()
    )
    
    return [
        {
            "interaction_id": i.id,
            "product_id": p.id,
            "product_name": p.name,
            "category": p.category,
            "interaction_type": i.interaction_type,
            "timestamp": i.timestamp,
            "device": i.device
        }
        for i, p in interactions
    ]

# Product endpoints
@app.get("/products", response_model=List[ProductResponse])
def get_products(
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    search: Optional[str] = None,
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    """Get products with optional filters"""
    query = db.query(Product)
    
    if category:
        query = query.filter(Product.category == category)
    if min_price:
        query = query.filter(Product.price >= min_price)
    if max_price:
        query = query.filter(Product.price <= max_price)
    if search:
        query = query.filter(
            (Product.name.ilike(f"%{search}%")) |
            (Product.description.ilike(f"%{search}%"))
        )
    
    products = query.offset(skip).limit(limit).all()
    
    result = []
    for product in products:
        result.append({
            "id": product.id,
            "name": product.name,
            "category": product.category,
            "price": product.price,
            "rating": product.rating,
            "brand": product.brand,
            "description": product.description,
            "tags": [t.tag for t in product.tags],
            "stock": product.stock
        })
    
    return result

@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """Get product by ID"""
    product = db.query(Product).filter(Product.id == product_id).first()
    
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return {
        "id": product.id,
        "name": product.name,
        "category": product.category,
        "price": product.price,
        "rating": product.rating,
        "brand": product.brand,
        "description": product.description,
        "tags": [t.tag for t in product.tags],
        "stock": product.stock
    }

@app.get("/categories")
def get_categories(db: Session = Depends(get_db)):
    """Get all product categories"""
    categories = db.query(Product.category).distinct().all()
    return {"categories": [c[0] for c in categories]}

# Interaction endpoints
@app.post("/interactions")
def create_interaction(
    interaction: InteractionCreate,
    db: Session = Depends(get_db)
):
    """Track user interaction with a product"""
    # Verify user and product exist
    user = db.query(User).filter(User.id == interaction.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    product = db.query(Product).filter(Product.id == interaction.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Create interaction
    new_interaction = Interaction(
        user_id=interaction.user_id,
        product_id=interaction.product_id,
        interaction_type=interaction.interaction_type,
        device=interaction.device,
        session_duration_seconds=interaction.session_duration_seconds,
        timestamp=datetime.utcnow()
    )
    
    db.add(new_interaction)
    db.commit()
    db.refresh(new_interaction)
    
    return {
        "message": "Interaction recorded successfully",
        "interaction_id": new_interaction.id
    }

@app.get("/analytics/popular-products")
def get_popular_products(
    limit: int = 10,
    category: Optional[str] = None,
    db: Session = Depends(get_db)
):
    """Get most popular products based on interactions"""
    from sqlalchemy import func
    
    query = (
        db.query(
            Product,
            func.count(Interaction.id).label('interaction_count')
        )
        .join(Interaction)
        .group_by(Product.id)
    )
    
    if category:
        query = query.filter(Product.category == category)
    
    popular = query.order_by(func.count(Interaction.id).desc()).limit(limit).all()
    
    return [
        {
            "product_id": p.id,
            "product_name": p.name,
            "category": p.category,
            "price": p.price,
            "interaction_count": count
        }
        for p, count in popular
    ]

@app.get("/analytics/user-activity")
def get_user_activity_stats(db: Session = Depends(get_db)):
    """Get overall user activity statistics"""
    from sqlalchemy import func
    
    stats = (
        db.query(
            func.count(Interaction.id).label('total_interactions'),
            func.count(func.distinct(Interaction.user_id)).label('active_users'),
            func.count(func.distinct(Interaction.product_id)).label('products_interacted')
        )
        .first()
    )
    
    return {
        "total_interactions": stats.total_interactions,
        "active_users": stats.active_users,
        "products_with_interactions": stats.products_interacted
    }

# Recommendation endpoints
@app.get("/recommendations/{user_id}", response_model=List[RecommendationResponse])
def get_recommendations(
    user_id: int,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    """
    Get personalized product recommendations for a user
    Uses content-based filtering with user interests and interaction history
    """
    # Get user
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Get user's interests
    user_interests = [p.interest for p in user.preferences]
    
    # Get user's recent interactions (last 30 days)
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    recent_interactions = (
        db.query(Interaction)
        .filter(
            Interaction.user_id == user_id,
            Interaction.timestamp >= thirty_days_ago
        )
        .all()
    )
    
    # Products user has already purchased or disliked - exclude these
    excluded_product_ids = [
        i.product_id for i in recent_interactions 
        if i.interaction_type in ['purchase', 'dislike']
    ]
    
    # Products user has interacted with positively
    positive_interaction_products = [
        i.product_id for i in recent_interactions
        if i.interaction_type in ['like', 'add_to_cart', 'purchase']
    ]
    
    # Get all products within user's budget
    candidate_products = (
        db.query(Product)
        .filter(
            Product.price >= user.budget_min,
            Product.price <= user.budget_max,
            Product.id.notin_(excluded_product_ids),
            Product.stock > 0
        )
        .all()
    )
    
    # Score each product
    scored_products = []
    
    for product in candidate_products:
        score = 0
        reasons = []
        
        # Get product tags
        product_tags = [t.tag for t in product.tags]
        
        # Interest matching (highest weight)
        interest_matches = [tag for tag in product_tags if tag in user_interests]
        if interest_matches:
            score += len(interest_matches) * 10
            reasons.append(f"matches your interests in {', '.join(interest_matches[:3])}")
        
        # Similar to liked products
        if positive_interaction_products:
            similar_count = 0
            for liked_id in positive_interaction_products:
                liked_product = db.query(Product).filter(Product.id == liked_id).first()
                if liked_product:
                    liked_tags = [t.tag for t in liked_product.tags]
                    overlap = len(set(product_tags) & set(liked_tags))
                    if overlap > 0:
                        similar_count += overlap
            
            if similar_count > 0:
                score += similar_count * 5
                reasons.append("similar to products you've liked")
        
        # High rating boost
        if product.rating >= 4.5:
            score += 5
            reasons.append(f"highly rated ({product.rating}★)")
        
        # Brand preference
        if hasattr(user, 'preferred_brands'):
            # This would need to be added to user model
            pass
        
        # Price preference (favor mid-range within budget)
        price_range = user.budget_max - user.budget_min
        optimal_price = user.budget_min + (price_range * 0.5)
        price_diff_ratio = abs(product.price - optimal_price) / price_range
        price_score = max(0, 3 * (1 - price_diff_ratio))
        score += price_score
        
        # Popularity boost (products with more interactions)
        interaction_count = (
            db.query(Interaction)
            .filter(Interaction.product_id == product.id)
            .count()
        )
        if interaction_count > 10:
            score += 2
            reasons.append("popular choice")
        
        scored_products.append({
            "product": product,
            "score": score,
            "reasons": reasons
        })
    
    # Sort by score and get top recommendations
    scored_products.sort(key=lambda x: x["score"], reverse=True)
    top_recommendations = scored_products[:limit]
    
    # Generate LLM-style explanations
    recommendations = []
    for item in top_recommendations:
        product = item["product"]
        reasons = item["reasons"]
        
        # Create explanation (in production, call LLM API here)
        explanation = generate_explanation(
            user=user,
            product=product,
            reasons=reasons
        )
        
        recommendations.append({
            "product_id": product.id,
            "product_name": product.name,
            "price": product.price,
            "rating": product.rating,
            "category": product.category,
            "score": round(item["score"], 2),
            "explanation": explanation,
            "tags": [t.tag for t in product.tags]
        })
    
    return recommendations

def generate_explanation(user, product, reasons):
    """
    Generate human-readable explanation for recommendation
    Uses Gemini API if configured, otherwise falls back to rule-based
    """
    # Get recent purchases for context
    from seed_database import SessionLocal
    db = SessionLocal()
    recent_purchases = (
        db.query(Product.name)
        .join(Interaction)
        .filter(
            Interaction.user_id == user.id,
            Interaction.interaction_type == 'purchase'
        )
        .limit(5)
        .all()
    )
    db.close()
    
    recent_purchase_names = [p[0] for p in recent_purchases]
    
    # Use Gemini LLM service
    return generate_llm_explanation(user, product, reasons, recent_purchase_names)

# LLM Integration endpoint (placeholder for OpenAI/Claude)
@app.post("/recommendations/{user_id}/explain")
async def explain_recommendation_with_llm(
    user_id: int,
    product_id: int,
    db: Session = Depends(get_db)
):
    """
    Generate LLM-powered explanation for a specific recommendation
    This is where you'd integrate OpenAI or Claude API
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Get user context
    user_interests = [p.interest for p in user.preferences]
    recent_purchases = (
        db.query(Product)
        .join(Interaction)
        .filter(
            Interaction.user_id == user_id,
            Interaction.interaction_type == 'purchase'
        )
        .limit(5)
        .all()
    )
    
    # Build prompt for LLM
    prompt = f"""
User Profile:
- Name: {user.name}
- Persona: {user.persona}
- Interests: {', '.join(user_interests)}
- Budget Range: ${user.budget_min} - ${user.budget_max}
- Recent Purchases: {', '.join([p.name for p in recent_purchases])}

Recommended Product:
- Name: {product.name}
- Category: {product.category}
- Price: ${product.price}
- Description: {product.description}
- Tags: {', '.join([t.tag for t in product.tags])}

Task: Explain in 2-3 conversational sentences why this product is perfect for this user. 
Be specific about features that match their interests and persona. Make it engaging and personal.
"""
    
    # TODO: Call OpenAI/Claude API here
    # Example:
    # import openai
    # response = openai.ChatCompletion.create(
    #     model="gpt-3.5-turbo",
    #     messages=[{"role": "user", "content": prompt}]
    # )
    # explanation = response.choices[0].message.content
    
    # For now, return the prompt structure
    return {
        "product_id": product_id,
        "prompt": prompt,
        "note": "Integrate OpenAI/Claude API to get actual LLM explanation",
        "placeholder_explanation": generate_explanation(
            user, product, ["matches your interests", "highly rated"]
        )
    }

# Statistics endpoint
@app.get("/stats")
def get_statistics(db: Session = Depends(get_db)):
    """Get overall platform statistics"""
    from sqlalchemy import func
    
    total_users = db.query(func.count(User.id)).scalar()
    total_products = db.query(func.count(Product.id)).scalar()
    total_interactions = db.query(func.count(Interaction.id)).scalar()
    
    # Interaction breakdown
    interaction_types = (
        db.query(
            Interaction.interaction_type,
            func.count(Interaction.id)
        )
        .group_by(Interaction.interaction_type)
        .all()
    )
    
    # Category breakdown
    category_stats = (
        db.query(
            Product.category,
            func.count(Product.id),
            func.avg(Product.price)
        )
        .group_by(Product.category)
        .all()
    )
    
    return {
        "overview": {
            "total_users": total_users,
            "total_products": total_products,
            "total_interactions": total_interactions
        },
        "interactions_by_type": {
            itype: count for itype, count in interaction_types
        },
        "products_by_category": [
            {
                "category": cat,
                "count": count,
                "avg_price": round(avg_price, 2)
            }
            for cat, count, avg_price in category_stats
        ]
    }

# Gemini API test endpoint
@app.get("/test-gemini")
def test_gemini_api():
    """Test Gemini API connection and configuration"""
    result = llm_service.test_connection()
    return result

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)