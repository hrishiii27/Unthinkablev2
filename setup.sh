#!/bin/bash

# E-commerce Product Recommender - Setup Script
# This script automates the entire setup process

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print colored messages
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_header() {
    echo -e "\n${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}\n"
}

# Check if Python is installed
check_python() {
    print_info "Checking Python installation..."
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version)
        print_success "Python found: $PYTHON_VERSION"
        return 0
    else
        print_error "Python 3 is not installed. Please install Python 3.9 or higher."
        exit 1
    fi
}

# Create virtual environment
create_venv() {
    print_info "Creating virtual environment..."
    if [ -d "venv" ]; then
        print_warning "Virtual environment already exists. Skipping..."
    else
        python3 -m venv venv
        print_success "Virtual environment created"
    fi
}

# Activate virtual environment
activate_venv() {
    print_info "Activating virtual environment..."
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
        print_success "Virtual environment activated"
    elif [ -f "venv/Scripts/activate" ]; then
        source venv/Scripts/activate
        print_success "Virtual environment activated"
    else
        print_error "Could not find virtual environment activation script"
        exit 1
    fi
}

# Install dependencies
install_dependencies() {
    print_info "Installing Python dependencies..."
    pip install --upgrade pip
    pip install -r requirements.txt
    print_success "Dependencies installed successfully"
}

# Setup environment variables
setup_env() {
    print_info "Setting up environment variables..."
    if [ -f ".env" ]; then
        print_warning ".env file already exists. Skipping..."
    else
        cp .env.example .env
        print_success ".env file created from template"
        print_warning "Please edit .env and add your API keys!"
    fi
}

# Generate sample data
generate_data() {
    print_info "Generating sample data..."
    
    echo "Choose dataset size:"
    echo "1) Standard (30 products, 6 users, 250 interactions)"
    echo "2) Extended (66 products, 10 users, 400 interactions)"
    read -p "Enter choice (1 or 2): " choice
    
    if [ "$choice" = "1" ]; then
        python generate_data.py
        print_success "Standard dataset generated"
    elif [ "$choice" = "2" ]; then
        python extended_data_generator.py
        print_success "Extended dataset generated"
    else
        print_warning "Invalid choice. Generating standard dataset..."
        python generate_data.py
    fi
}

# Initialize database
init_database() {
    print_info "Initializing database..."
    python seed_database.py
    print_success "Database initialized with sample data"
}

# Run tests
run_tests() {
    print_info "Would you like to run tests? (y/n)"
    read -p "Run tests: " run_tests
    
    if [ "$run_tests" = "y" ] || [ "$run_tests" = "Y" ]; then
        print_info "Running tests..."
        pytest tests/ -v
        print_success "Tests completed"
    else
        print_warning "Skipping tests"
    fi
}

# Start server
start_server() {
    print_info "Would you like to start the server now? (y/n)"
    read -p "Start server: " start_server
    
    if [ "$start_server" = "y" ] || [ "$start_server" = "Y" ]; then
        print_success "Starting FastAPI server..."
        print_info "Server will be available at: http://localhost:8000"
        print_info "API Documentation: http://localhost:8000/docs"
        print_info "Press Ctrl+C to stop the server"
        echo ""
        uvicorn main:app --reload
    else
        print_info "You can start the server later with: uvicorn main:app --reload"
    fi
}

# Main setup flow
main() {
    clear
    print_header "🛍️  E-commerce Product Recommender - Setup"
    
    print_info "This script will set up your development environment"
    echo ""
    
    # Step 1: Check Python
    print_header "Step 1: Checking Prerequisites"
    check_python
    
    # Step 2: Create virtual environment
    print_header "Step 2: Setting Up Virtual Environment"
    create_venv
    activate_venv
    
    # Step 3: Install dependencies
    print_header "Step 3: Installing Dependencies"
    install_dependencies
    
    # Step 4: Setup environment
    print_header "Step 4: Configuration"
    setup_env
    
    # Step 5: Generate data
    print_header "Step 5: Sample Data Generation"
    generate_data
    
    # Step 6: Initialize database
    print_header "Step 6: Database Initialization"
    init_database
    
    # Step 7: Optional tests
    print_header "Step 7: Testing (Optional)"
    run_tests
    
    # Step 8: Start server
    print_header "Step 8: Starting Server"
    start_server
    
    # Final message
    print_header "🎉 Setup Complete!"
    echo ""
    print_success "Your E-commerce Product Recommender is ready!"
    echo ""
    print_info "Next steps:"
    echo "  1. Edit .env and add your LLM API keys (OpenAI/Claude)"
    echo "  2. Start the server: uvicorn main:app --reload"
    echo "  3. Visit http://localhost:8000/docs for API documentation"
    echo "  4. Check out the README.md for more information"
    echo ""
    print_info "Happy coding! 🚀"
}

# Run main function
main