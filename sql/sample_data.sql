-- Users
INSERT INTO users (username, email, password_hash, role) VALUES
('admin', 'admin@example.com', 'hashed_password_1', 'admin'),
('storekeeper', 'storekeeper@example.com', 'hashed_password_2', 'clerk');

-- Suppliers
INSERT INTO suppliers (name, contact_person, phone, email, address) VALUES
('TechSource Ltd.', 'Jane Mwangi', '0711223344', 'jane@techsource.com', 'Nairobi, Kenya'),
('GreenFarm Distributors', 'Peter Otieno', '0722334455', 'peter@greenfarm.co.ke', 'Eldoret, Kenya');

-- Categories
INSERT INTO categories (category_name, description) VALUES
('Electronics', 'Devices and gadgets like laptops, phones, etc.'),
('Furniture', 'Chairs, tables, and other office/home furnishings'),
('Groceries', 'Everyday consumables and food products');

-- Products
INSERT INTO products (product_name, category_id, supplier_id, quantity_in_stock, unit_price) VALUES
('Laptop', 1, 1, 15, 75000.00),
('Office Chair', 2, 2, 30, 9500.00),
('Smartphone', 1, 1, 10, 45000.00),
('Tomatoes', 3, 2, 50, 150.00);

-- Customers
INSERT INTO customers (name, phone, email, address) VALUES
('Alice Wanjiru', '0711002200', 'alice@example.com', 'Nakuru'),
('John Kariuki', '0722334455', 'john@example.com', 'Mombasa');

-- Stock Entries
INSERT INTO stock_entries (product_id, supplier_id, quantity, user_id) VALUES
(1, 1, 10, 1),
(2, 2, 20, 2),
(3, 1, 5, 1);

-- Stock Movements
INSERT INTO stock_movements (product_id, quantity_change, movement_type, user_id) VALUES
(1, 10, 'IN', 1),
(2, 5, 'OUT', 2),
(3, 3, 'IN', 1);
