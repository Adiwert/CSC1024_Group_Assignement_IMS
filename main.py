def add_product():
    # Code to add a product to products.txt
    products = []
    table_header = f"{'ID':<10}{'Name':<20}{'Price':<10}{'Desccription':<40}\n"
    table_header += '-' * 80 + '\n'
    
    with open('products.txt', 'w') as f:
        f.write(table_header)
        print('Enter product details or "done" to exit: ')

        while True:
            try:
                product_id = input('Product ID: ')
                if product_id.lower().strip() == 'done':
                    break
                product_name = input('Product Name: ')
                product_price = float(input('Product Price: '))
                product_desc = input('Product Description: ')

                product = {
                    'ID': product_id,
                    'Name': product_name,
                    'Price': product_price,
                    'Description': product_desc
                }

                products.append(product)

                table = f'{product_id:<10}{product_name:<20}{product_price:<10}{product_desc:<40}\n'
                f.write(table)
                print('Product added \n')

            except ValueError:
                print('Please check the details for typo.')
                return


def update_product():
    # Code to update product details:
    products = []

    try:
        with open('products.txt','r') as f:
            lines = f.readlines()

        for line in lines[2:]:
            if line.strip():
                product_id = line[:10].strip()
                product_name = line[10:30].strip()
                product_price = line[30:40].strip()
                product_description = line[40:].strip()

                product = {
                    'ID': product_id,
                    'Name': product_name,
                    'Price': float(product_price) if product_price else 0,
                    'Description': product_description
                }
                products.append(product)

    except FileNotFoundError:
        print("No products file found. Please add products first.")
        return
            
    product_id = input('\nEnter product ID to update: ').strip().lower()
    for product in products:
        if product ['ID'].lower() == product_id:
            print('Current Product Details: ')
            print(f"Name: {product['Name']}, Price: {product['Price']}, Description: {product['Description']}")

            product['Name'] = input('Enter new Product Name (skip if no updates): ')
            try:
                price_input = input('Enter new Product Price (skip if no updates): ')
                if price_input:
                    product['Price'] = float(price_input)
            except ValueError:
                print('Enter a valid price')
            product['Description'] = input('Enter new Product Description (skip if no updates): ')

            print('Succesfully Updated Product')
            break
    else:
        print('Invalid Product ID')
        return
    
    with open('products.txt', 'w') as f:
        table_header = f"{'ID':<10}{'Name':<20}{'Price':<10}{'Description':<40}\n"
        table_header += "-" * 80 + "\n"
        f.write(table_header)
        for product in products:
            table = f"{product['ID']:<10}{product['Name']:<20}{product['Price']:<10}{product['Description']:<40}\n"
            f.write(table)


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

main_menu()