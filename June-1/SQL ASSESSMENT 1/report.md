There are  6 tables in this database.
Customer=> It consist of customer details.
Product=>Consist of product details and their price.
Orders=>Consist of customer_id and the order details like order_status
order_items=>Consist of items ordered with referencing order_id.
Payments=>It consist of payment mode,status,amount,order_id
deliveries=>consist of delivery status and details like delivery partner with foreign key order_id.

Tables of database:
             Payments
               |
customers--->orders<------order_items<---product_id
              |
              deliveries

Report Analysis:
Membership Analysis:
Gold (3): Anitha, Fiona, Preethi
Regular (3): Chinna, Bharat, Hannah
Platinum (2): swathi, Prathik
Silver (2): Babu, George

Customer 1 ("Anitha") is the most active, placing 3 unique orders.
Babu (2 orders), Chinna (2 orders), and swathi (2 orders) are also repeat customers.
Bharat (Customer 5) has placed an order (Order 306), but it was Cancelled, meaning he has 0 successful historical orders.

Total successful gross sales collected by the platform equal $4,786.23.
Credit Cards dominate, securing 6 successful transactions.

Delivery status:

Delivered: 8 orders have successfully reached their final destination.
Pending: 4 orders are stuck awaiting fulfillment dispatch (Orders 305, 311, 314, 315).
In Transit: 2 orders are actively on the move with couriers (Orders 303, 308).
Cancelled: 1 order was stopped and never fulfilled (Order 306).

Delivery partners and the orders handled:
FedEx: 5 orders handled (3 Delivered, 1 In Transit, 1 Cancelled).
UPS: 4 orders handled (2 Delivered, 2 Pending).
USPS: 3 orders handled (1 Delivered, 2 Pending).
DHL: 3 orders handled (1 Delivered, 2 In Transit).