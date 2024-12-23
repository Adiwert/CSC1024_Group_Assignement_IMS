def add_product():
    # Code to add a product to products.txt
    pass

def update_product():
    # Code to update product details
    pass

def add_supplier():
    # Code to add a supplier to suppliers.txt
    suppliers = []
    table_header = f"{'Suppliers Name':<20}{'Contact Info':<30}{'Product Category':<40}\n"
    table_header += '-' * 90 + '\n'

    with open('suplliers.txt', 'w') as f:
        f.write(table_header)
        print('Enter supplier details or "done" to exit the:\n')

        while True:
            try:
                # Validate supplier name
                supplier_name = input('Supplier Name: ').strip()
                if supplier_name.lower() == 'done':
                    break
                if not supplier_name:
                    print ("Supplier name cannot be empty. Please try again.")
                    continue

                # Validate contact info
                contact_info = input('Contact Info (email/phone): ').strip()
                if not contact_info:
                    print ("Contact info cannot be empty. Please try again.")
                    continue

                # Validate product supplied
                product_category = input('Product Catgory: ').strip()
                if not product_category:
                    print("Product category cannot be empty. Please try again.")
                    continue

                # Append to list and file
                supplier = {
                    'Name': supplier_name,
                    'Contact Info': contact_info,
                    'Product Category': product_category
                } 

                suppliers.append(supplier)

                table = f"{supplier_name:<20}{contact_info:<30}{product_category:<40}\n"
                f.write(table)
                print('supplier added\n')
            except Exception as e:
                print(f"An error occured: {e}")

    pass

def place_order():
    # Code to place an order
    orders = []
    table_header = f"{'Product Name':<20}{'Quantity':<10}{'Supplier Name':<20}\n"
    table_header += '-' * 60 + '\n'

    with open('orders.txt','w') as f:
        f.write(table_header)
        print('Enter order details or "done" ro exit:\n')

        while True:
            try:
                # Validate product name
                product_name = input('Product Name: ').strip()
                if product_name.lower() == 'done':
                    break
                if not product_name:
                    print("Product name cannot be empty. Please try again.")
                    continue

                # Validate quantity
                quantity = input('Quantity: ').strip()
                if not quantity.isdigit() or int(quantity) <= 0:
                    print("Quantity must be a valid number. Please try again.")
                    continue
                quantity = int(quantity)

                # Validate supplier name
                supplier_name = input('Supplier Name: ').strip()
                if not supplier_name:
                    print("Supplier name cannot be empty. Please try again.")
                    continue

                # Append to list and file
                order = {
                    'Product Name': product_name,
                    'Quantity': quantity,
                    'Supplier Name': supplier_name
                }

                orders.append(order)

                table = f"{product_name:<20}{quantity:<10}{supplier_name:<20}\n"
                f.write(table)
                print('Order placed\n')
            except Exception as e:
                print(f"An error occured: {e}")
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