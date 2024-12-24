import datetime # add date and time
from prettytable import PrettyTable 

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
    # Load existing suppliers (optional, for validation or display purposes)
    suppliers = {}
    try:
        with open('suppliers.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:  # Assuming format: SupplierID,SupplierName,ContactDetails
                    supplier_id, name, contact_info = parts[0], parts[1], parts[2]
                    suppliers[supplier_id] = {'Name': name, 'Contact Info': contact_info}
    except FileNotFoundError:
        print("suppliers.txt not found. Starting with an empty supplier list.")
    except Exception as e:
        print(f"Error reading suppliers.txt: {e}")
        return
    
    # Add new suppliers
    with open('suplliers.txt', 'a') as f: # Append mode
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

                # Generate a new Supplier ID
                new_supplier_id = f"S{len(suppliers) + 1:04d}"  # Example: S0001, S0002

                # Append to file
                supplier_entry = f"{new_supplier_id},{supplier_name},{contact_info}\n"
                f.write(supplier_entry)

                # Update in-memory list
                suppliers[new_supplier_id] = {'Name': supplier_name, 'Contact Info': contact_info}

                print(f"Supplier added successfully:\n"
                      f"Supplier ID: {new_supplier_id}\nName: {supplier_name}\nContact Info: {contact_info}\n")
                
            except Exception as e:
                print(f"An error occured: {e}")

def place_order():
    # Code to place an order
    # Load product data from products.txt
    product_stock = {}
    try:
        with open('products.txt', 'r') as prod_file:
            for line in prod_file:
                parts = line.strip().split(',')
                if len(parts) == 2:  # Assuming the file format is "ProductName,Quantity"
                    product_name, quantity = parts[0].strip(), parts[1].strip()
                    product_stock[product_name] = int(quantity)
    except FileNotFoundError:
        print("products.txt not found. Starting with an empty stock.")
    except Exception as e:
        print(f"Error reading products.txt: {e}")
        return
    
    # Load supplier data from suppliers.txt
    suppliers = {}
    try:
        with open('suppliers.txt', 'r') as sup_file:
            for line in sup_file:
                parts = line.strip().split(',')
                if len(parts) == 3:  # Format: SupplierID,SupplierName,ContactDetails
                    supplier_id, supplier_name, contact = parts[0], parts[1], parts[2]
                    suppliers[supplier_id] = {'SupplierName': supplier_name, 'ContactDetails': contact}
    except FileNotFoundError:
        print("suppliers.txt not found. Starting with an empty supplier list.")
        return
    except Exception as e:
        print(f"Error reading suppliers.txt: {e}")
        return
    
    # Append new orders to orders.txt
    try:
        with open('orders.txt', 'a') as f:
            print('Enter order details or "done" to exit:\n')

            while True:
                try:
                    # Validate Product ID
                    product_id = input('Product ID: ').strip()
                    if product_id.lower() == 'done':
                        break
                    if product_id not in product_stock:
                        print("Invalid Product ID. Please try again.")
                        continue

                    # Validate Quantity
                    quantity = input('Quantity: ').strip()
                    if not quantity.isdigit() or int(quantity) <= 0:
                        print("Quantity must be a valid positive number. Please try again.")
                        continue
                    quantity = int(quantity)

                    # Validate Supplier ID
                    supplier_id = input('Supplier ID: ').strip()
                    if supplier_id not in suppliers:
                        print("Invalid Supplier ID. Please try again.")
                        continue

                    # Calculate Quantity Change from products.txt data
                    previous_quantity = product_stock.get(product_name, 0)  # Default to 0 if not present
                    quantity_change = quantity - previous_quantity
                    product_stock[product_name] = quantity  # Update stock for future calculations

                    # Generate Order ID and Order Date
                    order_id = f"O{len(product_stock):04d}"  # Example: O0001, O0002
                    order_date = datetime.datetime.now().strftime('%Y-%m-%d')

                    # Write to orders.txt
                    order_entry = f"{order_id},{product_id},{quantity},{order_date},{supplier_id}\n"
                    f.write(order_entry)

                    # Display confirmation
                    print(f"Order placed successfully:\n"
                          f"Order ID: {order_id}\nProduct: {product_stock[product_id]['ProductName']}\n"
                          f"Quantity: {quantity}\nQuantity Change: {quantity_change}\n"
                          f"Supplier: {suppliers[supplier_id]['SupplierName']}\nDate: {order_date}\n")
                except Exception as e:
                    print(f"An error occurred while placing the order: {e}")
    except FileNotFoundError:
        print("orders.txt not found. Creating a new file...")
        open('orders.txt', 'w').close()
    except Exception as e:
        print(f"Error accessing orders.txt: {e}")

    # Update products.txt with the new quantities
    try:
        with open('products.txt', 'w') as prod_file:
            for product_id, details in product_stock.items():
                prod_file.write(f"{product_id},{details['ProductName']},{details['Quantity']}\n")
    except Exception as e:
        print(f"Error updating products.txt: {e}")

def view_inventory():
    try:
        with open("product.txt",'r') as file:
            lines = file.readlines()

            if len(lines) <= 2:
                print("The inventory is currently empty. Add some products first.")
                return

            print("\n-- Inventroy List --\n")
            for line in lines:
                print(line, end="")
            print("\n-------------------")

    except FileNotFoundError:
        print("\nError: The file does not exist. add product to create the file ")

    pass

def generate_reports():
    # Code to generate reports
    try:
        with open("product.txt",'r') as file :
            lines = file.readlines()

            if len(lines) <=2:
                print("\nThe inventory is empty. Report are unable to be generated")
                return

                total_product = 0
                total_value = 0.0

                for line in lines[2:]:
                    if line.strip():
                        total_product += 1
                        price = float(line[30:40].strip())
                        total_value += price

                print("\n-- Inventory Report --\n")
                print(f"The total products: {total_product}")
                print(f"The total value of products: {total_value:.2f}")
           
    except FileNotFoundError:
                print("\nError: the product does not exist. Add the product first\n")
           
    except FileNotFoundError:
                print("Invalid input. Try again")        
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