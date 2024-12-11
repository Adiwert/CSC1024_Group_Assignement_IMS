def add_product():
    # Code to add a product to products.txt
    pass

def update_product():
    # Code to update product details
    pass

def add_supplier():
    # Code to add a supplier to suppliers.txt
    pass

def place_order():
    # Code to place an order
    pass

def view_inventory():
    # Code to view inventory
    pass

def generate_reports():
    # Code to generate reports
    pass

def main_menu():
    while True:
        print("\nInventory Management System")
        print("1. Add a New Product")
        print("2. Update Product Details")
        print("3. Add a New Supplier")
        print("4. Place an Order")
        print("5. View Inventory")
        print("6. Generate Reports")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_product()
        elif choice == '2':
            update_product()
        elif choice == '3':
            add_supplier()
        elif choice == '4':
            place_order()
        elif choice == '5':
            view_inventory()
        elif choice == '6':
            generate_reports()
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")
            print("Hello world!")