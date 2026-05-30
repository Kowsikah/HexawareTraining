CREATE TABLE books 
( 
    book_id INT PRIMARY KEY, 
    book_title VARCHAR(100), 
    category VARCHAR(50),
    author VARCHAR(50), 
    price DECIMAL(10,2), 
    stock INT, 
    published_year INT 
);
INSERT INTO books VALUES 
(1, 'Python Basics', 'Programming', 'Ravi Kumar', 550, 30, 2021), 
(2, 'Advanced SQL', 'Database', 'Priya Sharma', 750, 15, 2020), 
(3, 'Data Engineering Guide', 'Data', 'Amit Verma', 1200, 10, 2023), 
(4, 'Machine Learning Start', 'AI', 'Neha Reddy', 950, 8, 2022), 
(5, 'Excel for Business', 'Business', 'Kiran Rao', 400, 50, 2019), 
(6, 'Power BI Reports', 'Data', 'Sneha Patel', 850, 12, 2021), 
(7, 'Java Fundamentals', 'Programming', 'Arjun Mehta', 600, 20, 2018), 
(8, 'Cloud Basics', 'Cloud', 'Rahul Nair', 700, 18, 2022), 
(9, 'SQL Interview Prep', 'Database', 'Farhan Ali', 500, 25, 2024), 
(10, 'AI for Beginners', 'AI', 'Meera Singh', 650, 5, 2023);

/*Exercise 1:Displaying all books*/
select * from books;

/*Exercise 2: Displaying specific rows: book_title,category,price*/
select book_title,category,price from books;

/*Exercise 3:Find unique categories*/
select distinct(category) from books;

/*Exercise 4:Displaying Programming category books*/
select * from books where category='Programming';

/*Exercise 5:Find books above 700 price*/
select * from books where price>700;

/*Exercise 6:stock <15*/
select * from books where stock<15;

/*Exercise 7: Display books of Programming,AI,Database*/
select * from books where category in('Programming','AI','DATABASE');

/*Exercise 8: Display books price between 500 and 900*/
select * from books where price between 500 and 900;

/*Exercise 9:Display the books that contains SQL*/
select book_title from books where book_title like '%SQL%';

/*Exercise 10: Title starts with data*/
select book_title from books where book_title like 'Data%';

/*Exercise 11:sorting the books from highest to lowest price*/
select * from books order by price desc;

/*Exercise 12:Category ascend price desc*/
select * from books order by category asc,price desc;

/*Exercise 13:Total number of books*/
select count(*)as TotalBooks from books;

/*Exercise 14:Display Highest Price*/
select max(price) as MaxPrice from books;

/*Exercise 15:Display Lowest price*/
select min(price) as MinPrice from books;

/*Exercise 16:Display Average book price*/
select avg(price) as AveragePrice from books;

/*Exercise 17:Total stock Available*/
select sum(stock) as TotalStock from books;

/*Exercise 18:Number of books in each category*/
select category,count(category) as Numberofbooks from books group by category;

/*Exercise 19:Avg by each category*/
select category,avg(price) as AveragePrice from books group by category;

/*Exercise 20:Display total stock by category*/
select category,sum(stock) as TotalStock from books group by category;

/*Exercise 21:Display categories more than one book*/
select category from books group by category having count(*)>1;

/*Exercise 22:Display category whose average price>700*/
select category from books group by category having avg(price)>700;

CREATE TABLE departments 
( 
    department_id INT PRIMARY KEY, 
    department_name VARCHAR(50), 
    location VARCHAR(50) 
);

CREATE TABLE employees 
( 
    employee_id INT PRIMARY KEY, 
    employee_name VARCHAR(50), 
    department_id INT, 
    salary DECIMAL(10,2), 
    city VARCHAR(50), 
    manager_id INT 
); 

INSERT INTO departments VALUES 
(10, 'IT', 'Hyderabad'), 
(20, 'HR', 'Bangalore'), 
(30, 'Finance', 'Mumbai'), 
(40, 'Sales', 'Delhi'), 
(50, 'Marketing', NULL); 

INSERT INTO employees VALUES 
(101, 'Rahul Sharma', 10, 75000, 'Hyderabad', 201), 
(102, 'Priya Reddy', 10, 85000, 'Bangalore', 201), 
(103, 'Amit Kumar', 20, 55000, NULL, 202), 
(104, 'Sneha Patel', 30, 65000, 'Mumbai', 203), 
(105, 'Arjun Verma', NULL, 60000, 'Chennai', 204), 
(106, 'Neha Singh', 60, 50000, 'Delhi', NULL), 
(107, 'Farhan Ali', 40, NULL, 'Hyderabad', 205),
(108, 'Meera Nair', 10, 90000, 'Pune', 201); 
/*Exercise 23: Inner join*/
select e.employee_name,e.salary,d.department_name,d.location from employees e inner join departments d on e.department_id=d.department_id;


/*Exercise 24:Left Join*/
select * from employees e left join departments d on e.department_id=d.department_id;

/*Exercise 25:Employees with non-valid department*/
select e.employee_name from employees e left join departments d on e.department_id=d.department_id where d.department_id is null;

/*Exercise 26:Right join*/
select * from employees e right join departments d on e.department_id=d.department_id;

/*Exercise 27:Department where no employees assigned*/
select d.department_name from employees e right join departments d on e.department_id=d.department_id where e.department_id is null;

/*Exercise 28:employee with salary null*/
select * from employees where salary is null;

/*Exercise 29:employee with city null*/
select * from employees where city is null;

/*Exercise 30:department with location null*/
select department_name from departments where location is null;

/*Exercise 31:departments with count*/
select d.department_name,count(e.department_id) from employees e right join departments d on e.department_id=d.department_id group by e.department_id,d.department_name;

/*Exercise 32:department with their Average salary*/
select d.department_name,avg(e.salary) from employees e right join departments d on e.department_id=d.department_id group by d.department_id,d.department_name;

/*Excercise 33*/
select d.department_name from employees e right join departments d on e.department_id=d.department_id group by e.department_id,d.department_name having count(e.department_id)>2;

/*Exercise 34* Department wise highest salary*/
select d.department_name,max(e.salary) from employees e right join departments d on e.department_id=d.department_id group by d.department_id,d.department_name;

CREATE TABLE customers_new 
(
   customer_id INT PRIMARY KEY, 
    customer_name VARCHAR(50), 
    city VARCHAR(50), 
    membership_type VARCHAR(30) 
);

CREATE TABLE payments 
( 
    payment_id INT PRIMARY KEY, 
    customer_id INT, 
    amount DECIMAL(10,2), 
    payment_mode VARCHAR(30), 
    payment_status VARCHAR(30) 
); 

INSERT INTO customers_new VALUES 
(1, 'Ramesh Gupta', 'Hyderabad', 'Gold'), 
(2, 'Sana Khan', 'Bangalore', 'Silver'), 
(3, 'John Mathew', 'Mumbai', 'Gold'), 
(4, 'Ayesha Begum', 'Chennai', 'Bronze'), 
(5, 'Vikram Rao', 'Delhi', 'Silver'), 
(6, 'Divya Sharma', 'Pune', NULL); 

INSERT INTO payments VALUES 
(1001, 1, 15000, 'UPI', 'Success'), 
(1002, 1, 8000, 'Card', 'Success'), 
(1003, 2, 5000, 'Cash', 'Pending'), 
(1004, 3, 22000, 'UPI', 'Success'), 
(1005, 7, 12000, 'Card', 'Failed'), 
(1006, NULL, 3000, 'Cash', 'Pending'), 
(1007, 4, NULL, 'UPI', 'Success'), 
(1008, 5, 7000, NULL, 'Success');

/*Exercise 35-Customers made payment*/
select customer_name from customers_new where customer_id in (select customer_id from payments);

/*Exercise 36- customers who have not made payment*/
select customer_name as NonPayers from customers_new where customer_id not in (select customer_id from payments where customer_id is not null);

/*Exercise 37-Find payments greater than average*/
select * from payments where amount>(select avg(amount) from payments);

/*Exercise 38-find customers who made highest payment*/
select customer_name from customers_new where customer_id in(select customer_id from payments where amount=(select max(amount) from payments));

/*Exercise 39-Gold customers who made payments*/
select customer_name from customers_new where membership_type='Gold' and customer_id in(select customer_id from payments);

/*Exercise 40-payment greater than 10000*/
select customer_name from customers_new where customer_id in (select customer_id from payments where amount>10000);

/*Exercise 41*/
select payment_id from payments where customer_id not in (select customer_id from customers_new) and customer_id is not null;

/*Exercise 42*/
SELECT * FROM customers_new c
WHERE EXISTS (
    SELECT 1 
    FROM payments p 
    WHERE c.customer_id = p.customer_id
);

/*Exercise 43*/
SELECT * FROM customers_new c
WHERE NOT EXISTS (
    SELECT 1 
    FROM payments p 
    WHERE c.customer_id = p.customer_id
);

/*Exercise 44-*/
select customer_name from customers_new where customer_id in (select customer_id from payments where amount>(select amount from payments where customer_id=2));