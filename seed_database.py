# """
# FastAPI Database Seed Script
# Loads sample data into the database
# Fixed for SQLAlchemy 2.0 compatibility
# """
# import json
# import asyncio
# from datetime import datetime
# from typing import List, Dict
# from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime, ForeignKey
# from sqlalchemy.orm import declarative_base, sessionmaker, relationship
# from sqlalchemy.orm import Session

# # Database configuration
# DATABASE_URL = "sqlite:///./ecommerce.db"  # Change to PostgreSQL in production
# # For PostgreSQL: "postgresql://user:password@localhost/ecommerce"

# engine = create_engine(DATABASE_URL, echo=False)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # SQLAlchemy Models
# class User(Base):
#     __tablename__ = "users"
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)
#     email = Column(String(150), unique=True)
#     age = Column(Integer)
#     persona = Column(String(100))
#     price_sensitivity = Column(String(20))
#     budget_min = Column(Float)
#     budget_max = Column(Float)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     last_active = Column(DateTime, default=datetime.utcnow)
    
#     preferences = relationship("UserPreference", back_populates="user", cascade="all, delete-orphan")
#     interactions = relationship("Interaction", back_populates="user", cascade="all, delete-orphan")

# class UserPreference(Base):
#     __tablename__ = "user_preferences"
    
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     interest = Column(String(50), nullable=False)
#     weight = Column(Float, default=1.0)
    
#     user = relationship("User", back_populates="preferences")

# class Product(Base):
#     __tablename__ = "products"
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String(200), nullable=False)
#     category = Column(String(50), nullable=False)
#     subcategory = Column(String(50))
#     price = Column(Float, nullable=False)
#     brand = Column(String(100))
#     rating = Column(Float)
#     description = Column(Text)
#     features = Column(Text)  # JSON stored as text
#     stock = Column(Integer, default=0)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)
    
#     tags = relationship("ProductTag", back_populates="product", cascade="all, delete-orphan")
#     interactions = relationship("Interaction", back_populates="product", cascade="all, delete-orphan")

# class ProductTag(Base):
#     __tablename__ = "product_tags"
    
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
#     tag = Column(String(50), nullable=False)
    
#     product = relationship("Product", back_populates="tags")

# class Interaction(Base):
#     __tablename__ = "interactions"
    
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
#     interaction_type = Column(String(20), nullable=False)
#     session_duration_seconds = Column(Integer)
#     device = Column(String(20))
#     timestamp = Column(DateTime, default=datetime.utcnow)
#     metadata_info = Column(Text)  # Renamed from 'metadata' to avoid conflict
    
#     user = relationship("User", back_populates="interactions")
#     product = relationship("Product", back_populates="interactions")

# # Seed functions
# def load_json_data(filename: str) -> List[Dict]:
#     """Load data from JSON file"""
#     try:
#         with open(filename, 'r') as f:
#             return json.load(f)
#     except FileNotFoundError:
#         print(f"❌ Error: {filename} not found. Trying alternate name...")
#         # Try alternate filename (with/without _extended)
#         if '_extended' in filename:
#             alt_filename = filename.replace('_extended', '')
#         else:
#             alt_filename = filename.replace('.json', '_extended.json')
        
#         try:
#             with open(alt_filename, 'r') as f:
#                 print(f"✅ Found {alt_filename} instead")
#                 return json.load(f)
#         except FileNotFoundError:
#             print(f"❌ Error: Neither {filename} nor {alt_filename} found.")
#             print(f"Please run: python extended_data_generator.py")
#             return []

# def seed_users(db: Session, users_data: List[Dict]):
#     """Seed users and their preferences"""
#     print("\n📥 Seeding users...")
    
#     for user_data in users_data:
#         # Create user
#         user = User(
#             id=user_data['id'],
#             name=user_data['name'],
#             email=f"{user_data['name'].lower().replace(' ', '.')}@example.com",
#             age=user_data.get('age'),
#             persona=user_data.get('persona'),
#             price_sensitivity=user_data.get('price_sensitivity'),
#             budget_min=user_data.get('budget_range', [0, 0])[0],
#             budget_max=user_data.get('budget_range', [0, 0])[1]
#         )
#         db.add(user)
        
#         # Create user preferences
#         for interest in user_data.get('interests', []):
#             pref = UserPreference(
#                 user_id=user_data['id'],
#                 interest=interest,
#                 weight=1.0
#             )
#             db.add(pref)
    
#     db.commit()
#     print(f"✅ Seeded {len(users_data)} users with preferences")

# def seed_products(db: Session, products_data: List[Dict]):
#     """Seed products and their tags"""
#     print("\n📥 Seeding products...")
    
#     for product_data in products_data:
#         # Create product
#         product = Product(
#             id=product_data['id'],
#             name=product_data['name'],
#             category=product_data['category'],
#             subcategory=product_data.get('subcategory'),
#             price=product_data['price'],
#             brand=product_data.get('brand'),
#             rating=product_data.get('rating'),
#             description=product_data.get('description'),
#             features=json.dumps(product_data.get('features', [])),
#             stock=product_data.get('stock', 0)
#         )
#         db.add(product)
        
#         # Create product tags
#         for tag in product_data.get('tags', []):
#             product_tag = ProductTag(
#                 product_id=product_data['id'],
#                 tag=tag
#             )
#             db.add(product_tag)
    
#     db.commit()
#     print(f"✅ Seeded {len(products_data)} products with tags")

# def seed_interactions(db: Session, interactions_data: List[Dict]):
#     """Seed user interactions"""
#     print("\n📥 Seeding interactions...")
    
#     for interaction_data in interactions_data:
#         interaction = Interaction(
#             id=interaction_data['id'],
#             user_id=interaction_data['user_id'],
#             product_id=interaction_data['product_id'],
#             interaction_type=interaction_data['interaction_type'],
#             session_duration_seconds=interaction_data.get('session_duration_seconds'),
#             device=interaction_data.get('device'),
#             timestamp=datetime.fromisoformat(interaction_data['timestamp'])
#         )
#         db.add(interaction)
    
#     db.commit()
#     print(f"✅ Seeded {len(interactions_data)} interactions")

# def clear_database(db: Session):
#     """Clear all data from database"""
#     print("\n🗑️  Clearing existing data...")
    
#     db.query(Interaction).delete()
#     db.query(ProductTag).delete()
#     db.query(UserPreference).delete()
#     db.query(Product).delete()
#     db.query(User).delete()
    
#     db.commit()
#     print("✅ Database cleared")

# def verify_seed(db: Session):
#     """Verify seeded data"""
#     print("\n🔍 Verifying seeded data...")
    
#     user_count = db.query(User).count()
#     product_count = db.query(Product).count()
#     interaction_count = db.query(Interaction).count()
#     tag_count = db.query(ProductTag).count()
#     pref_count = db.query(UserPreference).count()
    
#     print(f"  ✓ Users: {user_count}")
#     print(f"  ✓ Products: {product_count}")
#     print(f"  ✓ Product Tags: {tag_count}")
#     print(f"  ✓ User Preferences: {pref_count}")
#     print(f"  ✓ Interactions: {interaction_count}")
    
#     # Sample query
#     print("\n📊 Sample data:")
#     sample_user = db.query(User).first()
#     if sample_user:
#         print(f"  Sample User: {sample_user.name} ({sample_user.persona})")
#         print(f"  Interests: {[p.interest for p in sample_user.preferences[:5]]}")
    
#     sample_product = db.query(Product).first()
#     if sample_product:
#         print(f"  Sample Product: {sample_product.name} (${sample_product.price})")
#         print(f"  Tags: {[t.tag for t in sample_product.tags[:5]]}")

# def main():
#     """Main seed function"""
#     print("🚀 Starting database seed process...\n")
    
#     # Create tables
#     print("📋 Creating database tables...")
#     Base.metadata.create_all(bind=engine)
#     print("✅ Tables created\n")
    
#     # Load JSON data - try both naming conventions
#     print("📂 Loading data files...")
#     users_data = load_json_data('users_extended.json')
#     if not users_data:
#         users_data = load_json_data('users.json')
    
#     products_data = load_json_data('products_extended.json')
#     if not products_data:
#         products_data = load_json_data('products.json')
    
#     interactions_data = load_json_data('interactions_extended.json')
#     if not interactions_data:
#         interactions_data = load_json_data('interactions.json')
    
#     if not all([users_data, products_data, interactions_data]):
#         print("\n❌ Missing data files. Please run: python extended_data_generator.py")
#         return False
    
#     print(f"✅ Loaded data files")
    
#     # Create database session
#     db = SessionLocal()
    
#     try:
#         # Clear existing data
#         clear_database(db)
        
#         # Seed data
#         seed_users(db, users_data)
#         seed_products(db, products_data)
#         seed_interactions(db, interactions_data)
        
#         # Verify
#         verify_seed(db)
        
#         print("\n✨ Database seeding completed successfully!")
#         print("\n💡 Next steps:")
#         print("  1. Start your FastAPI server: uvicorn main:app --reload")
#         print("  2. Test endpoints: http://localhost:8000/docs")
#         print("  3. Get recommendations: curl http://localhost:8000/recommendations/1")
        
#         return True
        
#     except Exception as e:
#         print(f"\n❌ Error during seeding: {e}")
#         import traceback
#         traceback.print_exc()
#         db.rollback()
#         return False
#     finally:
#         db.close()

# def get_db():
#     """Dependency for FastAPI routes"""
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# if __name__ == "__main__":
#     success = main()
#     exit(0 if success else 1)

# """
# FastAPI Database Seed Script
# Loads sample data into the database
# Fixed for SQLAlchemy 2.0 compatibility
# """
# import json
# import asyncio
# from datetime import datetime
# from typing import List, Dict
# from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime, ForeignKey
# from sqlalchemy.orm import declarative_base, sessionmaker, relationship
# from sqlalchemy.orm import Session

# # Database configuration
# DATABASE_URL = "sqlite:///./ecommerce.db"  # Change to PostgreSQL in production
# # For PostgreSQL: "postgresql://user:password@localhost/ecommerce"

# engine = create_engine(DATABASE_URL, echo=False)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # SQLAlchemy Models
# class User(Base):
#     __tablename__ = "users"
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String(100), nullable=False)
#     email = Column(String(150), unique=True)
#     age = Column(Integer)
#     persona = Column(String(100))
#     price_sensitivity = Column(String(20))
#     budget_min = Column(Float)
#     budget_max = Column(Float)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     last_active = Column(DateTime, default=datetime.utcnow)
    
#     preferences = relationship("UserPreference", back_populates="user", cascade="all, delete-orphan")
#     interactions = relationship("Interaction", back_populates="user", cascade="all, delete-orphan")

# class UserPreference(Base):
#     __tablename__ = "user_preferences"
    
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     interest = Column(String(50), nullable=False)
#     weight = Column(Float, default=1.0)
    
#     user = relationship("User", back_populates="preferences")

# class Product(Base):
#     __tablename__ = "products"
    
#     id = Column(Integer, primary_key=True)
#     name = Column(String(200), nullable=False)
#     category = Column(String(50), nullable=False)
#     subcategory = Column(String(50))
#     price = Column(Float, nullable=False)
#     brand = Column(String(100))
#     rating = Column(Float)
#     description = Column(Text)
#     features = Column(Text)  # JSON stored as text
#     stock = Column(Integer, default=0)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     updated_at = Column(DateTime, default=datetime.utcnow)
    
#     tags = relationship("ProductTag", back_populates="product", cascade="all, delete-orphan")
#     interactions = relationship("Interaction", back_populates="product", cascade="all, delete-orphan")

# class ProductTag(Base):
#     __tablename__ = "product_tags"
    
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
#     tag = Column(String(50), nullable=False)
    
#     product = relationship("Product", back_populates="tags")

# class Interaction(Base):
#     __tablename__ = "interactions"
    
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
#     interaction_type = Column(String(20), nullable=False)
#     session_duration_seconds = Column(Integer)
#     device = Column(String(20))
#     timestamp = Column(DateTime, default=datetime.utcnow)
#     metadata_info = Column(Text)  # Renamed from 'metadata' to avoid conflict
    
#     user = relationship("User", back_populates="interactions")
#     product = relationship("Product", back_populates="interactions")

# # Seed functions
# def load_json_data(filename: str) -> List[Dict]:
#     """Load data from JSON file"""
#     # Try different file naming conventions
#     possible_names = [
#         filename,
#         filename.replace('.json', '_large.json'),
#         # filename.replace('.json', '_extended.json'),
#         filename.replace('_large', ''),
#         # filename.replace('_extended', '')
#     ]
    
#     for fname in possible_names:
#         try:
#             with open(fname, 'r') as f:
#                 data = json.load(f)
#                 if data:  # Check data is not empty
#                     print(f"✅ Loaded {fname} ({len(data)} records)")
#                     return data
#         except FileNotFoundError:
#             continue
    
#     print(f"❌ Error: Could not find any variant of {filename}")
#     print(f"   Tried: {', '.join(possible_names)}")
#     print(f"   Please run: python generate_large_dataset.py")
#     return []

# def seed_users(db: Session, users_data: List[Dict]):
#     """Seed users and their preferences"""
#     print("\n📥 Seeding users...")
    
#     for user_data in users_data:
#         # Create user
#         user = User(
#             id=user_data['id'],
#             name=user_data['name'],
#             email=f"{user_data['name'].lower().replace(' ', '.')}@example.com",
#             age=user_data.get('age'),
#             persona=user_data.get('persona'),
#             price_sensitivity=user_data.get('price_sensitivity'),
#             budget_min=user_data.get('budget_range', [0, 0])[0],
#             budget_max=user_data.get('budget_range', [0, 0])[1]
#         )
#         db.add(user)
        
#         # Create user preferences
#         for interest in user_data.get('interests', []):
#             pref = UserPreference(
#                 user_id=user_data['id'],
#                 interest=interest,
#                 weight=1.0
#             )
#             db.add(pref)
    
#     db.commit()
#     print(f"✅ Seeded {len(users_data)} users with preferences")

# def seed_products(db: Session, products_data: List[Dict]):
#     """Seed products and their tags"""
#     print("\n📥 Seeding products...")
    
#     for product_data in products_data:
#         # Create product
#         product = Product(
#             id=product_data['id'],
#             name=product_data['name'],
#             category=product_data['category'],
#             subcategory=product_data.get('subcategory'),
#             price=product_data['price'],
#             brand=product_data.get('brand'),
#             rating=product_data.get('rating'),
#             description=product_data.get('description'),
#             features=json.dumps(product_data.get('features', [])),
#             stock=product_data.get('stock', 0)
#         )
#         db.add(product)
        
#         # Create product tags
#         for tag in product_data.get('tags', []):
#             product_tag = ProductTag(
#                 product_id=product_data['id'],
#                 tag=tag
#             )
#             db.add(product_tag)
    
#     db.commit()
#     print(f"✅ Seeded {len(products_data)} products with tags")

# def seed_interactions(db: Session, interactions_data: List[Dict]):
#     """Seed user interactions"""
#     print("\n📥 Seeding interactions...")
    
#     for interaction_data in interactions_data:
#         interaction = Interaction(
#             id=interaction_data['id'],
#             user_id=interaction_data['user_id'],
#             product_id=interaction_data['product_id'],
#             interaction_type=interaction_data['interaction_type'],
#             session_duration_seconds=interaction_data.get('session_duration_seconds'),
#             device=interaction_data.get('device'),
#             timestamp=datetime.fromisoformat(interaction_data['timestamp'])
#         )
#         db.add(interaction)
    
#     db.commit()
#     print(f"✅ Seeded {len(interactions_data)} interactions")

# def clear_database(db: Session):
#     """Clear all data from database"""
#     print("\n🗑️  Clearing existing data...")
    
#     db.query(Interaction).delete()
#     db.query(ProductTag).delete()
#     db.query(UserPreference).delete()
#     db.query(Product).delete()
#     db.query(User).delete()
    
#     db.commit()
#     print("✅ Database cleared")

# def verify_seed(db: Session):
#     """Verify seeded data"""
#     print("\n🔍 Verifying seeded data...")
    
#     user_count = db.query(User).count()
#     product_count = db.query(Product).count()
#     interaction_count = db.query(Interaction).count()
#     tag_count = db.query(ProductTag).count()
#     pref_count = db.query(UserPreference).count()
    
#     print(f"  ✓ Users: {user_count}")
#     print(f"  ✓ Products: {product_count}")
#     print(f"  ✓ Product Tags: {tag_count}")
#     print(f"  ✓ User Preferences: {pref_count}")
#     print(f"  ✓ Interactions: {interaction_count}")
    
#     # Sample query
#     print("\n📊 Sample data:")
#     sample_user = db.query(User).first()
#     if sample_user:
#         print(f"  Sample User: {sample_user.name} ({sample_user.persona})")
#         print(f"  Interests: {[p.interest for p in sample_user.preferences[:5]]}")
    
#     sample_product = db.query(Product).first()
#     if sample_product:
#         print(f"  Sample Product: {sample_product.name} (${sample_product.price})")
#         print(f"  Tags: {[t.tag for t in sample_product.tags[:5]]}")

# def main():
#     """Main seed function"""
#     print("🚀 Starting database seed process...\n")
    
#     # Create tables
#     print("📋 Creating database tables...")
#     Base.metadata.create_all(bind=engine)
#     print("✅ Tables created\n")
    
#     # Load JSON data - try both naming conventions
#     print("📂 Loading data files...")
#     users_data = load_json_data('users_extended.json')
#     if not users_data:
#         users_data = load_json_data('users.json')
    
#     products_data = load_json_data('products_extended.json')
#     if not products_data:
#         products_data = load_json_data('products.json')
    
#     interactions_data = load_json_data('interactions_extended.json')
#     if not interactions_data:
#         interactions_data = load_json_data('interactions.json')
    
#     if not all([users_data, products_data, interactions_data]):
#         print("\n❌ Missing data files. Please run: python extended_data_generator.py")
#         return False
    
#     print(f"✅ Loaded data files")
    
#     # Create database session
#     db = SessionLocal()
    
#     try:
#         # Clear existing data
#         clear_database(db)
        
#         # Seed data
#         seed_users(db, users_data)
#         seed_products(db, products_data)
#         seed_interactions(db, interactions_data)
        
#         # Verify
#         verify_seed(db)
        
#         print("\n✨ Database seeding completed successfully!")
#         print("\n💡 Next steps:")
#         print("  1. Start your FastAPI server: uvicorn main:app --reload")
#         print("  2. Test endpoints: http://localhost:8000/docs")
#         print("  3. Get recommendations: curl http://localhost:8000/recommendations/1")
        
#         return True
        
#     except Exception as e:
#         print(f"\n❌ Error during seeding: {e}")
#         import traceback
#         traceback.print_exc()
#         db.rollback()
#         return False
#     finally:
#         db.close()

# def get_db():
#     """Dependency for FastAPI routes"""
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# if __name__ == "__main__":
#     success = main()
#     exit(0 if success else 1)


"""
FastAPI Database Seed Script
Loads sample data into the database
Fixed for SQLAlchemy 2.0 compatibility
"""
import json
import asyncio
from datetime import datetime
from typing import List, Dict
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.orm import Session

# Database configuration
DATABASE_URL = "sqlite:///./ecommerce.db"  # Change to PostgreSQL in production
# For PostgreSQL: "postgresql://user:password@localhost/ecommerce"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy Models
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True)
    age = Column(Integer)
    persona = Column(String(100))
    price_sensitivity = Column(String(20))
    budget_min = Column(Float)
    budget_max = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_active = Column(DateTime, default=datetime.utcnow)
    
    preferences = relationship("UserPreference", back_populates="user", cascade="all, delete-orphan")
    interactions = relationship("Interaction", back_populates="user", cascade="all, delete-orphan")

class UserPreference(Base):
    __tablename__ = "user_preferences"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    interest = Column(String(50), nullable=False)
    weight = Column(Float, default=1.0)
    
    user = relationship("User", back_populates="preferences")

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    category = Column(String(50), nullable=False)
    subcategory = Column(String(50))
    price = Column(Float, nullable=False)
    brand = Column(String(100))
    rating = Column(Float)
    description = Column(Text)
    features = Column(Text)  # JSON stored as text
    stock = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    
    tags = relationship("ProductTag", back_populates="product", cascade="all, delete-orphan")
    interactions = relationship("Interaction", back_populates="product", cascade="all, delete-orphan")

class ProductTag(Base):
    __tablename__ = "product_tags"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    tag = Column(String(50), nullable=False)
    
    product = relationship("Product", back_populates="tags")

class Interaction(Base):
    __tablename__ = "interactions"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    interaction_type = Column(String(20), nullable=False)
    session_duration_seconds = Column(Integer)
    device = Column(String(20))
    timestamp = Column(DateTime, default=datetime.utcnow)
    metadata_info = Column(Text)  # Renamed from 'metadata' to avoid conflict
    
    user = relationship("User", back_populates="interactions")
    product = relationship("Product", back_populates="interactions")

# Seed functions
def load_json_data(filename: str) -> List[Dict]:
    """Load data from JSON file"""
    # Try different file naming conventions
    possible_names = [
        filename,
        filename.replace('.json', '_large.json'),
        filename.replace('.json', '_extended.json'),
        filename.replace('_large', ''),
        filename.replace('_extended', '')
    ]
    
    for fname in possible_names:
        try:
            with open(fname, 'r') as f:
                data = json.load(f)
                if data:  # Check data is not empty
                    print(f"✅ Loaded {fname} ({len(data)} records)")
                    return data
        except FileNotFoundError:
            continue
    
    print(f"❌ Error: Could not find any variant of {filename}")
    print(f"   Tried: {', '.join(possible_names)}")
    print(f"   Please run: python generate_large_dataset.py")
    return []

def seed_users(db: Session, users_data: List[Dict]):
    """Seed users and their preferences"""
    print("\n📥 Seeding users...")
    
    for user_data in users_data:
        # Create user
        user = User(
            id=user_data['id'],
            name=user_data['name'],
            email=f"{user_data['name'].lower().replace(' ', '.')}@example.com",
            age=user_data.get('age'),
            persona=user_data.get('persona'),
            price_sensitivity=user_data.get('price_sensitivity'),
            budget_min=user_data.get('budget_range', [0, 0])[0],
            budget_max=user_data.get('budget_range', [0, 0])[1]
        )
        db.add(user)
        
        # Create user preferences
        for interest in user_data.get('interests', []):
            pref = UserPreference(
                user_id=user_data['id'],
                interest=interest,
                weight=1.0
            )
            db.add(pref)
    
    db.commit()
    print(f"✅ Seeded {len(users_data)} users with preferences")

def seed_products(db: Session, products_data: List[Dict]):
    """Seed products and their tags"""
    print("\n📥 Seeding products...")
    
    for product_data in products_data:
        # Create product
        product = Product(
            id=product_data['id'],
            name=product_data['name'],
            category=product_data['category'],
            subcategory=product_data.get('subcategory'),
            price=product_data['price'],
            brand=product_data.get('brand'),
            rating=product_data.get('rating'),
            description=product_data.get('description'),
            features=json.dumps(product_data.get('features', [])),
            stock=product_data.get('stock', 0)
        )
        db.add(product)
        
        # Create product tags
        for tag in product_data.get('tags', []):
            product_tag = ProductTag(
                product_id=product_data['id'],
                tag=tag
            )
            db.add(product_tag)
    
    db.commit()
    print(f"✅ Seeded {len(products_data)} products with tags")

def seed_interactions(db: Session, interactions_data: List[Dict]):
    """Seed user interactions"""
    print("\n📥 Seeding interactions...")
    
    for interaction_data in interactions_data:
        interaction = Interaction(
            id=interaction_data['id'],
            user_id=interaction_data['user_id'],
            product_id=interaction_data['product_id'],
            interaction_type=interaction_data['interaction_type'],
            session_duration_seconds=interaction_data.get('session_duration_seconds'),
            device=interaction_data.get('device'),
            timestamp=datetime.fromisoformat(interaction_data['timestamp'])
        )
        db.add(interaction)
    
    db.commit()
    print(f"✅ Seeded {len(interactions_data)} interactions")

def clear_database(db: Session):
    """Clear all data from database"""
    print("\n🗑️  Clearing existing data...")
    
    db.query(Interaction).delete()
    db.query(ProductTag).delete()
    db.query(UserPreference).delete()
    db.query(Product).delete()
    db.query(User).delete()
    
    db.commit()
    print("✅ Database cleared")

def verify_seed(db: Session):
    """Verify seeded data"""
    print("\n🔍 Verifying seeded data...")
    
    user_count = db.query(User).count()
    product_count = db.query(Product).count()
    interaction_count = db.query(Interaction).count()
    tag_count = db.query(ProductTag).count()
    pref_count = db.query(UserPreference).count()
    
    print(f"  ✓ Users: {user_count}")
    print(f"  ✓ Products: {product_count}")
    print(f"  ✓ Product Tags: {tag_count}")
    print(f"  ✓ User Preferences: {pref_count}")
    print(f"  ✓ Interactions: {interaction_count}")
    
    # Sample query
    print("\n📊 Sample data:")
    sample_user = db.query(User).first()
    if sample_user:
        print(f"  Sample User: {sample_user.name} ({sample_user.persona})")
        print(f"  Interests: {[p.interest for p in sample_user.preferences[:5]]}")
    
    sample_product = db.query(Product).first()
    if sample_product:
        print(f"  Sample Product: {sample_product.name} (${sample_product.price})")
        print(f"  Tags: {[t.tag for t in sample_product.tags[:5]]}")

def main():
    """Main seed function"""
    print("🚀 Starting database seed process...\n")
    
    # Create tables
    print("📋 Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created\n")
    
    # Load JSON data - prioritize large dataset, then extended, then basic
    print("📂 Loading data files...")
    
    # Try to load users (large -> extended -> basic)
    users_data = (load_json_data('users_large.json') or 
                  load_json_data('users_extended.json') or 
                  load_json_data('users.json'))
    
    # Try to load products
    products_data = (load_json_data('products_large.json') or 
                     load_json_data('products_extended.json') or 
                     load_json_data('products.json'))
    
    # Try to load interactions
    interactions_data = (load_json_data('interactions_large.json') or 
                        load_json_data('interactions_extended.json') or 
                        load_json_data('interactions.json'))
    
    if not all([users_data, products_data, interactions_data]):
        print("\n❌ Missing data files. Please run one of:")
        print("  python generate_large_dataset.py  (150 users, 1800 products)")
        print("  python extended_data_generator.py (10 users, 66 products)")
        print("  python generate_data.py           (6 users, 30 products)")
        return False
    
    print(f"✅ Loaded data: {len(users_data)} users, {len(products_data)} products, {len(interactions_data)} interactions")
    
    # Create database session
    db = SessionLocal()
    
    try:
        # Clear existing data
        clear_database(db)
        
        # Seed data
        seed_users(db, users_data)
        seed_products(db, products_data)
        seed_interactions(db, interactions_data)
        
        # Verify
        verify_seed(db)
        
        print("\n✨ Database seeding completed successfully!")
        print("\n💡 Next steps:")
        print("  1. Start your FastAPI server: uvicorn main:app --reload")
        print("  2. Test endpoints: http://localhost:8000/docs")
        print("  3. Get recommendations: curl \"http://localhost:8000/recommendations/1?limit=5\"")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error during seeding: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
        return False
    finally:
        db.close()

def get_db():
    """Dependency for FastAPI routes"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)