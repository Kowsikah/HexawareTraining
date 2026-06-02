

/*1 Q-Displaying all customers*/
select * from customers;

/*2 Q-Displaying customer name,city,membership_type*/
select customer_name,city,membership_type from customers;

/*3 -Displaying product sort by price in descending*/
select * from products order by price desc;

/*4-Hyderabad customers*/
select * from customers where city='Hyderabad';

/*5-Display gold membership customers*/
select * from customers where membership_type='Gold';

/*6 -Products price between 500 and 5000*/
select * from products where price between 500 and 5000;

/*7-Electronics and Fashion products*/
select * from products where category='Electronics' or category='Fashion';

/*8- order placed after 2026-01-01*/
select * from orders where order_date>'2026-01-01';

/*9- Payments mode upi*/
select * from payments where payment_mode='UPI';

/*10- Pending deliveries*/
select * from deliveries where delivery_status='Pending';

/*11-Total customers*/
select count(*) as Total_customers from customers;

/*12-Total orders*/
select count(*) as Total_Orders from orders;

/*13-Total Products*/
select count(*) as Total_Products from products;

/*14-Revenue Success payments*/
select sum(amount) from payments where payment_status='Success';

/*15-Average payment amount*/
select avg(amount) from payments;

/*16-Highest payment amount*/
select max(amount) from payments;

/*17-Lowest payment amount*/
select min(amount) from payments;

/*18- Count customers by city*/
select city,count(customer_id) from customers group by city;

/*19 - Count products by category*/
select category,count(product_id) from products group by category;

/*20-Count orders by status*/
select order_status,count(order_id) from orders group by order_status;

/*21-Customer name,order id,order status*/
select c.customer_name,o.order_id,o.order_status from customers c inner join orders o on c.customer_id=o.customer_id;

/*22-order ID, product name, quantity, and price.*/
select o.order_id,p.product_name,o.quantity,p.price from order_items o inner join products p on o.product_id=p.product_id;

/*23-customer name, product name, quantity, and order date.*/
select c.customer_name,p.product_name,o1.quantity,o.order_date from customers c inner join orders o on c.customer_id=o.customer_id inner join order_items o1 on o1.order_id=o.order_id inner join products p on p.product_id=o1.product_id;

/*24-order ID with payment mode, payment status, and amount.*/
select o.order_id,p.payment_mode,p.payment_status,p.amount from orders o inner join payments p on o.order_id=p.order_id;

/*25-order ID with delivery partner and delivery status.*/
select o.order_id,d.delivery_partner,d.delivery_status from orders o inner join deliveries d on o.order_id=d.order_id;

/*26-. Display full order report:Customer Name,City,Order ID,Order Date,Product Name,Category,Quantity,Price,Payment Status,Delivery Status*/

SELECT c.customer_name,c.city,o.order_id,o.order_date,p.product_name,p.category,o1.quantity,p.price,p1.payment_status 
FROM customers c 
INNER JOIN orders o       ON c.customer_id = o.customer_id 
INNER JOIN order_items o1 ON o.order_id = o1.order_id 
INNER JOIN products p     ON o1.product_id = p.product_id 
INNER JOIN payments p1    ON o.order_id = p1.order_id 
INNER JOIN deliveries d   ON o.order_id = d.order_id;

/*27-Total revenue by city*/
select c.city,sum(p.amount) as Total_revenue from customers c inner join orders o on c.customer_id=o.customer_id inner join payments p on p.order_id=o.order_id group by c.city; 

/*28-Total revenue by customers*/
select c.customer_name,sum(p.amount) as Total_revenue from customers c inner join orders o on c.customer_id=o.customer_id inner join payments p on p.order_id=o.order_id group by c.customer_id; 

/*29-Total quantity sold by a product*/
select p.product_name,sum(o1.quantity) as Total_Quantity from products p inner join  order_items o1 on p.product_id=o1.product_id group by o1.product_id; 

/*30-Number of orders by customer.*/
select c.customer_id,count(o.order_id) as No_of_orders from customers c inner join orders o on o.customer_id=c.customer_id group by o.customer_id;

/*32. Customers having more than 1 order.*/
select c.customer_id,count(o.order_id) as No_of_orders from customers c inner join orders o on o.customer_id=c.customer_id group by o.customer_id having count(o.customer_id)>1;

/*33- Product categories having revenue greater than ₹10,000.*/
select p.category,sum(p1.amount) from products p inner join order_items o on p.product_id=o.product_id inner join order_items o1 on o.order_id=o1.order_id inner join  payments p1 on p1.order_id=o1.order_id group by p.category;

/*34- Cities having more than 2 customers. */
select c.city,count(distinct o.customer_id) from customers c inner join orders o on c.customer_id=o.customer_id group by c.city having count(distinct o.customer_id)>2;

/*35-product sold more than 3 times*/
select p.product_name,count(o1.order_id) from products p inner join order_items o1 on p.product_id=o1.product_id group by o1.product_id having count(o1.order_id)>3;

/*36-Customers who placed order*/
select customer_name from customers where customer_id in (select customer_id from orders);

/*37-Customers who have never placed orders*/
select customer_name from customers where customer_id not in (select customer_id from orders);

/*38-Products that have never ordered*/
select product_name from products where product_id not in(select product_id from order_items);

/*39-Orders with amount greater than average*/
select order_id from payments where amount>(select avg(amount) from payments) and payment_status='Success';

/*40 - customer who made highest payment*/
select customer_name from customers where customer_id in(select customer_id from orders where order_id in(select order_id from payments where amount=(select max(amount) from payments where payment_status='Success')));

/*41 -Product price above average price */
select product_name from products where price>(select avg(price) from products);

/*42- Customers who ordered electronic products*/
select customer_name from customers where customer_id in (select customer_id from orders where order_id in (select order_id from order_items where product_id in(select product_id from products where category='Electronics')));

/*43-Orders that have Successful payments*/
select * from orders where order_id in(select order_id from payments where payment_status='Success');

/*44- Orders that have not delivered*/
select * from orders where order_id not in(select order_id from deliveries where delivery_status='Delivered');

/*45-customers whose total spending is above average customer spending.*/
SELECT c.customer_id,c.customer_name,SUM(p.amount) AS total_spending
FROM customers c
INNER JOIN orders o on c.customer_id = o.customer_id
INNER JOIN payments p on o.order_id = p.order_id
GROUP BY c.customer_id, c.customer_name
HAVING SUM(p.amount) > (
    SELECT AVG(amount) 
    FROM payments
);

/*46-orders without payment records.*/
select * from orders o left join payments p on o.order_id=p.order_id where p.order_id is null;

/*47-orders with no delivery records*/
select * from orders o left join deliveries d on o.order_id=d.order_id where d.order_id is null;

/*48- Payments with amount NULL or zero*/
select * from payments where amount is null or amount=0;

/*49-Delivered orders with failed payment*/
select * from deliveries inner join  payments on payments.order_id=deliveries.order_id where payments.payment_status not in('Cancelled','Pending','Success') and deliveries.delivery_status='Success';

/*50-cancelled orders with successful payment.*/
select * from orders inner join payments on orders.order_id=payments.order_id where orders.order_status='Cancelled'and payments.payment_status='Success';

/*51-Order items with invalid customer ID's*/
select order_id from orders where customer_id not in(select customer_id from customers);

/*52-Order items with invalid product ID*/
select order_id from order_items where product_id not in(select product_id from products);