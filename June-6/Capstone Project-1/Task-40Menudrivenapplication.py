import csv
import sys


def view_orders():
    print("\n--- All Orders ---")
    with open("orders.csv", "r") as fp:
        reader=csv.reader(fp)
        for row in reader:
            print(row)


def revenue_city():
    revenue_city = dict()
    with open("orders.csv", "r") as fp:
        reader=csv.reader(fp)
        next(reader)
        for data in reader:
            if revenue_city.get(data[2]):
                revenue_city[data[2]] += int(data[5]) * int(data[6])
            else:
                revenue_city[data[2]] = int(data[5]) * int(data[6])
    print("\nCity and Revenue:")
    for city_name, revenue in revenue_city.items():
        print(city_name, revenue)


def revenue_category():
    category_revenue = dict()
    with open("orders.csv", "r") as fp:
        fp.readline()
        line = fp.readline()
        while line:
            data = line.split(',')
            if category_revenue.get(data[4]):
                category_revenue[data[4]] += int(data[5]) * int(data[6])
            else:
                category_revenue[data[4]] = int(data[5]) * int(data[6])
            line = fp.readline()
    print("\nCategory by revenue:")
    for category_name, revenue in category_revenue.items():
        print(category_name, revenue)


def revenue_product():
    product_revenue = dict()
    print("\nProducts and their order revenue:")
    with open("orders.csv", "r") as fp:
        reader=csv.reader(fp)
        next(reader)
        for data in reader:
            revenue = int(data[5]) * int(data[6])
            if product_revenue.get(data[3]):
                product_revenue[data[3]] += revenue
            else:
                product_revenue[data[3]] = revenue
    for product_name, revenue in product_revenue.items():
        print(product_name, revenue)


def product_quantity():
    product_qty = dict()
    with open("orders.csv", "r") as fp:
        reader=csv.reader(fp)
        next(reader)
        for data in reader:
            if product_qty.get(data[3]):
                product_qty[data[3]] += int(data[5])
            else:
                product_qty[data[3]] = int(data[5])
            line = fp.readline()
    print("\nProduct Quantities Sold:")
    for product_name, quantity in product_qty.items():
        print(product_name, quantity)


def city_orders():
    city_ord = dict()
    with open("orders.csv", "r") as fp:
        reader=csv.reader(fp)
        next(reader)
        for data in reader:
            if city_ord.get(data[2]):
                city_ord[data[2]] += 1
            else:
                city_ord[data[2]] = 1
    print("\nCity and Orders:")
    for city_name, order_count in city_ord.items():
        print(city_name, order_count)


def export_reports():
    with open("report.txt", "w") as f1:
        f1.write("City and Revenue\n")
        # 1. City Revenue
        revenue_city_dict = dict()
        with open("orders.csv", "r") as fp:
            fp.readline()
            line = fp.readline()
            while line:
                data = line.split(',')
                if revenue_city_dict.get(data[2]):
                    revenue_city_dict[data[2]] += int(data[5]) * int(data[6])
                else:
                    revenue_city_dict[data[2]] = int(data[5]) * int(data[6])
                line = fp.readline()
        for city_name, revenue in revenue_city_dict.items():
            f1.write(f"{city_name} {revenue}\n")

        # 2. Category Revenue
        f1.write("\nCategory by revenue\n")
        category_revenue = dict()
        with open("orders.csv", "r") as fp:
            fp.readline()
            line = fp.readline()
            while line:
                data = line.split(',')
                if category_revenue.get(data[4]):
                    category_revenue[data[4]] += int(data[5]) * int(data[6])
                else:
                    category_revenue[data[4]] = int(data[5]) * int(data[6])
                line = fp.readline()
        for category_name, revenue in category_revenue.items():
            f1.write(f"{category_name} {revenue}\n")

        # 3. Product Revenue
        f1.write("\nProducts and their order revenue\n")
        product_revenue = dict()
        with open("orders.csv", "r") as fp:
            fp.readline()
            line = fp.readline()
            while line:
                data = line.split(',')
                revenue = int(data[5]) * int(data[6])
                if product_revenue.get(data[3]):
                    product_revenue[data[3]] += revenue
                else:
                    product_revenue[data[3]] = revenue
                line = fp.readline()
        for product_name, revenue in product_revenue.items():
            f1.write(f"{product_name} {revenue}\n")

        # 4. Product Quantity
        f1.write("\nProduct Quantities Sold\n")
        product_qty = dict()
        with open("orders.csv", "r") as fp:
            reader=csv.reader(fp)
            next(reader)
            for data in reader:
                if product_qty.get(data[3]):
                    product_qty[data[3]] += int(data[5])
                else:
                    product_qty[data[3]] = int(data[5])
        for product_name, quantity in product_qty.items():
            f1.write(f"{product_name} {quantity}\n")

        # 5. City Orders
        f1.write("\nCity and Orders\n")
        city_ord = dict()
        with open("orders.csv", "r") as fp:
            fp.readline()
            line = fp.readline()
            while line:
                data = line.split(',')
                if city_ord.get(data[2]):
                    city_ord[data[2]] += 1
                else:
                    city_ord[data[2]] = 1
                line = fp.readline()
        for city_name, order_count in city_ord.items():
            f1.write(f"{city_name} {order_count}\n")

    print("\nReport exported to report.txt successfully.")


def main():
    while True:
        print("\n1. View Orders")
        print("2. Revenue Analysis")
        print("3. Product Analysis")
        print("4. City Analysis")
        print("5. Export Reports")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_orders()
        elif choice == "2":
            revenue_city()
            revenue_category()
        elif choice == "3":
            revenue_product()
            product_quantity()
        elif choice == "4":
            city_orders()
        elif choice == "5":
            export_reports()
        elif choice == "6":
            print("Exiting application.")
            sys.exit()
        else:
            print("Invalid choice, please select again.")


if __name__ == "__main__":
    main()