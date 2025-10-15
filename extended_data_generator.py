# import json
# import random
# from datetime import datetime, timedelta

# # Extended product catalog with 60+ products
# EXTENDED_PRODUCTS = [
#     {
#         "id": 1,
#         "name": "MacBook Pro 16-inch M3",
#         "category": "Electronics",
#         "subcategory": "Laptops",
#         "price": 2499.99,
#         "brand": "Apple",
#         "rating": 4.8,
#         "description": "Powerful laptop with M3 chip, 16GB RAM, 512GB SSD",
#         "features": ["M3 chip", "16GB RAM", "512GB SSD", "16-inch display", "macOS"],
#         "tags": ["premium", "programming", "video-editing", "creative"],
#         "stock": 45
#     },
#     {
#         "id": 2,
#         "name": "Dell XPS 15 Developer Edition",
#         "category": "Electronics",
#         "subcategory": "Laptops",
#         "price": 1799.99,
#         "brand": "Dell",
#         "rating": 4.6,
#         "description": "High-performance laptop for developers with Ubuntu",
#         "features": ["Intel i7", "32GB RAM", "1TB SSD", "15.6-inch 4K display", "Ubuntu"],
#         "tags": ["programming", "developer", "linux", "performance"],
#         "stock": 32
#     },
#     {
#         "id": 3,
#         "name": "ASUS ROG Gaming Laptop",
#         "category": "Electronics",
#         "subcategory": "Laptops",
#         "price": 1599.99,
#         "brand": "ASUS",
#         "rating": 4.7,
#         "description": "Gaming powerhouse with RTX 4060",
#         "features": ["RTX 4060", "16GB RAM", "512GB SSD", "144Hz display", "RGB keyboard"],
#         "tags": ["gaming", "high-performance", "rgb", "entertainment"],
#         "stock": 28
#     },
    
#     # Electronics - Phones
#     {
#         "id": 4,
#         "name": "iPhone 15 Pro",
#         "category": "Electronics",
#         "subcategory": "Smartphones",
#         "price": 999.99,
#         "brand": "Apple",
#         "rating": 4.7,
#         "description": "Latest iPhone with A17 Pro chip and titanium design",
#         "features": ["A17 Pro chip", "256GB storage", "Pro camera system", "Titanium design"],
#         "tags": ["premium", "photography", "5g", "ios"],
#         "stock": 67
#     },
#     {
#         "id": 5,
#         "name": "Samsung Galaxy S24 Ultra",
#         "category": "Electronics",
#         "subcategory": "Smartphones",
#         "price": 1199.99,
#         "brand": "Samsung",
#         "rating": 4.6,
#         "description": "Flagship Android phone with S Pen",
#         "features": ["Snapdragon 8 Gen 3", "512GB storage", "200MP camera", "S Pen included"],
#         "tags": ["android", "productivity", "photography", "premium"],
#         "stock": 54
#     },
#     {
#         "id": 6,
#         "name": "Google Pixel 8",
#         "category": "Electronics",
#         "subcategory": "Smartphones",
#         "price": 699.99,
#         "brand": "Google",
#         "rating": 4.5,
#         "description": "Pure Android experience with amazing AI features",
#         "features": ["Google Tensor G3", "128GB storage", "AI photography", "Clean Android"],
#         "tags": ["android", "photography", "ai", "affordable"],
#         "stock": 41
#     },
    
#     # Electronics - Headphones
#     {
#         "id": 7,
#         "name": "Sony WH-1000XM5",
#         "category": "Electronics",
#         "subcategory": "Headphones",
#         "price": 399.99,
#         "brand": "Sony",
#         "rating": 4.8,
#         "description": "Industry-leading noise cancellation headphones",
#         "features": ["Active noise cancellation", "30hr battery", "Hi-Res audio", "Multipoint connection"],
#         "tags": ["audio", "noise-cancelling", "premium", "travel"],
#         "stock": 73
#     },
#     {
#         "id": 8,
#         "name": "AirPods Pro 2nd Gen",
#         "category": "Electronics",
#         "subcategory": "Headphones",
#         "price": 249.99,
#         "brand": "Apple",
#         "rating": 4.7,
#         "description": "Premium wireless earbuds with spatial audio",
#         "features": ["Active noise cancellation", "Spatial audio", "MagSafe charging", "IPX4 water resistant"],
#         "tags": ["wireless", "apple-ecosystem", "compact", "premium"],
#         "stock": 89
#     },
    
#     # Books
#     {
#         "id": 9,
#         "name": "Atomic Habits by James Clear",
#         "category": "Books",
#         "subcategory": "Self-Help",
#         "price": 16.99,
#         "brand": "Penguin Random House",
#         "rating": 4.9,
#         "description": "Practical strategies for forming good habits",
#         "features": ["Hardcover", "320 pages", "Bestseller", "Illustrated"],
#         "tags": ["self-improvement", "productivity", "habits", "bestseller"],
#         "stock": 156
#     },
#     {
#         "id": 10,
#         "name": "The Pragmatic Programmer",
#         "category": "Books",
#         "subcategory": "Technology",
#         "price": 49.99,
#         "brand": "Addison-Wesley",
#         "rating": 4.8,
#         "description": "Essential reading for software developers",
#         "features": ["Paperback", "352 pages", "20th Anniversary Edition", "Code examples"],
#         "tags": ["programming", "software-development", "technical", "reference"],
#         "stock": 92
#     },
#     {
#         "id": 11,
#         "name": "Dune by Frank Herbert",
#         "category": "Books",
#         "subcategory": "Science Fiction",
#         "price": 18.99,
#         "brand": "Ace Books",
#         "rating": 4.7,
#         "description": "Epic sci-fi masterpiece set on desert planet Arrakis",
#         "features": ["Paperback", "688 pages", "Classic", "Award winner"],
#         "tags": ["sci-fi", "classic", "adventure", "fantasy"],
#         "stock": 124
#     },
    
#     # Fitness
#     {
#         "id": 12,
#         "name": "Yoga Mat Pro - Extra Thick",
#         "category": "Fitness",
#         "subcategory": "Yoga",
#         "price": 39.99,
#         "brand": "FitLife",
#         "rating": 4.6,
#         "description": "Non-slip yoga mat with alignment marks",
#         "features": ["6mm thick", "Non-toxic", "Carrying strap", "72 inch length"],
#         "tags": ["yoga", "exercise", "home-workout", "eco-friendly"],
#         "stock": 203
#     },
#     {
#         "id": 13,
#         "name": "Resistance Bands Set (5-Pack)",
#         "category": "Fitness",
#         "subcategory": "Strength Training",
#         "price": 24.99,
#         "brand": "FitLife",
#         "rating": 4.5,
#         "description": "Complete resistance band set for strength training",
#         "features": ["5 resistance levels", "Door anchor", "Handles included", "Travel bag"],
#         "tags": ["strength-training", "portable", "home-gym", "versatile"],
#         "stock": 167
#     },
#     {
#         "id": 14,
#         "name": "Smart Fitness Watch",
#         "category": "Fitness",
#         "subcategory": "Wearables",
#         "price": 199.99,
#         "brand": "FitTrack",
#         "rating": 4.4,
#         "description": "Track your workouts, heart rate, and sleep",
#         "features": ["Heart rate monitor", "GPS tracking", "7-day battery", "Water resistant"],
#         "tags": ["fitness-tracking", "smart-device", "health", "wearable"],
#         "stock": 88
#     },
    
#     # Home & Kitchen
#     {
#         "id": 15,
#         "name": "Espresso Machine Deluxe",
#         "category": "Home & Kitchen",
#         "subcategory": "Coffee Makers",
#         "price": 299.99,
#         "brand": "BrewMaster",
#         "rating": 4.6,
#         "description": "Professional-grade espresso machine for home",
#         "features": ["15-bar pressure", "Milk frother", "Programmable", "Stainless steel"],
#         "tags": ["coffee", "kitchen", "barista", "premium"],
#         "stock": 56
#     },
#     {
#         "id": 16,
#         "name": "Air Fryer 6-Quart",
#         "category": "Home & Kitchen",
#         "subcategory": "Appliances",
#         "price": 89.99,
#         "brand": "CookPro",
#         "rating": 4.7,
#         "description": "Healthy cooking with rapid air circulation",
#         "features": ["6-quart capacity", "8 presets", "Digital display", "Dishwasher safe"],
#         "tags": ["cooking", "healthy", "kitchen", "convenient"],
#         "stock": 142
#     },
#     {
#         "id": 17,
#         "name": "Robot Vacuum Cleaner",
#         "category": "Home & Kitchen",
#         "subcategory": "Cleaning",
#         "price": 349.99,
#         "brand": "CleanBot",
#         "rating": 4.5,
#         "description": "Smart vacuum with mapping technology",
#         "features": ["Smart mapping", "App control", "Auto-charging", "HEPA filter"],
#         "tags": ["smart-home", "automation", "cleaning", "convenient"],
#         "stock": 67
#     },
    
#     # Fashion
#     {
#         "id": 18,
#         "name": "Wireless Mechanical Keyboard",
#         "category": "Electronics",
#         "subcategory": "Accessories",
#         "price": 129.99,
#         "brand": "KeyTech",
#         "rating": 4.6,
#         "description": "Premium mechanical keyboard for productivity",
#         "features": ["Cherry MX switches", "RGB backlight", "Bluetooth 5.0", "100hr battery"],
#         "tags": ["productivity", "gaming", "wireless", "ergonomic"],
#         "stock": 94
#     },
#     {
#         "id": 19,
#         "name": "4K Webcam Pro",
#         "category": "Electronics",
#         "subcategory": "Accessories",
#         "price": 149.99,
#         "brand": "VidStream",
#         "rating": 4.5,
#         "description": "Professional webcam for streaming and meetings",
#         "features": ["4K resolution", "Auto-focus", "Ring light", "Noise-cancelling mic"],
#         "tags": ["video-calls", "streaming", "work-from-home", "content-creation"],
#         "stock": 76
#     },
#     {
#         "id": 20,
#         "name": "Portable SSD 1TB",
#         "category": "Electronics",
#         "subcategory": "Storage",
#         "price": 119.99,
#         "brand": "DataFast",
#         "rating": 4.7,
#         "description": "Ultra-fast portable storage with USB-C",
#         "features": ["1TB capacity", "1000MB/s read speed", "USB-C", "Compact design"],
#         "tags": ["storage", "portable", "fast", "backup"],
#         "stock": 134
#     },
    
#     # More Books
#     {
#         "id": 21,
#         "name": "Designing Data-Intensive Applications",
#         "category": "Books",
#         "subcategory": "Technology",
#         "price": 54.99,
#         "brand": "O'Reilly",
#         "rating": 4.9,
#         "description": "The big ideas behind reliable, scalable systems",
#         "features": ["Paperback", "616 pages", "Comprehensive", "Industry standard"],
#         "tags": ["programming", "databases", "system-design", "technical"],
#         "stock": 68
#     },
#     {
#         "id": 22,
#         "name": "The Psychology of Money",
#         "category": "Books",
#         "subcategory": "Finance",
#         "price": 14.99,
#         "brand": "Harriman House",
#         "rating": 4.8,
#         "description": "Timeless lessons on wealth and happiness",
#         "features": ["Paperback", "256 pages", "Bestseller", "Practical advice"],
#         "tags": ["finance", "investing", "self-improvement", "bestseller"],
#         "stock": 187
#     },
    
#     # More Fitness
#     {
#         "id": 23,
#         "name": "Adjustable Dumbbells Set",
#         "category": "Fitness",
#         "subcategory": "Strength Training",
#         "price": 299.99,
#         "brand": "IronFit",
#         "rating": 4.7,
#         "description": "Space-saving adjustable dumbbells 5-52.5 lbs",
#         "features": ["15 weight settings", "Space efficient", "Quick adjustment", "Durable"],
#         "tags": ["strength-training", "home-gym", "compact", "versatile"],
#         "stock": 43
#     },
#     {
#         "id": 24,
#         "name": "Foam Roller - High Density",
#         "category": "Fitness",
#         "subcategory": "Recovery",
#         "price": 29.99,
#         "brand": "RecoverPro",
#         "rating": 4.6,
#         "description": "Deep tissue massage roller for recovery",
#         "features": ["High-density foam", "36 inch length", "Textured surface", "Includes guide"],
#         "tags": ["recovery", "massage", "flexibility", "fitness"],
#         "stock": 215
#     },
    
#     # Smart Home
#     {
#         "id": 25,
#         "name": "Smart LED Bulbs (4-Pack)",
#         "category": "Home & Kitchen",
#         "subcategory": "Smart Home",
#         "price": 49.99,
#         "brand": "LightSmart",
#         "rating": 4.5,
#         "description": "WiFi-enabled color-changing LED bulbs",
#         "features": ["16 million colors", "Voice control", "App scheduling", "Energy efficient"],
#         "tags": ["smart-home", "lighting", "automation", "energy-saving"],
#         "stock": 178
#     },
#     {
#         "id": 26,
#         "name": "Smart Thermostat",
#         "category": "Home & Kitchen",
#         "subcategory": "Smart Home",
#         "price": 179.99,
#         "brand": "EcoTemp",
#         "rating": 4.6,
#         "description": "Learn your schedule and save energy",
#         "features": ["Learning algorithm", "Remote control", "Energy reports", "Easy installation"],
#         "tags": ["smart-home", "energy-saving", "automation", "climate-control"],
#         "stock": 91
#     },
    
#     # Gaming
#     {
#         "id": 27,
#         "name": "Gaming Mouse RGB",
#         "category": "Electronics",
#         "subcategory": "Gaming",
#         "price": 79.99,
#         "brand": "GamePro",
#         "rating": 4.6,
#         "description": "High-precision gaming mouse with 16K DPI",
#         "features": ["16000 DPI", "RGB lighting", "8 programmable buttons", "Ergonomic"],
#         "tags": ["gaming", "esports", "rgb", "precision"],
#         "stock": 112
#     },
#     {
#         "id": 28,
#         "name": "Gaming Headset 7.1 Surround",
#         "category": "Electronics",
#         "subcategory": "Gaming",
#         "price": 99.99,
#         "brand": "GamePro",
#         "rating": 4.5,
#         "description": "Immersive gaming audio with noise-cancelling mic",
#         "features": ["7.1 surround sound", "Noise-cancelling mic", "RGB lighting", "50mm drivers"],
#         "tags": ["gaming", "audio", "esports", "immersive"],
#         "stock": 87
#     },
    
#     # More Home Items
#     {
#         "id": 29,
#         "name": "Blender Pro 1500W",
#         "category": "Home & Kitchen",
#         "subcategory": "Appliances",
#         "price": 129.99,
#         "brand": "BlendMaster",
#         "rating": 4.7,
#         "description": "Professional blender for smoothies and more",
#         "features": ["1500W motor", "64oz container", "10 speeds", "Self-cleaning"],
#         "tags": ["cooking", "healthy", "smoothies", "kitchen"],
#         "stock": 98
#     },
#     {
#         "id": 30,
#         "name": "Standing Desk Converter",
#         "category": "Home & Kitchen",
#         "subcategory": "Furniture",
#         "price": 199.99,
#         "brand": "ErgoWork",
#         "rating": 4.5,
#         "description": "Transform any desk into a standing desk",
#         "features": ["Height adjustable", "32 inch width", "Dual tier", "Easy assembly"],
#         "tags": ["ergonomic", "work-from-home", "health", "productivity"],
#         "stock": 72
#     },
#     # More Electronics - Tablets & E-readers
#     {
#         "id": 31,
#         "name": "iPad Air M2",
#         "category": "Electronics",
#         "subcategory": "Tablets",
#         "price": 599.99,
#         "brand": "Apple",
#         "rating": 4.7,
#         "description": "Powerful tablet with M2 chip for creativity",
#         "features": ["M2 chip", "10.9-inch display", "64GB storage", "Apple Pencil support"],
#         "tags": ["tablet", "apple-ecosystem", "creative", "portable"],
#         "stock": 78
#     },
#     {
#         "id": 32,
#         "name": "Samsung Galaxy Tab S9",
#         "category": "Electronics",
#         "subcategory": "Tablets",
#         "price": 799.99,
#         "brand": "Samsung",
#         "rating": 4.6,
#         "description": "Premium Android tablet with S Pen included",
#         "features": ["Snapdragon 8 Gen 2", "11-inch AMOLED", "128GB storage", "S Pen"],
#         "tags": ["android", "tablet", "productivity", "entertainment"],
#         "stock": 64
#     },
#     {
#         "id": 33,
#         "name": "Kindle Paperwhite",
#         "category": "Electronics",
#         "subcategory": "E-readers",
#         "price": 139.99,
#         "brand": "Amazon",
#         "rating": 4.8,
#         "description": "Waterproof e-reader with adjustable warm light",
#         "features": ["6.8-inch display", "Waterproof", "Warm light", "8GB storage"],
#         "tags": ["reading", "e-reader", "portable", "battery-life"],
#         "stock": 143
#     },
    
#     # Smart Watches & Fitness Trackers
#     {
#         "id": 34,
#         "name": "Apple Watch Series 9",
#         "category": "Electronics",
#         "subcategory": "Smartwatches",
#         "price": 429.99,
#         "brand": "Apple",
#         "rating": 4.7,
#         "description": "Advanced health and fitness tracking",
#         "features": ["Always-on display", "ECG", "Blood oxygen", "Crash detection"],
#         "tags": ["fitness-tracking", "health", "apple-ecosystem", "smart-device"],
#         "stock": 92
#     },
#     {
#         "id": 35,
#         "name": "Garmin Forerunner 265",
#         "category": "Electronics",
#         "subcategory": "Fitness Trackers",
#         "price": 449.99,
#         "brand": "Garmin",
#         "rating": 4.8,
#         "description": "Advanced GPS running watch with AMOLED",
#         "features": ["GPS", "Heart rate", "Training metrics", "13-day battery"],
#         "tags": ["running", "fitness-tracking", "gps", "endurance"],
#         "stock": 56
#     },
    
#     # Cameras & Photography
#     {
#         "id": 36,
#         "name": "Sony Alpha a7 IV",
#         "category": "Electronics",
#         "subcategory": "Cameras",
#         "price": 2499.99,
#         "brand": "Sony",
#         "rating": 4.9,
#         "description": "Professional mirrorless camera for hybrid shooting",
#         "features": ["33MP sensor", "4K 60fps", "693 AF points", "5-axis stabilization"],
#         "tags": ["photography", "videography", "professional", "creative"],
#         "stock": 34
#     },
#     {
#         "id": 37,
#         "name": "GoPro HERO 12 Black",
#         "category": "Electronics",
#         "subcategory": "Action Cameras",
#         "price": 399.99,
#         "brand": "GoPro",
#         "rating": 4.7,
#         "description": "Rugged action camera for adventures",
#         "features": ["5.3K video", "Waterproof", "HyperSmooth 6.0", "Voice control"],
#         "tags": ["action-sports", "adventure", "videography", "rugged"],
#         "stock": 87
#     },
    
#     # Audio - Speakers
#     {
#         "id": 38,
#         "name": "Sonos Era 100",
#         "category": "Electronics",
#         "subcategory": "Speakers",
#         "price": 249.99,
#         "brand": "Sonos",
#         "rating": 4.6,
#         "description": "Smart speaker with exceptional sound",
#         "features": ["Spatial audio", "Voice control", "Multi-room", "Bluetooth/WiFi"],
#         "tags": ["audio", "smart-home", "music", "wireless"],
#         "stock": 104
#     },
#     {
#         "id": 39,
#         "name": "JBL Charge 5",
#         "category": "Electronics",
#         "subcategory": "Speakers",
#         "price": 179.99,
#         "brand": "JBL",
#         "rating": 4.8,
#         "description": "Portable Bluetooth speaker with powerbank",
#         "features": ["20hr battery", "Waterproof", "USB charge-out", "PartyBoost"],
#         "tags": ["portable", "outdoor", "audio", "durable"],
#         "stock": 167
#     },
    
#     # More Books - Technical & Business
#     {
#         "id": 40,
#         "name": "Clean Code by Robert Martin",
#         "category": "Books",
#         "subcategory": "Technology",
#         "price": 44.99,
#         "brand": "Prentice Hall",
#         "rating": 4.7,
#         "description": "A handbook of agile software craftsmanship",
#         "features": ["Paperback", "464 pages", "Code examples", "Best practices"],
#         "tags": ["programming", "software-development", "technical", "reference"],
#         "stock": 112
#     },
#     {
#         "id": 41,
#         "name": "Thinking, Fast and Slow",
#         "category": "Books",
#         "subcategory": "Psychology",
#         "price": 17.99,
#         "brand": "Farrar, Straus and Giroux",
#         "rating": 4.6,
#         "description": "Groundbreaking tour of the mind by Nobel Prize winner",
#         "features": ["Paperback", "512 pages", "Research-based", "Bestseller"],
#         "tags": ["psychology", "decision-making", "self-improvement", "science"],
#         "stock": 143
#     },
#     {
#         "id": 42,
#         "name": "Zero to One by Peter Thiel",
#         "category": "Books",
#         "subcategory": "Business",
#         "price": 18.99,
#         "brand": "Crown Business",
#         "rating": 4.5,
#         "description": "Notes on startups and building the future",
#         "features": ["Hardcover", "224 pages", "Startup guide", "Innovation"],
#         "tags": ["business", "entrepreneurship", "startups", "innovation"],
#         "stock": 98
#     },
#     {
#         "id": 43,
#         "name": "The Lean Startup",
#         "category": "Books",
#         "subcategory": "Business",
#         "price": 16.99,
#         "brand": "Crown Business",
#         "rating": 4.6,
#         "description": "How today's entrepreneurs use continuous innovation",
#         "features": ["Paperback", "336 pages", "Methodology", "Case studies"],
#         "tags": ["business", "entrepreneurship", "startups", "agile"],
#         "stock": 127
#     },
#     {
#         "id": 44,
#         "name": "Deep Work by Cal Newport",
#         "category": "Books",
#         "subcategory": "Productivity",
#         "price": 15.99,
#         "brand": "Grand Central Publishing",
#         "rating": 4.7,
#         "description": "Rules for focused success in a distracted world",
#         "features": ["Hardcover", "304 pages", "Strategies", "Practical"],
#         "tags": ["productivity", "focus", "self-improvement", "work"],
#         "stock": 156
#     },
    
#     # More Fitness Equipment
#     {
#         "id": 45,
#         "name": "Peloton Bike+",
#         "category": "Fitness",
#         "subcategory": "Cardio",
#         "price": 2495.00,
#         "brand": "Peloton",
#         "rating": 4.7,
#         "description": "Premium indoor cycling bike with rotating screen",
#         "features": ["Rotating 24-inch screen", "Auto-resistance", "Live classes", "Metrics tracking"],
#         "tags": ["cycling", "cardio", "home-gym", "premium", "interactive"],
#         "stock": 23
#     },
#     {
#         "id": 46,
#         "name": "Treadmill Smart Pro",
#         "category": "Fitness",
#         "subcategory": "Cardio",
#         "price": 1299.99,
#         "brand": "NordicTrack",
#         "rating": 4.5,
#         "description": "Folding treadmill with iFit integration",
#         "features": ["12 MPH max speed", "Foldable", "iFit compatible", "Decline/incline"],
#         "tags": ["running", "cardio", "home-gym", "smart-device"],
#         "stock": 34
#     },
#     {
#         "id": 47,
#         "name": "Kettlebell Set (3-Pack)",
#         "category": "Fitness",
#         "subcategory": "Strength Training",
#         "price": 89.99,
#         "brand": "IronFit",
#         "rating": 4.6,
#         "description": "Cast iron kettlebells 15, 25, 35 lbs",
#         "features": ["Cast iron", "Wide handle", "Flat base", "Workout guide"],
#         "tags": ["strength-training", "functional-fitness", "home-gym", "versatile"],
#         "stock": 78
#     },
#     {
#         "id": 48,
#         "name": "Protein Powder - Whey Isolate",
#         "category": "Fitness",
#         "subcategory": "Supplements",
#         "price": 49.99,
#         "brand": "Optimum Nutrition",
#         "rating": 4.8,
#         "description": "Gold Standard 100% Whey protein 5lb",
#         "features": ["24g protein", "5.5g BCAAs", "Low sugar", "Chocolate flavor"],
#         "tags": ["nutrition", "protein", "supplements", "fitness"],
#         "stock": 234
#     },
    
#     # Home Office & Productivity
#     {
#         "id": 49,
#         "name": "Ergonomic Office Chair",
#         "category": "Home & Kitchen",
#         "subcategory": "Furniture",
#         "price": 349.99,
#         "brand": "Herman Miller",
#         "rating": 4.8,
#         "description": "Premium mesh office chair with lumbar support",
#         "features": ["Adjustable lumbar", "Breathable mesh", "Tilt limiter", "12-year warranty"],
#         "tags": ["ergonomic", "office", "work-from-home", "comfort"],
#         "stock": 45
#     },
#     {
#         "id": 50,
#         "name": "Monitor Arm Dual Mount",
#         "category": "Home & Kitchen",
#         "subcategory": "Accessories",
#         "price": 129.99,
#         "brand": "ErgoWork",
#         "rating": 4.6,
#         "description": "Adjustable dual monitor arm stand",
#         "features": ["Holds 2 monitors", "VESA compatible", "Cable management", "Gas spring"],
#         "tags": ["productivity", "ergonomic", "desk-setup", "organization"],
#         "stock": 89
#     },
#     {
#         "id": 51,
#         "name": "Desk Lamp LED Smart",
#         "category": "Home & Kitchen",
#         "subcategory": "Lighting",
#         "price": 79.99,
#         "brand": "LightPro",
#         "rating": 4.5,
#         "description": "Smart desk lamp with wireless charging",
#         "features": ["Eye-care LED", "Wireless charging pad", "Touch control", "Auto-dimming"],
#         "tags": ["lighting", "smart-device", "productivity", "desk-setup"],
#         "stock": 134
#     },
    
#     # Gaming Accessories
#     {
#         "id": 52,
#         "name": "Gaming Chair RGB",
#         "category": "Home & Kitchen",
#         "subcategory": "Gaming Furniture",
#         "price": 299.99,
#         "brand": "GamePro",
#         "rating": 4.5,
#         "description": "Racing-style gaming chair with RGB lighting",
#         "features": ["RGB lighting", "Lumbar pillow", "Reclining", "PU leather"],
#         "tags": ["gaming", "comfort", "rgb", "ergonomic"],
#         "stock": 67
#     },
#     {
#         "id": 53,
#         "name": "Gaming Monitor 27\" 165Hz",
#         "category": "Electronics",
#         "subcategory": "Monitors",
#         "price": 329.99,
#         "brand": "ASUS",
#         "rating": 4.7,
#         "description": "Fast refresh rate monitor for competitive gaming",
#         "features": ["165Hz refresh", "1ms response", "QHD resolution", "G-Sync compatible"],
#         "tags": ["gaming", "monitor", "high-refresh", "competitive"],
#         "stock": 56
#     },
#     {
#         "id": 54,
#         "name": "Streaming Microphone USB",
#         "category": "Electronics",
#         "subcategory": "Audio",
#         "price": 129.99,
#         "brand": "Blue Yeti",
#         "rating": 4.8,
#         "description": "Professional USB microphone for streaming",
#         "features": ["4 polar patterns", "Mute button", "Gain control", "Zero-latency monitoring"],
#         "tags": ["streaming", "content-creation", "audio", "podcasting"],
#         "stock": 103
#     },
    
#     # Kitchen Appliances
#     {
#         "id": 55,
#         "name": "Instant Pot Duo 8-Quart",
#         "category": "Home & Kitchen",
#         "subcategory": "Appliances",
#         "price": 119.99,
#         "brand": "Instant Pot",
#         "rating": 4.8,
#         "description": "7-in-1 electric pressure cooker",
#         "features": ["8-quart capacity", "7 functions", "Programmable", "Stainless steel"],
#         "tags": ["cooking", "pressure-cooker", "convenient", "multi-function"],
#         "stock": 156
#     },
#     {
#         "id": 56,
#         "name": "KitchenAid Stand Mixer",
#         "category": "Home & Kitchen",
#         "subcategory": "Appliances",
#         "price": 379.99,
#         "brand": "KitchenAid",
#         "rating": 4.9,
#         "description": "Professional 5-quart stand mixer",
#         "features": ["5-quart bowl", "10 speeds", "Tilt-head design", "Multiple attachments"],
#         "tags": ["baking", "cooking", "premium", "kitchen"],
#         "stock": 67
#     },
#     {
#         "id": 57,
#         "name": "Nespresso Machine",
#         "category": "Home & Kitchen",
#         "subcategory": "Coffee Makers",
#         "price": 199.99,
#         "brand": "Nespresso",
#         "rating": 4.7,
#         "description": "Original line espresso and coffee maker",
#         "features": ["19-bar pressure", "Fast heat-up", "Auto shut-off", "Compact design"],
#         "tags": ["coffee", "espresso", "convenient", "compact"],
#         "stock": 98
#     },
    
#     # Smart Home Devices
#     {
#         "id": 58,
#         "name": "Smart Doorbell Camera",
#         "category": "Home & Kitchen",
#         "subcategory": "Smart Home",
#         "price": 249.99,
#         "brand": "Ring",
#         "rating": 4.6,
#         "description": "Video doorbell with motion detection",
#         "features": ["1080p HD video", "Two-way talk", "Motion alerts", "Night vision"],
#         "tags": ["smart-home", "security", "video", "convenience"],
#         "stock": 123
#     },
#     {
#         "id": 59,
#         "name": "Smart Lock Keyless Entry",
#         "category": "Home & Kitchen",
#         "subcategory": "Smart Home",
#         "price": 199.99,
#         "brand": "August",
#         "rating": 4.5,
#         "description": "Retrofit smart lock with app control",
#         "features": ["Smartphone control", "Auto-lock/unlock", "Voice assistant", "Guest access"],
#         "tags": ["smart-home", "security", "keyless", "automation"],
#         "stock": 87
#     },
#     {
#         "id": 60,
#         "name": "Smart Display 10-inch",
#         "category": "Electronics",
#         "subcategory": "Smart Home",
#         "price": 229.99,
#         "brand": "Google",
#         "rating": 4.6,
#         "description": "Smart display with Google Assistant",
#         "features": ["10-inch touchscreen", "Video calls", "Smart home control", "YouTube/Netflix"],
#         "tags": ["smart-home", "voice-assistant", "entertainment", "video-calls"],
#         "stock": 76
#     },
    
#     # Fashion & Accessories
#     {
#         "id": 61,
#         "name": "Backpack Laptop 17-inch",
#         "category": "Fashion",
#         "subcategory": "Bags",
#         "price": 89.99,
#         "brand": "SwissGear",
#         "rating": 4.7,
#         "description": "Travel-friendly laptop backpack",
#         "features": ["17-inch laptop compartment", "USB charging port", "Water-resistant", "Padded straps"],
#         "tags": ["travel", "work", "laptop", "durable"],
#         "stock": 145
#     },
#     {
#         "id": 62,
#         "name": "Sunglasses Polarized",
#         "category": "Fashion",
#         "subcategory": "Accessories",
#         "price": 149.99,
#         "brand": "Ray-Ban",
#         "rating": 4.8,
#         "description": "Classic polarized sunglasses",
#         "features": ["Polarized lenses", "UV protection", "Durable frame", "Case included"],
#         "tags": ["fashion", "outdoor", "eyewear", "premium"],
#         "stock": 187
#     },
#     {
#         "id": 63,
#         "name": "Wireless Charging Stand",
#         "category": "Electronics",
#         "subcategory": "Accessories",
#         "price": 39.99,
#         "brand": "Anker",
#         "rating": 4.6,
#         "description": "Fast wireless charger with stand",
#         "features": ["15W fast charging", "Multi-device", "LED indicator", "Case-friendly"],
#         "tags": ["charging", "wireless", "desk-setup", "convenient"],
#         "stock": 234
#     },
    
#     # Outdoor & Sports
#     {
#         "id": 64,
#         "name": "Camping Tent 4-Person",
#         "category": "Sports & Outdoors",
#         "subcategory": "Camping",
#         "price": 199.99,
#         "brand": "Coleman",
#         "rating": 4.6,
#         "description": "Weatherproof camping tent",
#         "features": ["4-person capacity", "Waterproof", "Easy setup", "Storage pockets"],
#         "tags": ["camping", "outdoor", "adventure", "travel"],
#         "stock": 67
#     },
#     {
#         "id": 65,
#         "name": "Hydration Backpack",
#         "category": "Sports & Outdoors",
#         "subcategory": "Hiking",
#         "price": 79.99,
#         "brand": "CamelBak",
#         "rating": 4.7,
#         "description": "Hydration pack for hiking and biking",
#         "features": ["3L reservoir", "Insulated tube", "Lightweight", "Multiple compartments"],
#         "tags": ["hiking", "outdoor", "hydration", "adventure"],
#         "stock": 112
#     },
#     {
#         "id": 66,
#         "name": "Mountain Bike 29-inch",
#         "category": "Sports & Outdoors",
#         "subcategory": "Cycling",
#         "price": 899.99,
#         "brand": "Trek",
#         "rating": 4.7,
#         "description": "Hardtail mountain bike for trails",
#         "features": ["29-inch wheels", "21-speed", "Front suspension", "Disc brakes"],
#         "tags": ["cycling", "mountain-biking", "outdoor", "exercise"],
#         "stock": 34
#     },
# ]

# # Extended user personas - 10 total users
# EXTENDED_USERS = [
#     {
#         "id": 1,
#         "name": "Alex Chen",
#         "age": 28,
#         "persona": "Tech Enthusiast & Developer",
#         "interests": ["programming", "gaming", "tech", "productivity", "software-development"],
#         "price_sensitivity": "medium",
#         "preferred_brands": ["Apple", "Dell", "Sony", "ASUS"],
#         "budget_range": [500, 2500]
#     },
#     {
#         "id": 2,
#         "name": "Sarah Martinez",
#         "persona": "Fitness & Wellness",
#         "age": 32,
#         "interests": ["fitness", "health", "yoga", "self-improvement", "nutrition"],
#         "price_sensitivity": "low",
#         "preferred_brands": ["FitLife", "RecoverPro", "Peloton", "Optimum Nutrition"],
#         "budget_range": [20, 500]
#     },
#     {
#         "id": 3,
#         "name": "Mike Johnson",
#         "persona": "Budget-Conscious Student",
#         "age": 22,
#         "interests": ["books", "study", "affordable-tech", "gaming", "learning"],
#         "price_sensitivity": "high",
#         "preferred_brands": ["Google", "ASUS", "Anker"],
#         "budget_range": [10, 800]
#     },
#     {
#         "id": 4,
#         "name": "Emily Davis",
#         "persona": "Home & Lifestyle Enthusiast",
#         "age": 35,
#         "interests": ["cooking", "smart-home", "organization", "reading", "baking"],
#         "price_sensitivity": "medium",
#         "preferred_brands": ["BrewMaster", "CleanBot", "KitchenAid", "Instant Pot"],
#         "budget_range": [30, 400]
#     },
#     {
#         "id": 5,
#         "name": "James Wilson",
#         "persona": "Professional Gamer & Streamer",
#         "age": 24,
#         "interests": ["gaming", "esports", "streaming", "high-performance", "content-creation"],
#         "price_sensitivity": "low",
#         "preferred_brands": ["ASUS", "GamePro", "Sony", "Blue Yeti"],
#         "budget_range": [100, 2500]
#     },
#     {
#         "id": 6,
#         "name": "Lisa Park",
#         "persona": "Remote Worker & Freelancer",
#         "age": 29,
#         "interests": ["work-from-home", "productivity", "ergonomic", "video-calls", "focus"],
#         "price_sensitivity": "medium",
#         "preferred_brands": ["Dell", "VidStream", "ErgoWork", "Herman Miller"],
#         "budget_range": [50, 1500]
#     },
#     {
#         "id": 7,
#         "name": "David Kumar",
#         "persona": "Photography Enthusiast",
#         "age": 31,
#         "interests": ["photography", "videography", "creative", "travel", "adventure"],
#         "price_sensitivity": "medium",
#         "preferred_brands": ["Sony", "GoPro", "Canon"],
#         "budget_range": [200, 3000]
#     },
#     {
#         "id": 8,
#         "name": "Jennifer Lopez",
#         "persona": "Entrepreneur & Business Owner",
#         "age": 38,
#         "interests": ["business", "entrepreneurship", "productivity", "self-improvement", "innovation"],
#         "price_sensitivity": "low",
#         "preferred_brands": ["Apple", "Herman Miller", "Sony"],
#         "budget_range": [100, 3000]
#     },
#     {
#         "id": 9,
#         "name": "Tom Anderson",
#         "persona": "Outdoor Adventure Seeker",
#         "age": 27,
#         "interests": ["outdoor", "camping", "hiking", "adventure", "fitness"],
#         "price_sensitivity": "medium",
#         "preferred_brands": ["Coleman", "CamelBak", "GoPro", "Garmin"],
#         "budget_range": [50, 1000]
#     },
#     {
#         "id": 10,
#         "name": "Rachel Green",
#         "persona": "Book Lover & Lifelong Learner",
#         "age": 26,
#         "interests": ["reading", "learning", "self-improvement", "psychology", "literature"],
#         "price_sensitivity": "medium",
#         "preferred_brands": ["Amazon", "Penguin Random House", "O'Reilly"],
#         "budget_range": [10, 300]
#     }
# ]

# def generate_interactions(num_interactions=400):
#     """Generate realistic user interactions with extended products"""
#     interactions = []
#     interaction_types = ["view", "click", "add_to_cart", "purchase", "like", "dislike"]
    
#     for i in range(num_interactions):
#         user = random.choice(EXTENDED_USERS)
        
#         # Users are more likely to interact with products matching their interests
#         matching_products = [
#             p for p in EXTENDED_PRODUCTS 
#             if any(interest in p["tags"] for interest in user["interests"])
#         ]
        
#         # 75% chance to interact with matching products, 25% random exploration
#         if matching_products and random.random() < 0.75:
#             product = random.choice(matching_products)
#         else:
#             product = random.choice(EXTENDED_PRODUCTS)
        
#         # Price sensitivity affects purchase behavior
#         if product["price"] > user["budget_range"][1]:
#             interaction_type = random.choice(["view", "click"])  # Only browse expensive items
#         elif product["price"] < user["budget_range"][0]:
#             # Unlikely to interact with items too cheap for persona
#             if random.random() < 0.3:
#                 interaction_type = "view"
#             else:
#                 continue
#         else:
#             # Weight interaction types realistically
#             weights = [40, 25, 15, 12, 6, 2]  # view most common, dislike rare
#             interaction_type = random.choices(interaction_types, weights=weights)[0]
        
#         # Generate timestamp within last 60 days
#         days_ago = random.randint(0, 60)
#         hours_ago = random.randint(0, 23)
#         minutes_ago = random.randint(0, 59)
#         timestamp = datetime.now() - timedelta(days=days_ago, hours=hours_ago, minutes=minutes_ago)
        
#         interactions.append({
#             "id": i + 1,
#             "user_id": user["id"],
#             "product_id": product["id"],
#             "interaction_type": interaction_type,
#             "timestamp": timestamp.isoformat(),
#             "session_duration_seconds": random.randint(15, 900) if interaction_type == "view" else None,
#             "device": random.choice(["desktop", "mobile", "tablet"])
#         })
    
#     # Sort by timestamp
#     interactions.sort(key=lambda x: x["timestamp"])
#     return interactions

# def save_extended_data():
#     """Save all extended data to JSON files"""
    
#     # Save products
#     with open("products_extended.json", "w") as f:
#         json.dump(EXTENDED_PRODUCTS, f, indent=2)
#     print(f"✅ Saved {len(EXTENDED_PRODUCTS)} products to products_extended.json")
    
#     # Save users
#     with open("users_extended.json", "w") as f:
#         json.dump(EXTENDED_USERS, f, indent=2)
#     print(f"✅ Saved {len(EXTENDED_USERS)} users to users_extended.json")
    
#     # Generate and save interactions
#     interactions = generate_interactions(400)
#     with open("interactions_extended.json", "w") as f:
#         json.dump(interactions, f, indent=2)
#     print(f"✅ Saved {len(interactions)} interactions to interactions_extended.json")
    
#     # Create detailed summary
#     summary = {
#         "total_products": len(EXTENDED_PRODUCTS),
#         "total_users": len(EXTENDED_USERS),
#         "total_interactions": len(interactions),
#         "categories": {},
#         "interaction_breakdown": {},
#         "price_statistics": {
#             "min": min(p["price"] for p in EXTENDED_PRODUCTS),
#             "max": max(p["price"] for p in EXTENDED_PRODUCTS),
#             "average": sum(p["price"] for p in EXTENDED_PRODUCTS) / len(EXTENDED_PRODUCTS)
#         },
#         "user_personas": [u["persona"] for u in EXTENDED_USERS]
#     }
    
#     # Count products per category
#     for product in EXTENDED_PRODUCTS:
#         cat = product["category"]
#         summary["categories"][cat] = summary["categories"].get(cat, 0) + 1
    
#     # Count interactions by type
#     for interaction in interactions:
#         itype = interaction["interaction_type"]
#         summary["interaction_breakdown"][itype] = summary["interaction_breakdown"].get(itype, 0) + 1
    
#     with open("data_summary_extended.json", "w") as f:
#         json.dump(summary, f, indent=2)
#     print(f"✅ Saved extended summary to data_summary_extended.json")
    
#     print("\n📊 Extended Data Summary:")
#     print(f"  - Total Products: {summary['total_products']}")
#     print(f"  - Categories: {list(summary['categories'].keys())}")
#     print(f"  - Products per Category:")
#     for cat, count in summary['categories'].items():
#         print(f"      • {cat}: {count}")
#     print(f"  - Total Users: {summary['total_users']}")
#     print(f"  - User Personas: {len(summary['user_personas'])}")
#     print(f"  - Total Interactions: {summary['total_interactions']}")
#     print(f"  - Interaction Types: {summary['interaction_breakdown']}")
#     print(f"  - Price Range: ${summary['price_statistics']['min']:.2f} - ${summary['price_statistics']['max']:.2f}")
#     print(f"  - Average Price: ${summary['price_statistics']['average']:.2f}")

# if __name__ == "__main__":
#     print("🚀 Generating Extended E-commerce Sample Data...\n")
#     save_extended_data()
#     print("\n✨ Extended data generation complete!")
#     print("\nFiles created:")
#     print("  - products_extended.json (66 products)")
#     print("  - users_extended.json (10 user personas)")
#     print("  - interactions_extended.json (400+ interactions)")
#     print("  - data_summary_extended.json (detailed overview)")

"""
Large-Scale E-commerce Data Generator using Faker
Generates 100-150 users, 1700-2000 products, and realistic interactions
"""
import json
import random
from datetime import datetime, timedelta
from faker import Faker

# Initialize Faker
fake = Faker()
Faker.seed(42)  # For reproducibility
random.seed(42)

# Configuration
NUM_USERS = 150
NUM_PRODUCTS = 1800
NUM_INTERACTIONS = 5000

# Product Categories and Subcategories
CATEGORIES = {
    "Electronics": {
        "subcategories": ["Laptops", "Smartphones", "Tablets", "Cameras", "Headphones", 
                         "Speakers", "Smartwatches", "Gaming", "Accessories", "Monitors"],
        "price_range": (50, 3000),
        "brands": ["Apple", "Samsung", "Dell", "Sony", "Asus", "HP", "Lenovo", "LG", "Microsoft", "Google"]
    },
    "Books": {
        "subcategories": ["Technology", "Business", "Self-Help", "Fiction", "Science", 
                         "History", "Biography", "Psychology", "Philosophy", "Education"],
        "price_range": (10, 80),
        "brands": ["Penguin", "O'Reilly", "Wiley", "McGraw-Hill", "Pearson", "HarperCollins", 
                  "Random House", "Simon & Schuster", "Hachette", "Macmillan"]
    },
    "Fitness": {
        "subcategories": ["Yoga", "Cardio", "Strength Training", "Wearables", "Supplements", 
                         "Recovery", "Sports Equipment", "Clothing"],
        "price_range": (15, 500),
        "brands": ["Nike", "Adidas", "Peloton", "Garmin", "Fitbit", "Under Armour", 
                  "Lululemon", "Reebok", "NordicTrack", "Bowflex"]
    },
    "Home & Kitchen": {
        "subcategories": ["Appliances", "Furniture", "Smart Home", "Cookware", "Decor", 
                         "Lighting", "Storage", "Bedding"],
        "price_range": (20, 800),
        "brands": ["KitchenAid", "Cuisinart", "Dyson", "iRobot", "Philips", "Breville", 
                  "Instant Pot", "Ninja", "Hamilton Beach", "Black+Decker"]
    },
    "Fashion": {
        "subcategories": ["Men's Clothing", "Women's Clothing", "Shoes", "Accessories", 
                         "Bags", "Watches", "Jewelry", "Sunglasses"],
        "price_range": (25, 500),
        "brands": ["Nike", "Adidas", "Levi's", "Calvin Klein", "Tommy Hilfiger", "Ralph Lauren", 
                  "H&M", "Zara", "Uniqlo", "Gap"]
    },
    "Sports & Outdoors": {
        "subcategories": ["Camping", "Hiking", "Cycling", "Fishing", "Water Sports", 
                         "Winter Sports", "Team Sports", "Golf"],
        "price_range": (30, 1000),
        "brands": ["Coleman", "The North Face", "Patagonia", "REI", "Trek", "Specialized", 
                  "Osprey", "CamelBak", "Garmin", "GoPro"]
    },
    "Beauty & Personal Care": {
        "subcategories": ["Skincare", "Haircare", "Makeup", "Fragrances", "Tools", 
                         "Men's Grooming", "Oral Care", "Bath & Body"],
        "price_range": (10, 200),
        "brands": ["L'Oréal", "Neutrogena", "Olay", "Dove", "Gillette", "Philips", 
                  "Oral-B", "Maybelline", "Revlon", "CeraVe"]
    },
    "Toys & Games": {
        "subcategories": ["Action Figures", "Board Games", "Puzzles", "Educational", 
                         "Video Games", "Outdoor Toys", "Dolls", "Building Sets"],
        "price_range": (15, 300),
        "brands": ["Lego", "Hasbro", "Mattel", "Nintendo", "PlayStation", "Xbox", 
                  "Ravensburger", "Melissa & Doug", "Fisher-Price", "VTech"]
    }
}

# User Personas (expanded)
PERSONAS = [
    "Tech Enthusiast", "Budget Shopper", "Fitness Fanatic", "Book Lover", "Gamer",
    "Home Chef", "Fashion Forward", "Outdoor Adventurer", "Professional", "Student",
    "Parent", "Senior Citizen", "Minimalist", "Luxury Buyer", "Eco-Conscious",
    "DIY Enthusiast", "Photographer", "Musician", "Artist", "Traveler"
]

# Interest Tags
INTEREST_TAGS = [
    "technology", "programming", "gaming", "fitness", "yoga", "running", "reading",
    "cooking", "baking", "fashion", "travel", "photography", "music", "art",
    "outdoor", "camping", "hiking", "sports", "health", "wellness", "beauty",
    "productivity", "learning", "education", "business", "finance", "investing",
    "home-improvement", "gardening", "sustainability", "minimalism", "luxury",
    "entertainment", "movies", "tv-shows", "podcasts", "social-media"
]

def generate_product_name(category, subcategory, brand):
    """Generate realistic product name"""
    
    descriptors = {
        "Electronics": ["Smart", "Wireless", "Pro", "Ultra", "Premium", "Advanced", "Elite"],
        "Books": ["Complete Guide to", "Mastering", "Art of", "Science of", "Practical"],
        "Fitness": ["Pro", "Elite", "Advanced", "Essential", "Ultimate", "Premium"],
        "Home & Kitchen": ["Smart", "Digital", "Professional", "Deluxe", "Modern"],
        "Fashion": ["Classic", "Modern", "Essential", "Premium", "Signature"],
        "Sports & Outdoors": ["Pro", "Adventure", "Expedition", "Trail", "Summit"],
        "Beauty & Personal Care": ["Advanced", "Professional", "Radiance", "Ultimate"],
        "Toys & Games": ["Ultimate", "Deluxe", "Creative", "Educational", "Interactive"]
    }
    
    desc = random.choice(descriptors.get(category, ["Professional"]))
    
    # Generate specific product types
    product_types = {
        "Laptops": ["Laptop", "Notebook", "Ultrabook", "Chromebook"],
        "Smartphones": ["Phone", "Smartphone", "Mobile"],
        "Tablets": ["Tablet", "iPad", "Tab"],
        "Cameras": ["Camera", "DSLR", "Mirrorless Camera"],
        "Headphones": ["Headphones", "Earbuds", "Headset"],
        "Speakers": ["Speaker", "Soundbar", "Bluetooth Speaker"],
        "Yoga": ["Yoga Mat", "Yoga Block", "Yoga Wheel"],
        "Cookware": ["Pan Set", "Pot Set", "Skillet", "Dutch Oven"],
        "Board Games": ["Board Game", "Strategy Game", "Party Game"],
    }
    
    ptype = random.choice(product_types.get(subcategory, [subcategory]))
    
    # Add model/version numbers for some products
    if category == "Electronics":
        model = random.choice(["", f" {random.randint(5, 15)}", " Pro", " Air", " Max"])
        return f"{brand} {desc} {ptype}{model}"
    else:
        return f"{brand} {desc} {ptype}"

def generate_product_description(category, subcategory, name):
    """Generate product description"""
    templates = [
        f"Premium quality {subcategory.lower()} designed for optimal performance and durability.",
        f"Experience excellence with this top-rated {subcategory.lower()} featuring cutting-edge technology.",
        f"Perfect for both beginners and professionals, this {subcategory.lower()} delivers outstanding results.",
        f"Enhance your {category.lower()} collection with this highly-rated product.",
        f"Trusted by thousands, this {subcategory.lower()} combines quality with affordability.",
    ]
    return random.choice(templates)

def generate_product_features(category, subcategory):
    """Generate realistic product features"""
    
    common_features = {
        "Electronics": [
            f"{random.choice([512, 1024, 2048])}GB storage",
            f"{random.choice([8, 16, 32, 64])}GB RAM",
            f"{random.choice(['Intel i7', 'Intel i9', 'AMD Ryzen', 'Apple M2'])} processor",
            "High-resolution display",
            "Long battery life",
            "Wireless connectivity",
            "Fast charging",
            "Premium build quality"
        ],
        "Books": [
            f"{random.randint(200, 800)} pages",
            "Bestseller",
            "Illustrated edition",
            "Updated content",
            "Expert author",
            "Practical examples"
        ],
        "Fitness": [
            "Durable construction",
            "Ergonomic design",
            "Easy to clean",
            "Portable",
            "Multi-functional",
            "Professional grade"
        ],
        "Home & Kitchen": [
            "Energy efficient",
            "Easy to use",
            "Dishwasher safe",
            "Compact design",
            "Durable materials",
            "Safety features"
        ],
        "Fashion": [
            "Premium materials",
            "Comfortable fit",
            "Stylish design",
            "Versatile",
            "Machine washable",
            "Available in multiple colors"
        ],
        "Sports & Outdoors": [
            "Weather-resistant",
            "Lightweight",
            "Durable construction",
            "Easy setup",
            "Portable",
            "Safety tested"
        ],
        "Beauty & Personal Care": [
            "Dermatologist tested",
            "Hypoallergenic",
            "Natural ingredients",
            "Cruelty-free",
            "Long-lasting",
            "Easy application"
        ],
        "Toys & Games": [
            "Age-appropriate",
            "Educational",
            "Safe materials",
            "Interactive",
            "Durable",
            "Award-winning"
        ]
    }
    
    features = common_features.get(category, ["High quality", "Great value", "Highly rated"])
    return random.sample(features, min(4, len(features)))

def generate_product_tags(category, subcategory):
    """Generate relevant tags for product"""
    
    category_tags = {
        "Electronics": ["tech", "gadget", "wireless", "smart", "digital", "portable"],
        "Books": ["reading", "learning", "education", "knowledge", "reference"],
        "Fitness": ["exercise", "health", "workout", "training", "wellness"],
        "Home & Kitchen": ["home", "kitchen", "cooking", "appliance", "smart-home"],
        "Fashion": ["style", "clothing", "accessory", "trendy", "comfortable"],
        "Sports & Outdoors": ["outdoor", "adventure", "sports", "active", "camping"],
        "Beauty & Personal Care": ["beauty", "skincare", "grooming", "self-care"],
        "Toys & Games": ["fun", "entertainment", "family", "kids", "educational"]
    }
    
    base_tags = category_tags.get(category, ["product"])
    subcategory_tag = subcategory.lower().replace(" ", "-")
    
    all_tags = base_tags + [subcategory_tag, category.lower()]
    return random.sample(all_tags, min(5, len(all_tags)))

def generate_products(num_products):
    """Generate realistic product catalog"""
    print(f"🏭 Generating {num_products} products...")
    
    products = []
    product_id = 1
    
    # Calculate products per category
    products_per_category = num_products // len(CATEGORIES)
    
    for category, config in CATEGORIES.items():
        subcategories = config["subcategories"]
        price_min, price_max = config["price_range"]
        brands = config["brands"]
        
        products_per_sub = products_per_category // len(subcategories)
        
        for subcategory in subcategories:
            for _ in range(products_per_sub):
                brand = random.choice(brands)
                name = generate_product_name(category, subcategory, brand)
                
                # Generate price with some variation
                base_price = random.uniform(price_min, price_max)
                price = round(base_price * random.uniform(0.8, 1.2), 2)
                
                # Generate rating (skewed towards higher ratings)
                rating = round(random.triangular(3.5, 5.0, 4.5), 1)
                
                product = {
                    "id": product_id,
                    "name": name,
                    "category": category,
                    "subcategory": subcategory,
                    "price": price,
                    "brand": brand,
                    "rating": rating,
                    "description": generate_product_description(category, subcategory, name),
                    "features": generate_product_features(category, subcategory),
                    "tags": generate_product_tags(category, subcategory),
                    "stock": random.randint(0, 500)
                }
                
                products.append(product)
                product_id += 1
    
    print(f"✅ Generated {len(products)} products across {len(CATEGORIES)} categories")
    return products

def generate_users(num_users):
    """Generate realistic user profiles using Faker"""
    print(f"👥 Generating {num_users} users...")
    
    users = []
    
    for user_id in range(1, num_users + 1):
        # Generate basic info
        gender = random.choice(['male', 'female'])
        first_name = fake.first_name_male() if gender == 'male' else fake.first_name_female()
        last_name = fake.last_name()
        name = f"{first_name} {last_name}"
        
        # Age distribution (realistic)
        age = random.choices(
            [random.randint(18, 25), random.randint(26, 35), random.randint(36, 50), random.randint(51, 70)],
            weights=[25, 40, 25, 10]
        )[0]
        
        # Select persona based on age and interests
        persona = random.choice(PERSONAS)
        
        # Generate interests (3-7 interests per user)
        num_interests = random.randint(3, 7)
        interests = random.sample(INTEREST_TAGS, num_interests)
        
        # Price sensitivity based on persona and age
        if persona in ["Luxury Buyer", "Professional"]:
            price_sensitivity = "low"
            budget_min = random.randint(50, 200)
            budget_max = random.randint(1000, 5000)
        elif persona in ["Budget Shopper", "Student"]:
            price_sensitivity = "high"
            budget_min = random.randint(10, 50)
            budget_max = random.randint(100, 500)
        else:
            price_sensitivity = "medium"
            budget_min = random.randint(30, 100)
            budget_max = random.randint(300, 2000)
        
        # Preferred brands (2-5 brands)
        all_brands = []
        for config in CATEGORIES.values():
            all_brands.extend(config["brands"])
        preferred_brands = random.sample(list(set(all_brands)), random.randint(2, 5))
        
        user = {
            "id": user_id,
            "name": name,
            "age": age,
            "persona": persona,
            "interests": interests,
            "price_sensitivity": price_sensitivity,
            "preferred_brands": preferred_brands,
            "budget_range": [budget_min, budget_max]
        }
        
        users.append(user)
    
    print(f"✅ Generated {len(users)} users with diverse personas")
    return users

def generate_interactions(users, products, num_interactions):
    """Generate realistic user-product interactions"""
    print(f"🔄 Generating {num_interactions} interactions...")
    
    interactions = []
    interaction_types = ["view", "click", "add_to_cart", "purchase", "like", "dislike", "review"]
    
    # Interaction probabilities (more views, fewer purchases)
    type_weights = [40, 25, 15, 8, 7, 3, 2]
    
    for interaction_id in range(1, num_interactions + 1):
        user = random.choice(users)
        
        # 70% chance to interact with products matching interests
        user_interest_products = [
            p for p in products
            if any(interest in p["tags"] or interest in p["category"].lower() 
                   for interest in user["interests"])
        ]
        
        if user_interest_products and random.random() < 0.7:
            product = random.choice(user_interest_products)
        else:
            product = random.choice(products)
        
        # Check budget constraint for purchases
        interaction_type = random.choices(interaction_types, weights=type_weights)[0]
        
        if product["price"] > user["budget_range"][1]:
            # Only browse if too expensive
            interaction_type = random.choice(["view", "click"])
        
        # Generate timestamp (last 90 days)
        days_ago = random.randint(0, 90)
        hours_ago = random.randint(0, 23)
        minutes_ago = random.randint(0, 59)
        timestamp = datetime.now() - timedelta(days=days_ago, hours=hours_ago, minutes=minutes_ago)
        
        # Session duration for views
        session_duration = None
        if interaction_type == "view":
            session_duration = random.randint(10, 600)
        
        # Device distribution
        device = random.choices(
            ["desktop", "mobile", "tablet"],
            weights=[45, 45, 10]
        )[0]
        
        interaction = {
            "id": interaction_id,
            "user_id": user["id"],
            "product_id": product["id"],
            "interaction_type": interaction_type,
            "timestamp": timestamp.isoformat(),
            "session_duration_seconds": session_duration,
            "device": device
        }
        
        interactions.append(interaction)
    
    # Sort by timestamp
    interactions.sort(key=lambda x: x["timestamp"])
    
    print(f"✅ Generated {len(interactions)} interactions")
    return interactions

def generate_summary(products, users, interactions):
    """Generate dataset summary statistics"""
    
    # Category breakdown
    category_counts = {}
    for product in products:
        cat = product["category"]
        category_counts[cat] = category_counts.get(cat, 0) + 1
    
    # Interaction breakdown
    interaction_counts = {}
    for interaction in interactions:
        itype = interaction["interaction_type"]
        interaction_counts[itype] = interaction_counts.get(itype, 0) + 1
    
    # Price statistics
    prices = [p["price"] for p in products]
    
    # Persona breakdown
    persona_counts = {}
    for user in users:
        persona = user["persona"]
        persona_counts[persona] = persona_counts.get(persona, 0) + 1
    
    summary = {
        "dataset_info": {
            "total_users": len(users),
            "total_products": len(products),
            "total_interactions": len(interactions),
            "generation_date": datetime.now().isoformat()
        },
        "products": {
            "by_category": category_counts,
            "price_stats": {
                "min": min(prices),
                "max": max(prices),
                "average": sum(prices) / len(prices),
                "median": sorted(prices)[len(prices) // 2]
            }
        },
        "users": {
            "by_persona": persona_counts,
            "age_range": {
                "min": min(u["age"] for u in users),
                "max": max(u["age"] for u in users),
                "average": sum(u["age"] for u in users) / len(users)
            }
        },
        "interactions": {
            "by_type": interaction_counts,
            "time_span_days": 90
        }
    }
    
    return summary

def save_data(products, users, interactions):
    """Save all data to JSON files"""
    
    print("\n💾 Saving data to files...")
    
    # Save products
    with open("products_large.json", "w") as f:
        json.dump(products, f, indent=2)
    print(f"✅ Saved {len(products)} products to products_large.json")
    
    # Save users
    with open("users_large.json", "w") as f:
        json.dump(users, f, indent=2)
    print(f"✅ Saved {len(users)} users to users_large.json")
    
    # Save interactions
    with open("interactions_large.json", "w") as f:
        json.dump(interactions, f, indent=2)
    print(f"✅ Saved {len(interactions)} interactions to interactions_large.json")
    
    # Generate and save summary
    summary = generate_summary(products, users, interactions)
    with open("data_summary_large.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(f"✅ Saved summary to data_summary_large.json")
    
    # Print summary
    print("\n📊 Dataset Summary:")
    print(f"  - Users: {summary['dataset_info']['total_users']}")
    print(f"  - Products: {summary['dataset_info']['total_products']}")
    print(f"  - Interactions: {summary['dataset_info']['total_interactions']}")
    print(f"\n  Product Categories:")
    for cat, count in summary['products']['by_category'].items():
        print(f"    • {cat}: {count}")
    print(f"\n  Price Range: ${summary['products']['price_stats']['min']:.2f} - ${summary['products']['price_stats']['max']:.2f}")
    print(f"  Average Price: ${summary['products']['price_stats']['average']:.2f}")
    print(f"\n  Interaction Types:")
    for itype, count in summary['interactions']['by_type'].items():
        print(f"    • {itype}: {count}")

def main():
    """Main data generation function"""
    print("🚀 Large-Scale E-commerce Data Generator\n")
    print(f"Configuration:")
    print(f"  - Users: {NUM_USERS}")
    print(f"  - Products: {NUM_PRODUCTS}")
    print(f"  - Interactions: {NUM_INTERACTIONS}\n")
    
    # Generate data
    products = generate_products(NUM_PRODUCTS)
    users = generate_users(NUM_USERS)
    interactions = generate_interactions(users, products, NUM_INTERACTIONS)
    
    # Save data
    save_data(products, users, interactions)
    
    print("\n✨ Data generation complete!")
    print("\nNext steps:")
    print("  1. Run: python seed_database.py")
    print("  2. Start API: uvicorn main:app --reload")
    print("  3. Test: curl \"http://localhost:8000/recommendations/1?limit=5\"")

if __name__ == "__main__":
    main()