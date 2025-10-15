"""
E-commerce Recommender System Integration Test
Tests all major functionality of the API
"""
import requests
import json
from time import sleep

# Configuration
BASE_URL = "http://localhost:8000"
TEST_USER_ID = 1
TEST_PRODUCT_ID = 5

# Color codes for output
class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

def print_test(test_name):
    """Print test header"""
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BLUE}Testing: {test_name}{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}")

def print_success(message):
    """Print success message"""
    print(f"{Colors.GREEN}✅ {message}{Colors.END}")

def print_error(message):
    """Print error message"""
    print(f"{Colors.RED}❌ {message}{Colors.END}")

def print_info(message):
    """Print info message"""
    print(f"{Colors.YELLOW}ℹ️  {message}{Colors.END}")

def test_health_check():
    """Test 1: Health Check"""
    print_test("Health Check Endpoint")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            data = response.json()
            print_success(f"API is healthy: {data.get('message')}")
            print_info(f"Version: {data.get('version')}")
            return True
        else:
            print_error(f"Health check failed with status {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Could not connect to API: {e}")
        print_info("Make sure the server is running: uvicorn main:app --reload")
        return False

def test_get_users():
    """Test 2: Get All Users"""
    print_test("Get All Users")
    try:
        response = requests.get(f"{BASE_URL}/users")
        if response.status_code == 200:
            users = response.json()
            print_success(f"Found {len(users)} users")
            if users:
                print_info(f"Sample user: {users[0]['name']} - {users[0]['persona']}")
            return True
        else:
            print_error(f"Failed to get users: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False

def test_get_user_detail():
    """Test 3: Get User Detail"""
    print_test(f"Get User Detail (ID: {TEST_USER_ID})")
    try:
        response = requests.get(f"{BASE_URL}/users/{TEST_USER_ID}")
        if response.status_code == 200:
            user = response.json()
            print_success(f"User found: {user['name']}")
            print_info(f"Persona: {user['persona']}")
            print_info(f"Interests: {', '.join(user['interests'][:5])}")
            print_info(f"Budget: ${user['budget_range'][0]} - ${user['budget_range'][1]}")
            return True
        else:
            print_error(f"Failed to get user: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False

def test_get_products():
    """Test 4: Get Products"""
    print_test("Get All Products")
    try:
        response = requests.get(f"{BASE_URL}/products?limit=10")
        if response.status_code == 200:
            products = response.json()
            print_success(f"Found {len(products)} products")
            if products:
                print_info(f"Sample: {products[0]['name']} - ${products[0]['price']}")
            return True
        else:
            print_error(f"Failed to get products: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False

def test_filter_products():
    """Test 5: Filter Products"""
    print_test("Filter Products (Electronics, under $1000)")
    try:
        params = {
            "category": "Electronics",
            "max_price": 1000,
            "limit": 5
        }
        response = requests.get(f"{BASE_URL}/products", params=params)
        if response.status_code == 200:
            products = response.json()
            print_success(f"Found {len(products)} matching products")
            for p in products[:3]:
                print_info(f"  • {p['name']} - ${p['price']}")
            return True
        else:
            print_error(f"Failed to filter products: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False

def test_get_categories():
    """Test 6: Get Categories"""
    print_test("Get Product Categories")
    try:
        response = requests.get(f"{BASE_URL}/categories")
        if response.status_code == 200:
            categories = response.json()['categories']
            print_success(f"Found {len(categories)} categories")
            print_info(f"Categories: {', '.join(categories)}")
            return True
        else:
            print_error(f"Failed to get categories: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False

def test_create_interaction():
    """Test 7: Create Interaction"""
    print_test("Track User Interaction")
    try:
        data = {
            "user_id": TEST_USER_ID,
            "product_id": TEST_PRODUCT_ID,
            "interaction_type": "view",
            "device": "desktop",
            "session_duration_seconds": 45
        }
        response = requests.post(f"{BASE_URL}/interactions", json=data)
        if response.status_code == 200:
            result = response.json()
            print_success(f"Interaction tracked: {result['message']}")
            print_info(f"Interaction ID: {result['interaction_id']}")
            return True
        else:
            print_error(f"Failed to create interaction: {response.status_code}")
            print_error(response.text)
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False

def test_get_user_history():
    """Test 8: Get User History"""
    print_test(f"Get User History (ID: {TEST_USER_ID})")
    try:
        response = requests.get(f"{BASE_URL}/users/{TEST_USER_ID}/history?limit=10")
        if response.status_code == 200:
            history = response.json()
            print_success(f"Found {len(history)} interactions")
            if history:
                for h in history[:3]:
                    print_info(f"  • {h['interaction_type']}: {h['product_name']} ({h['timestamp'][:10]})")
            return True
        else:
            print_error(f"Failed to get history: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False

def test_get_recommendations():
    """Test 9: Get Recommendations (CORE FEATURE)"""
    print_test(f"Get Personalized Recommendations (User {TEST_USER_ID})")
    try:
        response = requests.get(f"{BASE_URL}/recommendations/{TEST_USER_ID}?limit=5")
        if response.status_code == 200:
            recommendations = response.json()
            print_success(f"Generated {len(recommendations)} recommendations")
            print()
            for i, rec in enumerate(recommendations, 1):
                print(f"{Colors.BLUE}Recommendation #{i}:{Colors.END}")
                print(f"  📦 Product: {rec['product_name']}")
                print(f"  💰 Price: ${rec['price']}")
                print(f"  ⭐ Rating: {rec['rating']}")
                print(f"  📊 Score: {rec['score']}")
                print(f"  💡 Explanation: {rec['explanation']}")
                print(f"  🏷️  Tags: {', '.join(rec['tags'][:5])}")
                print()
            return True
        else:
            print_error(f"Failed to get recommendations: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False

def test_get_popular_products():
    """Test 10: Get Popular Products"""
    print_test("Get Popular Products")
    try:
        response = requests.get(f"{BASE_URL}/analytics/popular-products?limit=5")
        if response.status_code == 200:
            popular = response.json()
            print_success(f"Found {len(popular)} popular products")
            for p in popular:
                print_info(f"  • {p['product_name']}: {p['interaction_count']} interactions")
            return True
        else:
            print_error(f"Failed to get popular products: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False

def test_get_statistics():
    """Test 11: Get Platform Statistics"""
    print_test("Get Platform Statistics")
    try:
        response = requests.get(f"{BASE_URL}/stats")
        if response.status_code == 200:
            stats = response.json()
            print_success("Statistics retrieved")
            print_info(f"Total Users: {stats['overview']['total_users']}")
            print_info(f"Total Products: {stats['overview']['total_products']}")
            print_info(f"Total Interactions: {stats['overview']['total_interactions']}")
            print_info(f"Interaction Types: {stats['interactions_by_type']}")
            return True
        else:
            print_error(f"Failed to get statistics: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Error: {e}")
        return False

def run_all_tests():
    """Run all tests and generate report"""
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BLUE}🚀 E-commerce Recommender System - Integration Test Suite{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}")
    print_info(f"Testing API at: {BASE_URL}")
    print_info("Make sure the server is running!")
    
    # Give server time to start if just launched
    sleep(1)
    
    # Run all tests
    tests = [
        ("Health Check", test_health_check),
        ("Get All Users", test_get_users),
        ("Get User Detail", test_get_user_detail),
        ("Get Products", test_get_products),
        ("Filter Products", test_filter_products),
        ("Get Categories", test_get_categories),
        ("Create Interaction", test_create_interaction),
        ("Get User History", test_get_user_history),
        ("Get Recommendations ⭐", test_get_recommendations),
        ("Get Popular Products", test_get_popular_products),
        ("Get Statistics", test_get_statistics),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print_error(f"Test crashed: {e}")
            results.append((test_name, False))
        sleep(0.5)  # Brief pause between tests
    
    # Print summary
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.BLUE}📊 Test Summary{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}\n")
    
    if percentage >= 80:
        print(f"{Colors.GREEN}🎉 System is ready for demo!{Colors.END}\n")
    else:
        print(f"{Colors.YELLOW}⚠️  Fix failing tests before demo{Colors.END}\n")
    
    return percentage == 100

if __name__ == "__main__":
    try:
        success = run_all_tests()
        exit(0 if success else 1)
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Tests interrupted by user{Colors.END}")
        exit(1)
    except Exception as e:
        print(f"\n\n{Colors.RED}Test suite crashed: {e}{Colors.END}")
        exit(1)n")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = f"{Colors.GREEN}PASSED{Colors.END}" if result else f"{Colors.RED}FAILED{Colors.END}"
        print(f"{status} - {test_name}")
    
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    percentage = (passed / total) * 100
    
    if percentage == 100:
        print(f"{Colors.GREEN}✅ All tests passed! ({passed}/{total}){Colors.END}")
    elif percentage >= 80:
        print(f"{Colors.YELLOW}⚠️  Most tests passed ({passed}/{total}) - {percentage:.1f}%{Colors.END}")
    else:
        print(f"{Colors.RED}❌ Multiple failures ({passed}/{total}) - {percentage:.1f}%{Colors.END}")
    
    print(f"{Colors.BLUE}{'='*60}{Colors.END}\