# """
# LLM Service - Google Gemini Integration
# Generates personalized product recommendation explanations
# """
# import os
# import json
# from typing import List, Dict, Optional
# import google.generativeai as genai
# from google.generativeai.types import GenerationConfig
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# class LLMService:
#     def __init__(self):
#         self.model_name = "models/gemini-2.0-flash"
#         GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

#         if GEMINI_API_KEY:
#             try:
#                 genai.configure(api_key=GEMINI_API_KEY)
#                 self.model = genai.GenerativeModel(self.model_name)
#                 self.is_configured = True
#                 print("✅ Gemini API configured successfully")
#             except Exception as e:
#                 print(f"⚠️ Gemini API configuration failed: {e}")
#                 self.is_configured = False
#         else:
#             print("⚠️ GEMINI_API_KEY not found in environment variables")
#             self.is_configured = False

#     def generate_explanation(
#         self,
#         user_name: str,
#         user_persona: str,
#         user_interests: List[str],
#         user_budget_range: List[float],
#         recent_purchases: List[str],
#         product_name: str,
#         product_category: str,
#         product_price: float,
#         product_description: str,
#         product_tags: List[str],
#         product_rating: float,
#         recommendation_reasons: List[str]
#     ) -> str:
#         """Generate personalized explanation using Gemini API"""

#         if not self.is_configured:
#             return self._generate_fallback_explanation(
#                 product_name, product_price, user_budget_range,
#                 recommendation_reasons, product_rating
#             )

#         prompt = self._build_prompt(
#             user_name=user_name,
#             user_persona=user_persona,
#             user_interests=user_interests,
#             user_budget_range=user_budget_range,
#             recent_purchases=recent_purchases,
#             product_name=product_name,
#             product_category=product_category,
#             product_price=product_price,
#             product_description=product_description,
#             product_tags=product_tags,
#             product_rating=product_rating,
#             recommendation_reasons=recommendation_reasons
#         )

#         try:
#             response = self.model.generate_content(
#                 prompt,
#                 generation_config=GenerationConfig(
#                     temperature=0.7,
#                     top_p=0.95,
#                     top_k=40,
#                     max_output_tokens=200,
#                 ),
#             )

#             if response and response.text:
#                 return response.text.strip()
#             else:
#                 print("⚠️ Empty response from Gemini, using fallback")
#                 return self._generate_fallback_explanation(
#                     product_name, product_price, user_budget_range,
#                     recommendation_reasons, product_rating
#                 )
#         except Exception as e:
#             print(f"⚠️ Gemini API error: {e}")
#             return self._generate_fallback_explanation(
#                 product_name, product_price, user_budget_range,
#                 recommendation_reasons, product_rating
#             )

# #     def _build_prompt(
# #         self,
# #         user_name: str,
# #         user_persona: str,
# #         user_interests: List[str],
# #         user_budget_range: List[float],
# #         recent_purchases: List[str],
# #         product_name: str,
# #         product_category: str,
# #         product_price: float,
# #         product_description: str,
# #         product_tags: List[str],
# #         product_rating: float,
# #         recommendation_reasons: List[str]
# #     ) -> str:
# #         """Build the prompt for Gemini API"""

# #         prompt = f"""You are a helpful e-commerce product recommendation assistant. Create a personalized, conversational explanation for why a product is recommended to a user.

# # USER PROFILE:
# # - Name: {user_name}
# # - Persona: {user_persona}
# # - Interests: {', '.join(user_interests[:5])}
# # - Budget Range: ${user_budget_range[0]} - ${user_budget_range[1]}
# # - Recent Purchases: {', '.join(recent_purchases[:3]) if recent_purchases else 'None yet'}

# # RECOMMENDED PRODUCT:
# # - Name: {product_name}
# # - Category: {product_category}
# # - Price: ${product_price}
# # - Rating: {product_rating}/5 stars
# # - Description: {product_description}
# # - Key Features: {', '.join(product_tags[:5])}

# # WHY THIS RECOMMENDATION:
# # {chr(10).join(f"- {reason}" for reason in recommendation_reasons[:3])}

# # TASK:
# # Write a compelling 2-3 sentence explanation for why this product is perfect for {user_name}. Be specific about features that match their interests. Make it conversational and persuasive. Focus on value and relevance.

# # EXPLANATION:"""
# #         return prompt

#     def _build_prompt(
#         self,
#         user_name: str,
#         user_persona: str,
#         user_interests: List[str],
#         user_budget_range: List[float],
#         recent_purchases: List[str],
#         product_name: str,
#         product_category: str,
#         product_price: float,
#         product_description: str,
#         product_tags: List[str],
#         product_rating: float,
#         recommendation_reasons: List[str]
#     ) -> str:
#         """Builds a professional and context-rich prompt for Gemini API."""

#         prompt = f"""
#     You are an intelligent product recommendation writer for an AI-powered shopping assistant.
#     Your goal is to create a short, **highly personalized and specific explanation** for why a product is a perfect fit for a user.

#     The tone should be:
#     - **Professional**, **insightful**, and **human-like** (no marketing clichés or greetings like “Hey”)
#     - Use **confident, factual language** focused on the user's persona, interests, and product features
#     - Write like an expert reviewer, not a salesperson
#     - Keep it concise — 2 to 4 sentences max

#     ---

#     USER PROFILE:
#     - Name: {user_name}
#     - Persona: {user_persona}
#     - Interests: {', '.join(user_interests[:5])}
#     - Budget Range: ${user_budget_range[0]} - ${user_budget_range[1]}
#     - Recent Purchases: {', '.join(recent_purchases[:3]) if recent_purchases else 'None'}

#     RECOMMENDED PRODUCT:
#     - Name: {product_name}
#     - Category: {product_category}
#     - Price: ${product_price}
#     - Rating: {product_rating}/5 stars
#     - Description: {product_description}
#     - Key Features: {', '.join(product_tags[:5])}

#     REASONS FOR RECOMMENDATION:
#     {chr(10).join(f"- {reason}" for reason in recommendation_reasons[:3])}

#     ---

#     TASK:
#     Write a **precise and context-aware explanation** describing *why this product is ideal for the user*.  
#     - Mention specific product attributes that match their persona or use-case.  
#     - Highlight **functional advantages**, **performance**, and **value alignment** (e.g., “fits your budget,” “ideal for developers,” “balances price and capability”).  
#     - If relevant, note the **product’s standout qualities** (like power, design, efficiency, comfort, etc.).  
#     - Avoid flattery, emojis, or greetings.  

#     Respond in this style:

#     **Example 1:**  
#     "Alex, as a tech enthusiast and developer, the MacBook Pro 16-inch M3 is your perfect coding companion. Its M3 chip handles demanding programming tasks and video editing effortlessly, while the 16-inch Retina display offers ample workspace. At $2499, it's a premium investment aligned with your passion for cutting-edge performance."

#     **Example 2:**  
#     "The Dell XPS 15 Developer Edition is designed for professionals like you. With Ubuntu pre-installed and 32GB RAM, it manages heavy workloads across multiple IDEs with ease. Its 4K display enhances productivity, and at $1799, it offers strong value within your budget."

#     Now write a similar explanation for this user and product.

#     EXPLANATION:
#     """
#         return prompt.strip()

#     def _generate_fallback_explanation(
#         self,
#         product_name: str,
#         product_price: float,
#         user_budget_range: List[float],
#         recommendation_reasons: List[str],
#         product_rating: float
#     ) -> str:
#         """Generate rule-based explanation when API is not available"""
#         explanation = f"We recommend {product_name}"

#         if recommendation_reasons:
#             explanation += f" because it {recommendation_reasons[0]}"
#             if len(recommendation_reasons) > 1:
#                 explanation += f" and {recommendation_reasons[1]}"
#         else:
#             explanation += " based on your profile"

#         if user_budget_range:
#             budget_mid = (user_budget_range[0] + user_budget_range[1]) / 2
#             if product_price < budget_mid * 0.5:
#                 explanation += f". At ${product_price:.2f}, it's an excellent value"
#             elif product_price > budget_mid * 1.5:
#                 explanation += f". It's a premium choice at ${product_price:.2f}"
#             else:
#                 explanation += f" at a great price of ${product_price:.2f}"

#         if product_rating >= 4.5:
#             explanation += f" with an outstanding {product_rating}⭐ rating"
#         elif product_rating >= 4.0:
#             explanation += f" and has a solid {product_rating}⭐ rating"

#         explanation += "."
#         return explanation

#     def generate_batch_explanations(self, recommendations: List[Dict]) -> List[Dict]:
#         """Generate explanations for multiple recommendations"""
#         for rec in recommendations:
#             rec['explanation'] = self.generate_explanation(
#                 user_name=rec.get('user_name', 'User'),
#                 user_persona=rec.get('user_persona', ''),
#                 user_interests=rec.get('user_interests', []),
#                 user_budget_range=rec.get('user_budget_range', [0, 10000]),
#                 recent_purchases=rec.get('recent_purchases', []),
#                 product_name=rec.get('product_name', ''),
#                 product_category=rec.get('product_category', ''),
#                 product_price=rec.get('product_price', 0),
#                 product_description=rec.get('product_description', ''),
#                 product_tags=rec.get('product_tags', []),
#                 product_rating=rec.get('product_rating', 0),
#                 recommendation_reasons=rec.get('recommendation_reasons', [])
#             )
#         return recommendations

#     def test_connection(self) -> Dict[str, any]:
#         """Test the Gemini API connection"""
#         if not self.is_configured:
#             return {
#                 "status": "error",
#                 "message": "Gemini API key not configured",
#                 "configured": False
#             }

#         try:
#             test_prompt = "Say 'Hello! Gemini API is working.' in a friendly way."
#             response = self.model.generate_content(test_prompt)
#             return {
#                 "status": "success",
#                 "message": "Gemini API is working correctly",
#                 "configured": True,
#                 "test_response": response.text if response else "No response",
#                 "model": self.model_name
#             }
#         except Exception as e:
#             return {
#                 "status": "error",
#                 "message": f"Gemini API test failed: {str(e)}",
#                 "configured": True,
#                 "error": str(e)
#             }

# # Global instance
# llm_service = LLMService()

# # Helper function
# def generate_explanation(
#     user,
#     product,
#     reasons: List[str],
#     recent_purchases: List[str] = None
# ) -> str:
#     """Convenience function to generate explanation"""
#     return llm_service.generate_explanation(
#         user_name=user.name,
#         user_persona=user.persona,
#         user_interests=[p.interest for p in user.preferences] if hasattr(user, 'preferences') else [],
#         user_budget_range=[user.budget_min, user.budget_max],
#         recent_purchases=recent_purchases or [],
#         product_name=product.name,
#         product_category=product.category,
#         product_price=product.price,
#         product_description=product.description or "",
#         product_tags=[t.tag for t in product.tags] if hasattr(product, 'tags') else [],
#         product_rating=product.rating or 0,
#         recommendation_reasons=reasons
#     )

"""
LLM Service - Google Gemini Integration
Generates personalized product recommendation explanations
"""
import os
import json
from typing import List, Dict, Optional
import google.generativeai as genai
from google.generativeai.types import GenerationConfig
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class LLMService:
    def __init__(self):
        self.model_name = "models/gemini-2.0-flash"
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

        if GEMINI_API_KEY:
            try:
                genai.configure(api_key=GEMINI_API_KEY)
                self.model = genai.GenerativeModel(self.model_name)
                self.is_configured = True
                print("✅ Gemini API configured successfully")
            except Exception as e:
                print(f"⚠️ Gemini API configuration failed: {e}")
                self.is_configured = False
        else:
            print("⚠️ GEMINI_API_KEY not found in environment variables")
            self.is_configured = False

    def generate_explanation(
        self,
        user_name: str,
        user_persona: str,
        user_interests: List[str],
        user_budget_range: List[float],
        recent_purchases: List[str],
        product_name: str,
        product_category: str,
        product_price: float,
        product_description: str,
        product_tags: List[str],
        product_rating: float,
        recommendation_reasons: List[str]
    ) -> str:
        """Generate personalized explanation using Gemini API"""

        if not self.is_configured:
            return self._generate_fallback_explanation(
                product_name, product_price, user_budget_range,
                recommendation_reasons, product_rating
            )

        prompt = self._build_prompt(
            user_name=user_name,
            user_persona=user_persona,
            user_interests=user_interests,
            user_budget_range=user_budget_range,
            recent_purchases=recent_purchases,
            product_name=product_name,
            product_category=product_category,
            product_price=product_price,
            product_description=product_description,
            product_tags=product_tags,
            product_rating=product_rating,
            recommendation_reasons=recommendation_reasons
        )

        try:
            response = self.model.generate_content(
                prompt,
                generation_config=GenerationConfig(
                    temperature=0.85,
                    top_p=0.9,
                    top_k=40,
                    max_output_tokens=250,
                ),
            )

            if response and response.text:
                return response.text.strip()
            else:
                print("⚠️ Empty response from Gemini, using fallback")
                return self._generate_fallback_explanation(
                    product_name, product_price, user_budget_range,
                    recommendation_reasons, product_rating
                )
        except Exception as e:
            print(f"⚠️ Gemini API error: {e}")
            return self._generate_fallback_explanation(
                product_name, product_price, user_budget_range,
                recommendation_reasons, product_rating
            )

    def _build_prompt(
        self,
        user_name: str,
        user_persona: str,
        user_interests: List[str],
        user_budget_range: List[float],
        recent_purchases: List[str],
        product_name: str,
        product_category: str,
        product_price: float,
        product_description: str,
        product_tags: List[str],
        product_rating: float,
        recommendation_reasons: List[str]
    ) -> str:
        """Builds a premium, expressive, and context-rich prompt for Gemini API."""

        prompt = f"""
    You are a smart and expressive product recommendation assistant. 
    Your goal is to write a vivid, premium-quality explanation of why a specific product is ideal for the user.

    ✅ Writing Style:
    - Start directly with the user's name (no greetings like “Hey”)
    - Sound confident, professional, and expressive — not robotic or generic
    - Highlight *who the user is* (their persona/interests)
    - Explain *why this product perfectly fits them*, mentioning 2–3 concrete product attributes
    - Optionally mention the price naturally in the flow
    - Avoid overused phrases like “you’ll love” or “based on your interests”
    - Keep it short (3–5 sentences max), natural, and flowing like a real product advisor

    ---

    USER PROFILE:
    - Name: {user_name}
    - Persona: {user_persona}
    - Interests: {', '.join(user_interests[:5])}
    - Budget Range: ${user_budget_range[0]} - ${user_budget_range[1]}
    - Recent Purchases: {', '.join(recent_purchases[:3]) if recent_purchases else 'None'}

    RECOMMENDED PRODUCT:
    - Name: {product_name}
    - Category: {product_category}
    - Price: ${product_price}
    - Rating: {product_rating}/5 stars
    - Description: {product_description}
    - Key Features: {', '.join(product_tags[:5])}

    WHY THIS PRODUCT:
    {chr(10).join(f"- {reason}" for reason in recommendation_reasons[:3])}

    ---

    ✍️ TASK:
    Write one paragraph in this expressive style:

    **Example 1:**  
    "Alex, as a tech enthusiast and developer, the MacBook Pro 16-inch M3 is your perfect coding companion. Its M3 chip effortlessly handles programming tasks, video editing, and gaming, while the 16-inch Retina display provides ample space for your workflow. At $2499, it's a premium investment that perfectly aligns with your passion for cutting-edge technology."

    **Example 2:**  
    "The Dell XPS 15 Developer Edition is built for professionals like you. With Ubuntu pre-installed and 32GB RAM, it manages multiple IDEs seamlessly. The 4K display ensures crystal-clear code rendering, and at $1799, it’s an excellent balance of performance and value."

    Now write a similar expressive, natural explanation for this user and product.

    EXPLANATION:
    """
        return prompt.strip()

    def _generate_fallback_explanation(
        self,
        product_name: str,
        product_price: float,
        user_budget_range: List[float],
        recommendation_reasons: List[str],
        product_rating: float
    ) -> str:
        """Generate rule-based explanation when API is not available"""
        explanation = f"We recommend {product_name}"

        if recommendation_reasons:
            explanation += f" because it {recommendation_reasons[0]}"
            if len(recommendation_reasons) > 1:
                explanation += f" and {recommendation_reasons[1]}"
        else:
            explanation += " based on your profile"

        if user_budget_range:
            budget_mid = (user_budget_range[0] + user_budget_range[1]) / 2
            if product_price < budget_mid * 0.5:
                explanation += f". At ${product_price:.2f}, it's an excellent value"
            elif product_price > budget_mid * 1.5:
                explanation += f". It's a premium choice at ${product_price:.2f}"
            else:
                explanation += f" at a great price of ${product_price:.2f}"

        if product_rating >= 4.5:
            explanation += f" with an outstanding {product_rating}⭐ rating"
        elif product_rating >= 4.0:
            explanation += f" and has a solid {product_rating}⭐ rating"

        explanation += "."
        return explanation

    def generate_batch_explanations(self, recommendations: List[Dict]) -> List[Dict]:
        """Generate explanations for multiple recommendations"""
        for rec in recommendations:
            rec['explanation'] = self.generate_explanation(
                user_name=rec.get('user_name', 'User'),
                user_persona=rec.get('user_persona', ''),
                user_interests=rec.get('user_interests', []),
                user_budget_range=rec.get('user_budget_range', [0, 10000]),
                recent_purchases=rec.get('recent_purchases', []),
                product_name=rec.get('product_name', ''),
                product_category=rec.get('product_category', ''),
                product_price=rec.get('product_price', 0),
                product_description=rec.get('product_description', ''),
                product_tags=rec.get('product_tags', []),
                product_rating=rec.get('product_rating', 0),
                recommendation_reasons=rec.get('recommendation_reasons', [])
            )
        return recommendations

    def test_connection(self) -> Dict[str, any]:
        """Test the Gemini API connection"""
        if not self.is_configured:
            return {
                "status": "error",
                "message": "Gemini API key not configured",
                "configured": False
            }

        try:
            test_prompt = "Say 'Hello! Gemini API is working.' in a friendly way."
            response = self.model.generate_content(test_prompt)
            return {
                "status": "success",
                "message": "Gemini API is working correctly",
                "configured": True,
                "test_response": response.text if response else "No response",
                "model": self.model_name
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Gemini API test failed: {str(e)}",
                "configured": True,
                "error": str(e)
            }

# Global instance
llm_service = LLMService()

# Helper function
def generate_explanation(
    user,
    product,
    reasons: List[str],
    recent_purchases: List[str] = None
) -> str:
    """Convenience function to generate explanation"""
    return llm_service.generate_explanation(
        user_name=user.name,
        user_persona=user.persona,
        user_interests=[p.interest for p in user.preferences] if hasattr(user, 'preferences') else [],
        user_budget_range=[user.budget_min, user.budget_max],
        recent_purchases=recent_purchases or [],
        product_name=product.name,
        product_category=product.category,
        product_price=product.price,
        product_description=product.description or "",
        product_tags=[t.tag for t in product.tags] if hasattr(product, 'tags') else [],
        product_rating=product.rating or 0,
        recommendation_reasons=reasons
    )
