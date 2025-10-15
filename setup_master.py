# """
# Master Setup Script - E-commerce Product Recommender
# This script automates the ENTIRE setup process:
# 1. Generate sample data
# 2. Create database
# 3. Populate database
# 4. Verify setup
# 5. Run tests
# 6. (Optional) Start server
# """

# import os
# import sys
# import subprocess
# import json
# from pathlib import Path
# from time import sleep

# # Colors for terminal output
# class Colors:
#     HEADER = '\033[95m'
#     BLUE = '\033[94m'
#     CYAN = '\033[96m'
#     GREEN = '\033[92m'
#     YELLOW = '\033[93m'
#     RED = '\033[91m'
#     END = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'

# def print_header(text):
#     """Print section header"""
#     print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}")
#     print(f"{Colors.BOLD}{Colors.BLUE}{text:^70}{Colors.END}")
#     print(f"{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}\n")

# def print_step(step_num, total_steps, text):
#     """Print step indicator"""
#     print(f"\n{Colors.CYAN}[Step {step_num}/{total_steps}]{Colors.END} {Colors.BOLD}{text}{Colors.END}")

# def print_success(text):
#     """Print success message"""
#     print(f"{Colors.GREEN}✅ {text}{Colors.END}")

# def print_error(text):
#     """Print error message"""
#     print(f"{Colors.RED}❌ {text}{Colors.END}")

# def print_warning(text):
#     """Print warning message"""
#     print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")

# def print_info(text):
#     """Print info message"""
#     print(f"{Colors.BLUE}ℹ️  {text}{Colors.END}")

# def check_python_version():
#     """Check if Python version is adequate"""
#     version = sys.version_info
#     if version.major < 3 or (version.major == 3 and version.minor < 9):
#         print_error(f"Python 3.9+ required. You have {version.major}.{version.minor}")
#         return False
#     print_success(f"Python {version.major}.{version.minor}.{version.micro} detected")
#     return True

# def check_dependencies():
#     """Check if required packages are installed"""
#     print_info("Checking dependencies...")
    
#     required = ['fastapi', 'uvicorn', 'sqlalchemy', 'pandas']
#     missing = []
    
#     for package in required:
#         try:
#             __import__(package)
#             print_success(f"{package} installed")
#         except ImportError:
#             missing.append(package)
#             print_warning(f"{package} not found")
    
#     if missing:
#         print_warning("Some packages are missing. Installing...")
#         try:
#             subprocess.check_call([
#                 sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'
#             ])
#             print_success("All dependencies installed!")
#             return True
#         except:
#             print_error("Failed to install dependencies")
#             print_info("Please run manually: pip install -r requirements.txt")
#             return False
    
#     print_success("All dependencies are installed!")
#     return True

# def generate_sample_data():
#     """Step 1: Generate sample data files"""
#     print_step(1, 6, "Generating Sample Data")
    
#     # Check which generator exists
#     if Path('extended_data_generator.py').exists():
#         script = 'extended_data_generator.py'
#         print_info("Using extended data generator (66 products, 10 users)")
#     elif Path('generate_data.py').exists():
#         script = 'generate_data.py'
#         print_info("Using basic data generator (30 products, 6 users)")
#     else:
#         print_error("No data generator script found!")
#         return False
    
#     try:
#         # Run the generator
#         result = subprocess.run(
#             [sys.executable, script],
#             capture_output=True,
#             text=True,
#             timeout=30
#         )
        
#         if result.returncode == 0:
#             print_success("Sample data generated successfully!")
            
#             # Check output files
#             expected_files = [
#                 'products_large.json' if 'extended' in script else 'products.json',
#                 'users_large.json' if 'extended' in script else 'users.json',
#                 'interactions_large.json' if 'extended' in script else 'interactions.json'
#             ]
            
#             for file in expected_files:
#                 if Path(file).exists():
#                     size = Path(file).stat().st_size
#                     print_success(f"  {file} ({size} bytes)")
#                 else:
#                     # Try alternate names
#                     alt_file = file.replace('_large', '')
#                     if Path(alt_file).exists():
#                         print_success(f"  {alt_file} ({Path(alt_file).stat().st_size} bytes)")
            
#             return True
#         else:
#             print_error(f"Data generation failed: {result.stderr}")
#             return False
            
#     except Exception as e:
#         print_error(f"Error running data generator: {e}")
#         return False

# def create_database():
#     """Step 2: Create and populate database"""
#     print_step(2, 6, "Creating and Populating Database")
    
#     if not Path('seed_database.py').exists():
#         print_error("seed_database.py not found!")
#         return False
    
#     try:
#         # Run database seeding
#         result = subprocess.run(
#             [sys.executable, 'seed_database.py'],
#             capture_output=True,
#             text=True,
#             timeout=60
#         )
        
#         if result.returncode == 0:
#             print_success("Database created and populated!")
            
#             # Check database file
#             if Path('ecommerce.db').exists():
#                 size = Path('ecommerce.db').stat().st_size / 1024  # KB
#                 print_success(f"  ecommerce.db created ({size:.1f} KB)")
            
#             # Parse output to show stats
#             if "Seeded" in result.stdout:
#                 for line in result.stdout.split('\n'):
#                     if '✅' in line or 'Seeded' in line:
#                         print(f"  {line}")
            
#             return True
#         else:
#             print_error(f"Database setup failed: {result.stderr}")
#             return False
            
#     except Exception as e:
#         print_error(f"Error setting up database: {e}")
#         return False

# def verify_database():
#     """Step 3: Verify database contents"""
#     print_step(3, 6, "Verifying Database Contents")
    
#     try:
#         # Import database components
#         from seed_database import SessionLocal, User, Product, Interaction
        
#         db = SessionLocal()
        
#         # Count records
#         user_count = db.query(User).count()
#         product_count = db.query(Product).count()
#         interaction_count = db.query(Interaction).count()
        
#         db.close()
        
#         print_success(f"Users: {user_count}")
#         print_success(f"Products: {product_count}")
#         print_success(f"Interactions: {interaction_count}")
        
#         # Verify minimum data
#         if user_count > 0 and product_count > 0 and interaction_count > 0:
#             print_success("Database verification passed!")
#             return True
#         else:
#             print_error("Database is empty or incomplete")
#             return False
            
#     except Exception as e:
#         print_error(f"Database verification failed: {e}")
#         return False

# def create_env_file():
#     """Step 4: Create .env file if not exists"""
#     print_step(4, 6, "Setting Up Configuration")
    
#     if Path('.env').exists():
#         print_success(".env file already exists")
#         return True
    
#     if Path('.env.example').exists():
#         try:
#             with open('.env.example', 'r') as src:
#                 content = src.read()
            
#             with open('.env', 'w') as dst:
#                 dst.write(content)
            
#             print_success(".env file created from template")
#             print_warning("Remember to add your LLM API keys to .env!")
#             return True
#         except Exception as e:
#             print_error(f"Failed to create .env: {e}")
#             return False
#     else:
#         print_warning(".env.example not found, skipping...")
#         return True

# def run_tests():
#     """Step 5: Run system tests"""
#     print_step(5, 6, "Running Integration Tests")
    
#     if not Path('test_system.py').exists():
#         print_warning("test_system.py not found, skipping tests")
#         return True
    
#     print_info("Starting API server for testing...")
    
#     # Start server in background
#     server_process = None
#     try:
#         server_process = subprocess.Popen(
#             [sys.executable, '-m', 'uvicorn', 'main:app', '--port', '8000'],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE
#         )
        
#         # Wait for server to start
#         print_info("Waiting for server to start...")
#         sleep(3)
        
#         # Run tests
#         print_info("Running tests...")
#         result = subprocess.run(
#             [sys.executable, 'test_system.py'],
#             capture_output=True,
#             text=True,
#             timeout=30
#         )
        
#         # Show test output
#         print(result.stdout)
        
#         if 'All tests passed' in result.stdout or result.returncode == 0:
#             print_success("All tests passed!")
#             return True
#         else:
#             print_warning("Some tests failed, but setup is complete")
#             return True
            
#     except Exception as e:
#         print_error(f"Test execution error: {e}")
#         return False
        
#     finally:
#         # Stop server
#         if server_process:
#             server_process.terminate()
#             server_process.wait()
#             print_info("Test server stopped")

# def show_summary():
#     """Step 6: Show setup summary and next steps"""
#     print_step(6, 6, "Setup Complete!")
    
#     print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 Your E-commerce Product Recommender is Ready!{Colors.END}\n")
    
#     print(f"{Colors.BOLD}📁 Project Structure:{Colors.END}")
#     files = [
#         ('ecommerce.db', 'SQLite database'),
#         ('products_extended.json', 'Product catalog data'),
#         ('users_extended.json', 'User profile data'),
#         ('interactions_extended.json', 'Interaction history'),
#         ('main.py', 'FastAPI application'),
#         ('.env', 'Configuration file'),
#     ]
    
#     for file, desc in files:
#         # Check alternate names
#         if not Path(file).exists():
#             alt_file = file.replace('_extended', '')
#             if Path(alt_file).exists():
#                 file = alt_file
        
#         if Path(file).exists():
#             print(f"  ✅ {file:<30} - {desc}")
#         else:
#             print(f"  ⚠️  {file:<30} - {desc} (not found)")
    
#     print(f"\n{Colors.BOLD}🚀 Next Steps:{Colors.END}")
#     print(f"  1. {Colors.CYAN}Start the server:{Colors.END}")
#     print(f"     uvicorn main:app --reload")
#     print(f"\n  2. {Colors.CYAN}Visit API documentation:{Colors.END}")
#     print(f"     http://localhost:8000/docs")
#     print(f"\n  3. {Colors.CYAN}Test recommendations:{Colors.END}")
#     print(f"     curl http://localhost:8000/recommendations/1?limit=5")
#     print(f"\n  4. {Colors.CYAN}(Optional) Add LLM API keys:{Colors.END}")
#     print(f"     Edit .env file and add OPENAI_API_KEY or ANTHROPIC_API_KEY")
    
#     print(f"\n{Colors.BOLD}📚 Documentation:{Colors.END}")
#     print(f"  • README.md - Full documentation")
#     print(f"  • QUICK_START.md - Quick reference")
#     print(f"  • /docs endpoint - Interactive API docs")
    
#     print(f"\n{Colors.BOLD}🧪 Testing:{Colors.END}")
#     print(f"  • python test_system.py - Run integration tests")
#     print(f"  • Check /stats endpoint for analytics")
    
#     print(f"\n{Colors.GREEN}✨ Setup completed successfully!{Colors.END}")
#     print(f"{Colors.BLUE}Happy coding! 🚀{Colors.END}\n")

# def ask_start_server():
#     """Ask if user wants to start the server now"""
#     print(f"\n{Colors.BOLD}Would you like to start the server now? (y/n): {Colors.END}", end='')
    
#     try:
#         response = input().strip().lower()
#         if response in ['y', 'yes']:
#             print(f"\n{Colors.GREEN}Starting FastAPI server...{Colors.END}")
#             print(f"{Colors.BLUE}Press Ctrl+C to stop{Colors.END}\n")
#             sleep(1)
            
#             try:
#                 subprocess.run([
#                     sys.executable, '-m', 'uvicorn', 'main:app', '--reload'
#                 ])
#             except KeyboardInterrupt:
#                 print(f"\n\n{Colors.YELLOW}Server stopped{Colors.END}")
#         else:
#             print(f"\n{Colors.INFO}You can start the server later with:{Colors.END}")
#             print(f"  uvicorn main:app --reload\n")
#     except:
#         pass

# def main():
#     """Main setup orchestration"""
#     # Print banner
#     print(f"\n{Colors.BOLD}{Colors.BLUE}")
#     print("╔" + "═" * 68 + "╗")
#     print("║" + "🛍️  E-COMMERCE PRODUCT RECOMMENDER - MASTER SETUP".center(68) + "║")
#     print("║" + "Automated Setup Script".center(68) + "║")
#     print("╚" + "═" * 68 + "╝")
#     print(f"{Colors.END}\n")
    
#     print_info("This script will set up your entire project automatically")
#     print_info("Estimated time: 1-2 minutes\n")
    
#     sleep(1)
    
#     # Pre-flight checks
#     print_header("PRE-FLIGHT CHECKS")
    
#     if not check_python_version():
#         return 1
    
#     if not check_dependencies():
#         return 1
    
#     # Main setup steps
#     print_header("SETUP PROCESS")
    
#     steps = [
#         ("Generating sample data", generate_sample_data),
#         ("Creating database", create_database),
#         ("Verifying database", verify_database),
#         ("Setting up configuration", create_env_file),
#         ("Running tests", run_tests),
#     ]
    
#     for step_name, step_func in steps:
#         if not step_func():
#             print_error(f"\n❌ Setup failed at: {step_name}")
#             print_info("Please check the error messages above")
#             return 1
#         sleep(0.5)
    
#     # Show summary
#     print_header("SETUP SUMMARY")
#     show_summary()
    
#     # Ask to start server
#     ask_start_server()
    
#     return 0

# if __name__ == "__main__":
#     try:
#         exit_code = main()
#         sys.exit(exit_code)
#     except KeyboardInterrupt:
#         print(f"\n\n{Colors.YELLOW}Setup interrupted by user{Colors.END}")
#         sys.exit(1)
#     except Exception as e:
#         print(f"\n\n{Colors.RED}Unexpected error: {e}{Colors.END}")
#         sys.exit(1)


"""
Master Setup Script - E-commerce Product Recommender
This script automates the ENTIRE setup process:
1. Generate sample data
2. Create database
3. Populate database
4. Verify setup
5. Run tests
6. (Optional) Start server
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from time import sleep

# Colors for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    """Print section header"""
    print(f"\n{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{text:^70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.BLUE}{'='*70}{Colors.END}\n")

def print_step(step_num, total_steps, text):
    """Print step indicator"""
    print(f"\n{Colors.CYAN}[Step {step_num}/{total_steps}]{Colors.END} {Colors.BOLD}{text}{Colors.END}")

def print_success(text):
    """Print success message"""
    print(f"{Colors.GREEN}✅ {text}{Colors.END}")

def print_error(text):
    """Print error message"""
    print(f"{Colors.RED}❌ {text}{Colors.END}")

def print_warning(text):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠️  {text}{Colors.END}")

def print_info(text):
    """Print info message"""
    print(f"{Colors.BLUE}ℹ️  {text}{Colors.END}")

def check_python_version():
    """Check if Python version is adequate"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print_error(f"Python 3.9+ required. You have {version.major}.{version.minor}")
        return False
    print_success(f"Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def check_dependencies():
    """Check if required packages are installed"""
    print_info("Checking dependencies...")
    
    required = ['fastapi', 'uvicorn', 'sqlalchemy', 'pandas']
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print_success(f"{package} installed")
        except ImportError:
            missing.append(package)
            print_warning(f"{package} not found")
    
    if missing:
        print_warning("Some packages are missing. Installing...")
        try:
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'
            ])
            print_success("All dependencies installed!")
            return True
        except:
            print_error("Failed to install dependencies")
            print_info("Please run manually: pip install -r requirements.txt")
            return False
    
    print_success("All dependencies are installed!")
    return True

def generate_sample_data():
    """Step 1: Generate sample data files"""
    print_step(1, 6, "Generating Sample Data")
    
    # Check which generators exist and prioritize large dataset
    generators = [
        ('generate_large_dataset.py', 'large-scale dataset (150 users, 1800 products, 5000 interactions)'),
        ('extended_data_generator.py', 'extended dataset (10 users, 66 products, 400 interactions)'),
        ('generate_data.py', 'basic dataset (6 users, 30 products, 250 interactions)')
    ]
    
    script = None
    description = None
    
    # Find first available generator
    for gen_script, gen_desc in generators:
        if Path(gen_script).exists():
            script = gen_script
            description = gen_desc
            break
    
    if not script:
        print_error("No data generator script found!")
        return False
    
    # If large dataset generator exists, prefer it
    if Path('generate_large_dataset.py').exists():
        script = 'generate_large_dataset.py'
        description = generators[0][1]
        print_info(f"Using {description}")
        print_info("⚡ This will generate a comprehensive dataset for realistic testing")
    else:
        print_info(f"Using {description}")
    
    try:
        # Run the generator
        result = subprocess.run(
            [sys.executable, script],
            capture_output=True,
            text=True,
            timeout=120  # Increased timeout for large dataset
        )
        
        if result.returncode == 0:
            print_success("Sample data generated successfully!")
            
            # Check output files - try all possible names
            possible_files = [
                ('products_large.json', 'products_extended.json', 'products.json'),
                ('users_large.json', 'users_extended.json', 'users.json'),
                ('interactions_large.json', 'interactions_extended.json', 'interactions.json')
            ]
            
            for file_options in possible_files:
                found = False
                for fname in file_options:
                    if Path(fname).exists():
                        size = Path(fname).stat().st_size / 1024  # KB
                        print_success(f"  {fname} ({size:.1f} KB)")
                        found = True
                        break
                if not found:
                    print_warning(f"  Expected one of: {', '.join(file_options)}")
            
            return True
        else:
            print_error(f"Data generation failed: {result.stderr}")
            return False
            
    except Exception as e:
        print_error(f"Error running data generator: {e}")
        return False

def create_database():
    """Step 2: Create and populate database"""
    print_step(2, 6, "Creating and Populating Database")
    
    if not Path('seed_database.py').exists():
        print_error("seed_database.py not found!")
        return False
    
    try:
        # Run database seeding
        result = subprocess.run(
            [sys.executable, 'seed_database.py'],
            capture_output=True,
            text=True,
            timeout=60
        )
        
        if result.returncode == 0:
            print_success("Database created and populated!")
            
            # Check database file
            if Path('ecommerce.db').exists():
                size = Path('ecommerce.db').stat().st_size / 1024  # KB
                print_success(f"  ecommerce.db created ({size:.1f} KB)")
            
            # Parse output to show stats
            if "Seeded" in result.stdout:
                for line in result.stdout.split('\n'):
                    if '✅' in line or 'Seeded' in line:
                        print(f"  {line}")
            
            return True
        else:
            print_error(f"Database setup failed: {result.stderr}")
            return False
            
    except Exception as e:
        print_error(f"Error setting up database: {e}")
        return False

def verify_database():
    """Step 3: Verify database contents"""
    print_step(3, 6, "Verifying Database Contents")
    
    try:
        # Import database components
        from seed_database import SessionLocal, User, Product, Interaction
        
        db = SessionLocal()
        
        # Count records
        user_count = db.query(User).count()
        product_count = db.query(Product).count()
        interaction_count = db.query(Interaction).count()
        
        db.close()
        
        print_success(f"Users: {user_count}")
        print_success(f"Products: {product_count}")
        print_success(f"Interactions: {interaction_count}")
        
        # Verify minimum data
        if user_count > 0 and product_count > 0 and interaction_count > 0:
            print_success("Database verification passed!")
            return True
        else:
            print_error("Database is empty or incomplete")
            return False
            
    except Exception as e:
        print_error(f"Database verification failed: {e}")
        return False

def create_env_file():
    """Step 4: Create .env file if not exists"""
    print_step(4, 6, "Setting Up Configuration")
    
    if Path('.env').exists():
        print_success(".env file already exists")
        return True
    
    if Path('.env.example').exists():
        try:
            with open('.env.example', 'r') as src:
                content = src.read()
            
            with open('.env', 'w') as dst:
                dst.write(content)
            
            print_success(".env file created from template")
            print_warning("Remember to add your LLM API keys to .env!")
            return True
        except Exception as e:
            print_error(f"Failed to create .env: {e}")
            return False
    else:
        print_warning(".env.example not found, skipping...")
        return True

def run_tests():
    """Step 5: Run system tests"""
    print_step(5, 6, "Running Integration Tests")
    
    if not Path('test_system.py').exists():
        print_warning("test_system.py not found, skipping tests")
        return True
    
    print_info("Starting API server for testing...")
    
    # Start server in background
    server_process = None
    try:
        server_process = subprocess.Popen(
            [sys.executable, '-m', 'uvicorn', 'main:app', '--port', '8000'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait for server to start
        print_info("Waiting for server to start...")
        sleep(3)
        
        # Run tests
        print_info("Running tests...")
        result = subprocess.run(
            [sys.executable, 'test_system.py'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Show test output
        print(result.stdout)
        
        if 'All tests passed' in result.stdout or result.returncode == 0:
            print_success("All tests passed!")
            return True
        else:
            print_warning("Some tests failed, but setup is complete")
            return True
            
    except Exception as e:
        print_error(f"Test execution error: {e}")
        return False
        
    finally:
        # Stop server
        if server_process:
            server_process.terminate()
            server_process.wait()
            print_info("Test server stopped")

def show_summary():
    """Step 6: Show setup summary and next steps"""
    print_step(6, 6, "Setup Complete!")
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 Your E-commerce Product Recommender is Ready!{Colors.END}\n")
    
    print(f"{Colors.BOLD}📁 Project Structure:{Colors.END}")
    files = [
        ('ecommerce.db', 'SQLite database'),
        ('products_extended.json', 'Product catalog data'),
        ('users_extended.json', 'User profile data'),
        ('interactions_extended.json', 'Interaction history'),
        ('main.py', 'FastAPI application'),
        ('.env', 'Configuration file'),
    ]
    
    for file, desc in files:
        # Check alternate names
        if not Path(file).exists():
            alt_file = file.replace('_extended', '')
            if Path(alt_file).exists():
                file = alt_file
        
        if Path(file).exists():
            print(f"  ✅ {file:<30} - {desc}")
        else:
            print(f"  ⚠️  {file:<30} - {desc} (not found)")
    
    print(f"\n{Colors.BOLD}🚀 Next Steps:{Colors.END}")
    print(f"  1. {Colors.CYAN}Start the server:{Colors.END}")
    print(f"     uvicorn main:app --reload")
    print(f"\n  2. {Colors.CYAN}Visit API documentation:{Colors.END}")
    print(f"     http://localhost:8000/docs")
    print(f"\n  3. {Colors.CYAN}Test recommendations:{Colors.END}")
    print(f"     curl http://localhost:8000/recommendations/1?limit=5")
    print(f"\n  4. {Colors.CYAN}(Optional) Add LLM API keys:{Colors.END}")
    print(f"     Edit .env file and add OPENAI_API_KEY or ANTHROPIC_API_KEY")
    
    print(f"\n{Colors.BOLD}📚 Documentation:{Colors.END}")
    print(f"  • README.md - Full documentation")
    print(f"  • QUICK_START.md - Quick reference")
    print(f"  • /docs endpoint - Interactive API docs")
    
    print(f"\n{Colors.BOLD}🧪 Testing:{Colors.END}")
    print(f"  • python test_system.py - Run integration tests")
    print(f"  • Check /stats endpoint for analytics")
    
    print(f"\n{Colors.GREEN}✨ Setup completed successfully!{Colors.END}")
    print(f"{Colors.BLUE}Happy coding! 🚀{Colors.END}\n")

def ask_start_server():
    """Ask if user wants to start the server now"""
    print(f"\n{Colors.BOLD}Would you like to start the server now? (y/n): {Colors.END}", end='')
    
    try:
        response = input().strip().lower()
        if response in ['y', 'yes']:
            print(f"\n{Colors.GREEN}Starting FastAPI server...{Colors.END}")
            print(f"{Colors.BLUE}Press Ctrl+C to stop{Colors.END}\n")
            sleep(1)
            
            try:
                subprocess.run([
                    sys.executable, '-m', 'uvicorn', 'main:app', '--reload'
                ])
            except KeyboardInterrupt:
                print(f"\n\n{Colors.YELLOW}Server stopped{Colors.END}")
        else:
            print(f"\n{Colors.INFO}You can start the server later with:{Colors.END}")
            print(f"  uvicorn main:app --reload\n")
    except:
        pass

def main():
    """Main setup orchestration"""
    # Print banner
    print(f"\n{Colors.BOLD}{Colors.BLUE}")
    print("╔" + "═" * 68 + "╗")
    print("║" + "🛍️  E-COMMERCE PRODUCT RECOMMENDER - MASTER SETUP".center(68) + "║")
    print("║" + "Automated Setup Script".center(68) + "║")
    print("╚" + "═" * 68 + "╝")
    print(f"{Colors.END}\n")
    
    print_info("This script will set up your entire project automatically")
    print_info("Estimated time: 1-2 minutes\n")
    
    sleep(1)
    
    # Pre-flight checks
    print_header("PRE-FLIGHT CHECKS")
    
    if not check_python_version():
        return 1
    
    if not check_dependencies():
        return 1
    
    # Main setup steps
    print_header("SETUP PROCESS")
    
    steps = [
        ("Generating sample data", generate_sample_data),
        ("Creating database", create_database),
        ("Verifying database", verify_database),
        ("Setting up configuration", create_env_file),
        ("Running tests", run_tests),
    ]
    
    for step_name, step_func in steps:
        if not step_func():
            print_error(f"\n❌ Setup failed at: {step_name}")
            print_info("Please check the error messages above")
            return 1
        sleep(0.5)
    
    # Show summary
    print_header("SETUP SUMMARY")
    show_summary()
    
    # Ask to start server
    ask_start_server()
    
    return 0

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Setup interrupted by user{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n{Colors.RED}Unexpected error: {e}{Colors.END}")
        sys.exit(1)