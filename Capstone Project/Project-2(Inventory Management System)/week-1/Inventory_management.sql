create table product(product_id int primary key,
              product_name varchar(30),
              supplier_id int,
              unit_price int,
              category varchar(30),
              brand varchar(20));

create table warehouse(warehouse_id int primary key,
                      product_id int,
                      stock_quantity int,
                      reorder_level int,
                      last_update varchar(20),
                      FOREIGN KEY (product_id) REFERENCES product(product_id));

create table stock_movement(movement_id int primary key,
                            warehouse_id int,
                            product_id int,
                            product_name varchar(30),
                            movement_type varchar(10),
                            date_movement varchar(20),
                            QuantityChanged int,
                            NewQuantity int,
                            FOREIGN KEY (warehouse_id) references warehouse(warehouse_id));

create table suppliers(supplier_id int primary key,
                       supplier_name varchar(30),
                       city varchar(30),
                       rating float,
                       phone varchar(20),
                       email varchar(20));

INSERT INTO product (product_id, product_name, supplier_id, unit_price, category, brand) VALUES
(10, 'Quantum Laptop Pro', 501, 1200, 'Electronics', 'VoltTech'),
(20, 'Wireless Ergonomic Mouse', 501, 45, 'Electronics', 'LogiWave'),
(30, 'Running Shoes Cloud-9', 503, 85, 'Apparel', 'Stride'),
(40, 'Stainless Water Bottle', 504, 25, 'Home & Kitchen', 'HydroFlow'),
(50, 'Mechanical Keyboard', 502, 110, 'Electronics', 'KeyClick');

INSERT INTO warehouse (warehouse_id, product_id, stock_quantity, reorder_level, last_update) VALUES
(1001, 10, 50, 15, '2026-06-10'),
(1002, 20, 200, 50, '2026-06-12'),
(1003, 30, 120, 30, '2026-06-14'),
(1004, 40, 300, 75, '2026-06-11'),
(1005, 50, 80, 120, '2026-06-13');

INSERT INTO suppliers (supplier_id, supplier_name, city, rating, phone, email) VALUES
(501, 'Alpha Tech Logistics', 'New York', 4.8, '555-0192', 'info@alphatech.com'),
(502, 'Global Prime Goods', 'Chicago', 4.2, '555-0143', 'sales@gpgoods.com'),
(503, 'Apex Apparel & Co', 'Los Angeles', 3.9, '555-0177', 'contact@apex.com'),
(504, 'Omega Home Supplies', 'Houston', 4.5, '555-0115', 'order@omegahome.com');

INSERT INTO stock_movement (movement_id, warehouse_id, product_id, product_name, movement_type, date_movement, QuantityChanged, NewQuantity) VALUES
(9001, 1001, 10, 'Quantum Laptop Pro', 'IN', '2026-06-01', 20, 50),
(9002, 1002, 20, 'Wireless Ergonomic Mouse', 'OUT', '2026-06-05', -15, 200),
(9003, 1003, 30, 'Running Shoes Cloud-9', 'IN', '2026-06-08', 40, 120),
(9004, 1004, 40, 'Stainless Water Bottle', 'OUT', '2026-06-11', -50, 300),
(9005, 1005, 50, 'Mechanical Keyboard', 'IN', '2026-06-13', 15, 80);

/*Displaying all records*/
select * from product;
select * from warehouse;
select * from suppliers;
select * from stock_movement;

/*inserting new stock movement*/
insert into stock_movement values(9006,1002,30,'Running Shoes Cloud-9','OUT','2026-06-14',-10,110);
/*Updating stock quanttity*/
update warehouse set stock_quantity=110 where product_id=30;

/*Displaying after updation*/
select * from  stock_movement;

select * from warehouse;

DELIMITER //

CREATE PROCEDURE products_below_reorder_level()
BEGIN
    SELECT p.product_name 
    FROM product p
    INNER JOIN warehouse w ON p.product_id = w.product_id
    WHERE w.stock_quantity < w.reorder_level;
END //

DELIMITER ;

-- To execute the procedure:
CALL products_below_reorder_level();