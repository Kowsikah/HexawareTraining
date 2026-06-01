CREATE TABLE customers
(
customer_id INT PRIMARY KEY,
customer_name VARCHAR(100),
city VARCHAR(50),
state VARCHAR(50),
gender VARCHAR(10),
membership_type VARCHAR(30)
);

CREATE TABLE products
(
product_id INT PRIMARY KEY,
product_name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10,2)
);

CREATE TABLE orders
(
order_id INT PRIMARY KEY,
customer_id INT references customers(customer_id),
order_date DATE,
order_status VARCHAR(30)
);

CREATE TABLE order_items
(
item_id INT PRIMARY KEY,
order_id INT references orders(order_id),
product_id INT references product(product_id),
quantity INT
);

CREATE TABLE payments
(
payment_id INT PRIMARY KEY,
order_id INT references orders(order_id),
payment_mode VARCHAR(30),
payment_status VARCHAR(30),
amount DECIMAL(10,2)
);
CREATE TABLE deliveries
(
delivery_id INT PRIMARY KEY,
order_id INT references orders(order_id),
delivery_partner VARCHAR(50),
delivery_status VARCHAR(30),
delivery_city VARCHAR(50)
);