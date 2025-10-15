import requests
import json

# Test recommendations
response = requests.get("http://localhost:8000/recommendations/67?limit=7")
data = response.json()

print("🎯 Recommendations for User 67:\n")
for i, rec in enumerate(data, 1):
    print(f"{i}. {rec['product_name']} - ${rec['price']}")
    print(f"   Rating: {rec['rating']}⭐")
    print(f"   Score: {rec['score']}")
    print(f"   💡 {rec['explanation']}\n")