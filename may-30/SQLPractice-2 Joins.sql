CREATE TABLE customers
(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    city VARCHAR(50),
    phone VARCHAR(15)
);

CREATE TABLE orders
(
    order_id INT PRIMARY KEY,
    customer_id INT,
    product_name VARCHAR(50),
    order_amount DECIMAL(10,2),
    order_status VARCHAR(30)
);

INSERT INTO customers VALUES
(1, 'Rahul Sharma', 'Hyderabad', '9876543210'),
(2, 'Priya Reddy', 'Bangalore', '9876543211'),
(3, 'Amit Kumar', 'Mumbai', NULL),
(4, 'Sneha Patel', 'Chennai', '9876543213'),
(5, 'Arjun Verma', NULL, '9876543214'),
(6, 'Neha Singh', 'Delhi', '9876543215');

INSERT INTO orders VALUES
(101, 1, 'Laptop', 55000, 'Delivered'),
(102, 1, 'Mouse', 700, 'Delivered'),
(103, 2, 'Mobile', 25000, 'Shipped'),
(104, 3, 'Keyboard', NULL, 'Pending'),
(105, 7, 'Printer', 18000, 'Delivered'),
(106, NULL, 'Office Chair', 7500, 'Pending'),
(107, 4, NULL, 12000, 'Cancelled'),
(108, 8, 'Monitor', 1500, NULL);
/*Inner join: The common information on both tables.(intersection area)*/
Select c.customer_id,c.customer_name,c.city,o.order_id,o.product_name,o.order_amount,o.order_status from customers c inner join orders o where c.customer_id=o.customer_id;

/*Left Join: The common information on both tables +information in left table.We are performing join to identify the bad data like the order that do not have product name,the orders that do not have product amount or price which may leads to inconsistencies in the data.*/

Select c.customer_id,c.customer_name,c.city,o.order_id,o.product_name,o.order_amount,o.order_status from customers c left join orders o on c.customer_id=o.customer_id;

/*Right Join: The common things on both table+right table*/
Select c.customer_id,c.customer_name,c.city,o.order_id,o.product_name,o.order_amount,o.order_status from customers c right join orders o on c.customer_id=o.customer_id;
/*Full Join:*/
Select c.customer_id,c.customer_name,c.city,o.order_id,o.product_name,o.order_amount,o.order_status from customers c right join orders o on c.customer_id=o.customer_id union Select c.customer_id,c.customer_name,c.city,o.order_id,o.product_name,o.order_amount,o.order_status from Customers c left join orders o on c.customer_id=o.customer_id ;
/*Subquery:
Details of the customers who have placed order:*/
select * from customers where customers.customer_id in (select customer_id from orders);
/*The details of the customers who have not placed the order:*/
select customer_name from customers where customer_id not in (select customer_id from orders where customer_id is not null);
/*The details of the customers whose order amount is greater than average:*/
select * from orders where order_amount>(select AVG(order_amount) from orders);
/*The details of the customers who have ordered more amount:*/
select * from orders where order_amount=(select MAX(order_amount) from orders);

