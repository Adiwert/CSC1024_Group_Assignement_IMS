import datetime # add date and time

def add_product():
    # Code to add a product to products.txt
    pass

def update_product():
    # Code to update product details
    pass

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