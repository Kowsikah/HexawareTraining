class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

    def display(self):
        print("\nCustomer Details")
        print("-----------------------------")
        print(f"Customer ID   : {self.customer_id}")
        print(f"Name          : {self.name}")
        print(f"Email         : {self.email}")
        print(f"Phone         : {self.phone}")
        print("-----------------------------")


class CustomerManagementSystem:
    def __init__(self):
        self.customers = {}

    # Create Customer
    def add_customer(self):
        customer_id = input("Enter Customer ID: ")

        if customer_id in self.customers:
            print("Customer ID already exists.")
            return

        name = input("Enter Customer Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone Number: ")

        customer = Customer(customer_id, name, email, phone)
        self.customers[customer_id] = customer

        print("Customer added successfully.")

    # View All Customers
    def view_customers(self):
        if not self.customers:
            print("No customers available.")
            return

        print("\n===== Customer List =====")
        for customer in self.customers.values():
            customer.display()

    # Search Customer
    def search_customer(self):
        customer_id = input("Enter Customer ID to search: ")

        customer = self.customers.get(customer_id)

        if customer:
            customer.display()
        else:
            print("Customer not found.")

    # Update Customer
    def update_customer(self):
        customer_id = input("Enter Customer ID to update: ")

        customer = self.customers.get(customer_id)

        if customer:
            customer.name = input("Enter New Name: ")
            customer.email = input("Enter New Email: ")
            customer.phone = input("Enter New Phone: ")

            print("Customer updated successfully.")
        else:
            print("Customer not found.")

    # Delete Customer
    def delete_customer(self):
        customer_id = input("Enter Customer ID to delete: ")

        if customer_id in self.customers:
            del self.customers[customer_id]
            print("Customer deleted successfully.")
        else:
            print("Customer not found.")

    # Menu
    def menu(self):
        while True:
            print("\n========== Customer Management System ==========")
            print("1. Add Customer")
            print("2. View Customers")
            print("3. Search Customer")
            print("4. Update Customer")
            print("5. Delete Customer")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_customer()

            elif choice == "2":
                self.view_customers()

            elif choice == "3":
                self.search_customer()

            elif choice == "4":
                self.update_customer()

            elif choice == "5":
                self.delete_customer()

            elif choice == "6":
                print("Exiting Customer Management System...")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    cms = CustomerManagementSystem()
    cms.menu()