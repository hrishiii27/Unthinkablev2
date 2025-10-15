-- E-commerce Product Recommender Database Schema
-- Compatible with PostgreSQL and SQLite

-- Drop tables if they exist (for clean setup)
DROP TABLE IF EXISTS interactions CASCADE;
DROP TABLE IF EXISTS user_preferences CASCADE;
DROP TABLE IF EXISTS product_tags CASCADE;
DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- Users table

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    age INTEGER,
    persona VARCHAR(100),
    price_sensitivity VARCHAR(20) CHECK (price_sensitivity IN ('low', 'medium', 'high')),
    budget_min DECIMAL(10, 2),
    budget_max DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- User interests/preferences (normalized)
CREATE TABLE user_preferences (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    interest VARCHAR(50) NOT NULL,
    weight DECIMAL(3, 2) DEFAULT 1.0, -- Importance weight 0-1
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Products table
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    category VARCHAR(50) NOT NULL,
    subcategory VARCHAR(50),
    price DECIMAL(10, 2) NOT NULL,
    brand VARCHAR(100),
    rating DECIMAL(3, 2) CHECK (rating >= 0 AND rating <= 5),
    description TEXT,
    features TEXT, -- JSON array stored as text
    stock INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Product tags (normalized for better querying)
CREATE TABLE product_tags (
    id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    tag VARCHAR(50) NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    UNIQUE(product_id, tag)
);

-- Interactions table (user behavior tracking)
CREATE TABLE interactions (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    interaction_type VARCHAR(20) NOT NULL CHECK (
        interaction_type IN ('view', 'click', 'add_to_cart', 'purchase', 'like', 'dislike', 'review')
    ),
    session_duration_seconds INTEGER,
    device VARCHAR(20) CHECK (device IN ('desktop', 'mobile', 'tablet')),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    metadata TEXT, -- JSON for additional context
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create indexes for better query performance
CREATE INDEX idx_products_category ON products(category);
CREATE INDEX idx_products_price ON products(price);
CREATE INDEX idx_products_rating ON products(rating);
CREATE INDEX idx_product_tags_tag ON product_tags(tag);
CREATE INDEX idx_product_tags_product ON product_tags(product_id);
CREATE INDEX idx_interactions_user ON interactions(user_id);
CREATE INDEX idx_interactions_product ON interactions(product_id);
CREATE INDEX idx_interactions_type ON interactions(interaction_type);
CREATE INDEX idx_interactions_timestamp ON interactions(timestamp);
CREATE INDEX idx_user_preferences_user ON user_preferences(user_id);

-- Create views for common queries

-- View: User activity summary
CREATE VIEW user_activity_summary AS
SELECT 
    u.id,
    u.name,
    u.persona,
    COUNT(DISTINCT i.id) as total_interactions,
    COUNT(DISTINCT CASE WHEN i.interaction_type = 'view' THEN i.id END) as views,
    COUNT(DISTINCT CASE WHEN i.interaction_type = 'purchase' THEN i.id END) as purchases,
    MAX(i.timestamp) as last_interaction
FROM users u
LEFT JOIN interactions i ON u.id = i.user_id
GROUP BY u.id, u.name, u.persona;

-- View: Product popularity
CREATE VIEW product_popularity AS
SELECT 
    p.id,
    p.name,
    p.category,
    p.price,
    p.rating,
    COUNT(DISTINCT i.id) as total_interactions,
    COUNT(DISTINCT CASE WHEN i.interaction_type = 'purchase' THEN i.id END) as purchase_count,
    COUNT(DISTINCT i.user_id) as unique_viewers,
    AVG(CASE WHEN i.interaction_type = 'view' THEN i.session_duration_seconds END) as avg_view_duration
FROM products p
LEFT JOIN interactions i ON p.id = i.product_id
GROUP BY p.id, p.name, p.category, p.price, p.rating;

-- View: Recent user interactions (last 30 days)
CREATE VIEW recent_user_interactions AS
SELECT 
    i.user_id,
    i.product_id,
    p.name as product_name,
    p.category,
    i.interaction_type,
    i.timestamp
FROM interactions i
JOIN products p ON i.product_id = p.id
WHERE i.timestamp >= datetime('now', '-30 days')
ORDER BY i.timestamp DESC;

-- View: Product recommendations base (products frequently bought together)
CREATE VIEW products_bought_together AS
SELECT 
    i1.product_id as product_a,
    i2.product_id as product_b,
    COUNT(DISTINCT i1.user_id) as co_purchase_count
FROM interactions i1
JOIN interactions i2 ON i1.user_id = i2.user_id 
    AND i1.product_id < i2.product_id
    AND i1.interaction_type = 'purchase'
    AND i2.interaction_type = 'purchase'
GROUP BY i1.product_id, i2.product_id
HAVING COUNT(DISTINCT i1.user_id) >= 2
ORDER BY co_purchase_count DESC;

-- Trigger to update product updated_at timestamp
CREATE TRIGGER update_product_timestamp 
AFTER UPDATE ON products
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE id = NEW.id;
END;

-- Trigger to update user last_active timestamp
CREATE TRIGGER update_user_last_active
AFTER INSERT ON interactions
BEGIN
    UPDATE users SET last_active = CURRENT_TIMESTAMP WHERE id = NEW.user_id;
END;

-- Sample queries for testing

-- Get top products by category
-- SELECT * FROM product_popularity WHERE category = 'Electronics' ORDER BY total_interactions DESC LIMIT 10;

-- Get user's interaction history
-- SELECT * FROM recent_user_interactions WHERE user_id = 1;

-- Find similar users (based on interaction patterns)
-- SELECT u1.user_id, u2.user_id, COUNT(*) as common_products
-- FROM interactions u1
-- JOIN interactions u2 ON u1.product_id = u2.product_id AND u1.user_id < u2.user_id
-- GROUP BY u1.user_id, u2.user_id
-- ORDER BY common_products DESC;

-- Get products matching user interests
-- SELECT DISTINCT p.* 
-- FROM products p
-- JOIN product_tags pt ON p.id = pt.product_id
-- JOIN user_preferences up ON pt.tag = up.interest
-- WHERE up.user_id = 1
-- ORDER BY p.rating DESC;