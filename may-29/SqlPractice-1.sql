/*Creating tables*/
create table Customers(
	Customer_ID int ,
    Customer_name varchar(100),
    City varchar(50)
);
/*Inserting Recors*/
insert into Customers values(1,'Anita','Chennai'),(2,'Vijaya','Hyderabad'),(3,'Harini','Bangalore');

--set  SQL_SAFE_UPDATES=0;
/*Updating specific Records*/
update Customers set City= 'Kerala' where Customer_ID =3;
/* delete particular records*/
delete from Customers where City='Bangalore';

--set  SQL_SAFE_UPDATES=1;
/*Reteriving/Displaying all records*/
select * from Customers;

 
 /*Table Creation*/
 CREATE TABLE products(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(30),
    price DECIMAL(10,2),
    stock_quantity INT,
    supplier_city VARCHAR(30)
);
 /*Inserting values*/
 INSERT INTO products VALUES
(1,'Laptop','Electronics',55000,10,'Hyderabad'),
(2,'Mobile','Electronics',25000,25,'Bangalore'),
(3,'Printer','Electronics',18000,8,'Pune'),
(4,'Office Chair','Furniture',7500,15,'Mumbai'),
(5,'Desk','Furniture',12000,5,'Chennai'),
(6,'Notebook','Stationery',80,200,'Hyderabad'),
(7,'Pen','Stationery',20,500,'Delhi'),
(8,'Water Bottle','Accessories',500,50,'Bangalore');
/*specific columns*/
select product_name,price from products;
/* distinct category*/
select distinct category from products;
/*Stationary products*/
select * from products where category ='Stationery';
/*products whose price>5000*/
select * from products where price >5000;
/*Products in stationary category with price >50*/
select * from products where category ='Stationery' and price >50;
/*Products in Bangalore or Hyderabad as supplier city*/
select * from products where supplier_city ='Bangalore' or supplier_city ='Hyderabad';
/*Products except stationery category*/
select * from products where not category ='Stationery';
/*Product in Bangalore,Hyderabad,Chennai*/
select * from products where supplier_city in ('Bangalore','Hyderabad','Chennai');
/*Products price between the price */
select * from products where price between 500 and  50000;
/*Product name starting with L*/
select * from products where product_name like 'L%';
/*Product name ends with N*/
select * from products where product_name like '%n';
/*Product name contains*/
select * from products where product_name like '%ote%';
/*Alias*/
select product_name as Product ,price as Product_Price  from products;
/Sorting-desc*/
select * from products order by price desc;
/*Aggregation*/
select count(*) as Total_Products from products;
/*Specific counting*/
select count(*) as Rows from products where category ='Stationery';

select sum(price) as Total_Price from products;

select 
count(*) as Total_Products,
sum(price) as Total_Price,
avg(price) as Average_Price,
max(price) as Highest_Price,
min(price) as Lowest_Price from products;
/*Group by clause*/
select category,count(*) as Product_count from products group by category;

select category,sum(price) as Total_Price from products group by category;

