
/*inserting customer data*/
insert into customers (customer_id, customer_name, city, state, gender, membership_type) VALUES
(1, 'Anitha', 'New York', 'NY', 'Female', 'Gold'),
(2, 'Babu', 'Los Angeles', 'CA', 'Male', 'Silver'),
(3, 'Chinna', 'Chicago', 'IL', 'Male', 'Regular'),
(4, 'swathi', 'New York', 'NY', 'Female', 'Platinum'),
(5, 'Bharat', 'Los Angeles', 'CA', 'Male', 'Regular'),
(6, 'Fiona', 'Chicago', 'IL', 'Female', 'Gold'),
(7, 'George', 'Houston', 'TX', 'Male', 'Silver'),
(8, 'Hannah', 'Miami', 'FL', 'Female', 'Regular'),
(9, 'Prathik', 'Austin', 'TX', 'Male', 'Platinum'),
(10, 'Preethi', 'New York', 'NY', 'Female', 'Gold');

/*inserting product details*/
insert into products (product_id, product_name, category, price) VALUES
(201, 'Smartphone X', 'Electronics', 799.99),
(202, 'Wireless Headphones', 'Electronics', 149.99),
(203, 'Laptop Pro', 'Electronics', 1299.00),
(204, 'Running Shoes', 'Apparel', 89.95),
(205, 'Cotton T-Shirt', 'Apparel', 24.99),
(206, 'Leather Jacket', 'Apparel', 199.00),
(207, 'Coffee Maker', 'Home Goods', 79.99),
(208, 'Blender XL', 'Home Goods', 119.50),
(209, 'Desk Lamp', 'Home Goods', 34.99),
(210, 'Gaming Mouse', 'Electronics', 59.99);

/*inserting orders table records*/
insert into orders (order_id, customer_id, order_date, order_status) VALUES
(301, 1, '2026-05-01', 'Delivered'),
(302, 2, '2026-05-02', 'Delivered'),
(303, 3, '2026-05-03', 'Shipped'),
(304, 1, '2026-05-05', 'Delivered'),
(305, 4, '2026-05-06', 'Processing'),
(306, 5, '2026-05-07', 'Cancelled'), 
(307, 2, '2026-05-08', 'Delivered'),
(308, 6, '2026-05-10', 'Shipped'),
(309, 7, '2026-05-12', 'Delivered'),
(310, 4, '2026-05-15', 'Delivered'),
(311, 8, '2026-05-18', 'Processing'),
(312, 9, '2026-05-20', 'Delivered'),
(313, 10, '2026-05-22', 'Shipped'),
(314, 1, '2026-05-25', 'Processing'),
(315, 3, '2026-05-26', 'Processing');

/*inserting payment records*/
insert into order_items (item_id, order_id, product_id, quantity) VALUES
(401, 301, 201, 1), 
(402, 301, 202, 1), 
(403, 302, 204, 2), -
(404, 302, 205, 3), 
(405, 303, 203, 1),
(406, 304, 207, 1),
(407, 305, 206, 1), 
(408, 305, 209, 2),
(409, 305, 210, 1),
(410, 306, 201, 1),
(411, 307, 208, 1),
(412, 308, 205, 4),
(413, 309, 202, 1),
(414, 310, 203, 1), 
(415, 310, 210, 1),
(416, 311, 207, 1),
(417, 312, 204, 1),
(418, 313, 206, 1),
(419, 314, 202, 2),
(420, 315, 209, 1);

/*inserting product records*/
insert into payments (payment_id, order_id, payment_mode, payment_status, amount) VALUES
(501, 301, 'Credit Card', 'Success', 949.98),
(502, 302, 'PayPal', 'Success', 254.87),
(503, 303, 'Credit Card', 'Success', 1299.00),
(504, 304, 'Debit Card', 'Success', 79.99),
(505, 305, 'Credit Card', 'Success', 293.97),
(506, 306, 'Credit Card', 'Failed', 799.99),  
(507, 307, 'UPI', 'Success', 119.50),
(508, 308, 'PayPal', 'Success', 99.96),
(509, 309, 'Credit Card', 'Success', 149.99),
(510, 310, 'Debit Card', 'Success', 1358.99),
(511, 311, 'Credit Card', 'Failed', 79.99),   
(512, 312, 'UPI', 'Success', 89.95),
(513, 313, 'Credit Card', 'Success', 199.00),
(514, 314, 'PayPal', 'Success', 299.98),
(515, 315, 'Debit Card', 'Success', 34.99);

/*inserting deliveries records*/
insert into deliveries (delivery_id, order_id, delivery_partner, delivery_status, delivery_city) VALUES
(601, 301, 'FedEx', 'Delivered', 'New York'),
(602, 302, 'UPS', 'Delivered', 'Los Angeles'),
(603, 303, 'DHL', 'In Transit', 'Chicago'),
(604, 304, 'FedEx', 'Delivered', 'New York'),
(605, 305, 'USPS', 'Pending', 'New York'),      
(606, 306, 'FedEx', 'Cancelled', 'Los Angeles'),  
(607, 307, 'UPS', 'Delivered', 'Los Angeles'),
(608, 308, 'DHL', 'In Transit', 'Chicago'),
(609, 309, 'USPS', 'Delivered', 'Houston'),
(610, 310, 'FedEx', 'Delivered', 'New York'),
(611, 311, 'UPS', 'Pending', 'Miami'),         
(612, 312, 'DHL', 'Delivered', 'Austin'),
(613, 313, 'FedEx', 'In Transit', 'New York'),
(614, 314, 'USPS', 'Pending', 'New York'),     
(615, 315, 'UPS', 'Pending', 'Chicago');         