def add_product():
    # Code to add a product to products.txt
    pass

def update_product(): ## always check the sticky notes 
    # Code to update product details
    product = []
    try:
        with open('product.txt', 'r') as f:
            lines = f.readlines()
            for line in lines[2:]: # this step to skip header lines
                parts = lines.split('I')
                if len(parts) >= 4:
                    product = {
                        'ID': parts[0].strip(),
                        'Name': parts[1].strip(),
                        'Price': float(parts[2].strip()),
                        'Description': parts[3].strip()
                    }
                    products.append(product)
    except FileNotFoundError:
        print("No products found! Please add a product first. Thank you")
        return
    
    print("Current products: ")
    for product in products:
        print(f"{product['ID']:<10}{product['Name']:<20}{product["price"]:<10}{product['Description']:<40}")
        # to update some specific
        product_id_to_update = input("Please enter the Product ID to update: ")

        for product in products:
            if product['ID'] == product_id_to_update:
                try:
                    new_name = input(f"Enter new name for '{product['Name']}'(or leave blank to keep the current name):") or product['Name']
                    new_price = input(f"Enter new price for '{product['Name']}'(or leave blank to keep the current price):") 
                    new_description = input(f"Enter new description for '{product['Name']}'(or leave blank to keep the current description):") or product['Description']

                    # product detail updated
                    product['Name'] = new_name
                    product['Price'] = new_price
                    product['Description'] = new_description

                    print(f"Product '{product_id_to_update}' are updated successfully.")
                except ValueError: 
                    print("Invalid price entered. Update failed. ")
                break
            else:
                print(f"Product ID '{product_id_to_update}' are not found. ")

                # writing the updated products into the file
                with open('products.txt', 'w') as f:
                    table_header = f"{'ID':<10}{'Name':<20}{'Price':<10}{'Description':<40}\n"
                    table_header += '-' * 80 + '\n'
                    f.write(table_header)

                    for p in products:
                        table_row = f"{p['ID']:<10}{p['Name']:<20}{p['Price']:<10}{p['Description']:<40}\n"
            f.write(table_row)

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