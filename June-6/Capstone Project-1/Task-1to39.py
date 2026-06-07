#Reading csv file(file handling)
import numpy as np
import pandas as pd
import csv
with open("orders.csv","r") as fp:
    reader = csv.reader(fp)
    next(reader)
    for row in reader:
        print(row)
#Task 3-Count Total orders
count=0
with open("orders.csv","r") as fp:
    reader=csv.reader(fp)
    next(reader)
    for row in reader:
        count+=1
print("Total Orders:",count)
#Task 4-Calculating Total Revenue
total_revenue=0
with open("orders.csv","r") as fp:
    reader=csv.reader(fp)
    next(reader)
    for row in reader:
        total_revenue+=(int(row[5])*int(row[6]))
        line=fp.readline()
print("Total Revenue:",total_revenue)
#highest order value
high_order_value=0
with open("orders.csv","r") as fp:
    reader=csv.reader(fp)
    next(reader)
    for data in reader:
        if (int(data[5])*int(data[6]))>high_order_value:
            highest_order_value=int(data[5])*int(data[6])
        line=fp.readline()
print("Highest Order Value:",highest_order_value)
#lowest order value
with open("orders.csv","r") as fp:
    reader=csv.reader(fp)
    next(reader)
    lowest_order_value=highest_order_value
    for data in reader:
        data=line.split(',')
        if(int(data[5])*int(data[6]))<lowest_order_value:
            lowest_order_value=int(data[5])*int(data[6])
        line=fp.readline()
print("Lowest Order Value:",lowest_order_value)
# Average order value
total_order_value=0
with open("orders.csv","r") as fp:
    reader=csv.reader(fp)
    next(reader)
    for data in reader:
        total_order_value+=(int(data[5])*(int(data[6])))
print("Average Order value:",total_order_value/count)
#Display all unique customers
customers=set()
with open("orders.csv","r") as fp:
    reader=csv.reader(fp)
    next(reader)
    for data in reader:
        customers.add(data[1])

print("Unique Customers:")
customers=list(customers)
for c in customers:
    print(c)
#Count Unique customers
print("Total Customers:",len(customers))
#Customer with high purchase amount
print("Customer with highest purchase amount")
with open("orders.csv","r") as fp:
    reader=csv.reader(fp)
    next(reader)
    for data in reader:
        if(int(data[5])*int(data[6]))==highest_order_value:
            print(data[1])
#count orders by product
product_count=dict()
print("Products and their order count:")
with open("orders.csv","r") as fp:
    reader=csv.reader(fp)
    next(reader)
    for data in reader:
        if product_count.get(data[3]):
            product_count[data[3]]+=1
        else:
            product_count[data[3]]=1
for product_name,count in product_count.items():
    print(product_name,count)

#product with revenue
product_revenue=dict()
print("Products and their order revenue:")
with open("orders.csv","r") as fp:
    reader=csv.reader(fp)
    next(reader)
    for data in reader:
        revenue=int(data[5])*int(data[6])
        if product_revenue.get(data[3]):
            product_revenue[data[3]]+=revenue
        else:
            product_revenue[data[3]]=revenue
        line=fp.readline()
for product_name,revenue in product_revenue.items():
    print(product_name,revenue)
Highest_sold_product=""
Highest_count=0
product_quantity=dict()
with open("orders.csv","r") as fp:
    reader=csv.reader(fp)
    next(reader)
    for data in reader:
        if product_quantity.get(data[3]):
            product_quantity[data[3]]+=int(data[5])
        else:
            product_quantity[data[3]]=int(data[5])
for product_name,count in product_quantity.items():
    if count > Highest_count:
        Highest_sold_product=product_name
        Highest_count=count
print("Highest sold product:"+Highest_sold_product+" "+str(Highest_count))
least_sold_product=Highest_sold_product
least_count=Highest_count
for product_name,count in product_quantity.items():
    if count<least_count:
        least_count=count
        least_sold_product=product_name
print("Least sold product:"+least_sold_product+" "+str(least_count))
#revenue by category
category_revenue=dict()
with open("orders.csv","r") as fp:
    reader=csv.reader(fp)
    next(reader)
    for data in reader:
        if category_revenue.get(data[4]):
            category_revenue[data[4]]+=int(data[5])*int(data[6])
        else:
            category_revenue[data[4]]=int(data[5])*int(data[6])

print("Category by revenue")
for category_name,revenue in category_revenue.items():
    print(category_name,revenue)
#count orders by city
city_orders=dict()
with open("orders.csv","r") as fp:
    reader=csv.reader(fp)
    next(reader)
    for data in reader:
        if city_orders.get(data[2]):
            city_orders[data[2]]+=1
        else:
            city_orders[data[2]]=1
print("City and Orders:")
for city_name,order_count in city_orders.items():
    print(city_name,order_count)
#revenue by city
revenue_city=dict()
with open("orders.csv","r") as fp:
    reader=csv.reader(fp)
    next(reader)
    for data in reader:
        if revenue_city.get(data[2]):
            revenue_city[data[2]]+=int(data[5])*int(data[6])
        else:
            revenue_city[data[2]]=int(data[5])*int(data[6])
        line=fp.readline()
print("City and Revenue")
for city_name,revenue in revenue_city.items():
    print(city_name,revenue)
#city generating highest revenue.
highest_revenue=0
for city_name,revenue in revenue_city.items():
    if highest_revenue<revenue:
        highest_revenue=revenue
print("City generating Highest Revenue:")
for city_name,revenue in revenue_city.items():
    if revenue==highest_revenue:
        print(city_name,revenue)
print("Products:")
product_name=[]
with open("orders.csv","r") as fp:
    reader=csv.reader(fp)
    next(reader)
    while line:
        data=line.split(',')
        product_name.append(data[3])
        line=fp.readline()
product_name.sort()
for product in product_name:
    print(product)
cities=set()
with open("orders.csv","r") as fp:
    reader=csv.reader(fp)
    next(reader)
    while line:
        data=line.split(',')
        cities.add(data[2])
        line=fp.readline()
print("Cities:",cities)
#revenue_city
print("Revenue by city",revenue_city)
#products quantity sold
print("Product quantity sold:",product_quantity)
#calculate_revenue
def calculate_revenue():
    total_revenue = 0
    with open("orders.csv", "r") as fp:
        reader=csv.reader(fp)
        next(reader)
        for data in reader:
            data = line.split(",")
            total_revenue += (int(data[5]) * int(data[6]))
    print("Total Revenue:", total_revenue)

def find_top_product():
    Highest_sold_product = ""
    Highest_count = 0
    product_quantity = dict()
    with open("orders.csv", "r") as fp:
        reader=csv.reader(fp)
        next(reader)
        for data in reader:
            data = line.split(',')
            if product_quantity.get(data[3]):
                product_quantity[data[3]] += int(data[5])
            else:
                product_quantity[data[3]] = int(data[5])
            line = fp.readline()
    for product_name, count in product_quantity.items():
        if count > Highest_count:
            Highest_sold_product = product_name
            Highest_count = count
    print("Highest sold product:" + Highest_sold_product + " " + str(Highest_count))

def find_top_city():
    revenue_city = dict()
    with open("orders.csv", "r") as fp:
        reader=csv.reader(fp)
        next(reader)
        for data in reader:
            if revenue_city.get(data[2]):
                revenue_city[data[2]] += int(data[5]) * int(data[6])
            else:
                revenue_city[data[2]] = int(data[5]) * int(data[6])
            line = fp.readline()
    print("City and Revenue")
    # city generating highest revenue.
    highest_revenue = 0
    for city_name, revenue in revenue_city.items():
        if highest_revenue < revenue:
            highest_revenue = revenue
    print("City generating Highest Revenue:")
    for city_name, revenue in revenue_city.items():
        if revenue == highest_revenue:
            print(city_name)

def average_order_value():
    total_order_value = 0
    with open("orders.csv", "r") as fp:
        reader=csv.reader(fp)
        next(reader)
        for data in reader:
            data = line.split(',')
            total_order_value += (int(data[5]) * (int(data[6])))
            line = fp.readline()
    print("Average Order value:", total_order_value / count)

#Handling csv file
try:
    with open("order1.csv", "r") as fp:
        data = fp.read()
        print(data)
except FileNotFoundError:
       print("File not found")

#Handling Invalid quantity
try:
    with open("orders2.csv", "r") as fp:
        reader=csv.reader(fp)
        next(reader)
        for data in reader:
            if int(data[5])<0:
                raise ValueError("Product quantity cannot be negative.")
            if int(data[6])<0:
                raise ValueError("Price cannot be negative.")
            line=fp.readline()
except ValueError as e:
    print(e)

order_data = np.genfromtxt("orders.csv", delimiter=",", dtype=None, names=True, encoding="utf-8")

# Calculate revenue by multiplying quantity and price fields
order_revenue = order_data['quantity'] * order_data['price']

# Calculate statistics
total_revenue = np.sum(order_revenue)
average_revenue = total_revenue / len(order_data)
maximum_revenue = np.max(order_revenue)
minimum_revenue = np.min(order_revenue)
standard_deviation = np.std(order_revenue)

# Print results
print("Total revenue:", total_revenue)
print("Average revenue:", average_revenue)
print("Maximum revenue:", maximum_revenue)
print("Minimum revenue:", minimum_revenue)
print("Standard deviation:", standard_deviation)

df=pd.read_csv("orders.csv")
df["Revenue_Column"]=df["quantity"]*df["price"]
#Display top 5 highest value orders.Display top 5 highest value orders.
print(df.head(5))
#Group by city and calculate revenue.
revenue_city=df.groupby("city")["Revenue_Column"].sum()
print(revenue_city)
#Group by product and calculate revenue.
revenue_product=df.groupby("product")["Revenue_Column"].sum()
print(revenue_product)
#top selling product
top_product_by_qty = df.groupby("product")["quantity"].sum().idxmax()
total_qty_sold = df.groupby("product")["quantity"].sum().max()
print(f"Top selling product by Quantity: {top_product_by_qty} ({total_qty_sold} units sold)")
#order-count by city
city_order=df.groupby("city")["order_id"].count()
print(city_order)
#Report generation
with open("sales_summary_report.txt","w") as fp:
    fp.write("Total Order:"+str(count)+"\n")
    fp.write("Total Revenue"+str(total_revenue))
    fp.write("\nAverage order value"+str(total_order_value/count))
    fp.write("\nHighest order value:"+str(highest_order_value))
    fp.write("\nLowest order value:"+str(lowest_order_value))
    fp.write("\nRevenue by city")
    for city_name,revenue in revenue_city.items():
        fp.write(city_name+" "+str(revenue))
    fp.write("\nRevenue by category")
    for category_name,revenue in category_revenue.items():
        fp.write(category_name+" "+str(revenue))
    fp.write("\nTop selling product by quantity")
    fp.write(top_product_by_qty)
    fp.write("\nTop revenue generating by city")
    highest_revenue = 0
    for city_name, revenue in revenue_city.items():
        if highest_revenue < revenue:
            highest_revenue = revenue
    for city_name, revenue in revenue_city.items():
        if revenue == highest_revenue:
            fp.write(city_name+str(revenue))

with open("orders.csv","r") as fp:
    with open("high_value_orders","w") as f1:
        reader=csv.reader(fp)
        next(reader)
        for data in reader:
            if(int(data[5])*int(data[6])>50000):
                f1.write(line)

with open("electronic_orders","w") as f1:
    with open("orders.csv","r") as f2:
        reader=csv.reader(f2)
        next(reader)
        for data in reader:
            if(data[4]=="Electronics"):
                f1.write(line)
