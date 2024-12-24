import datetime # to add date and probably time inside the order file

def add_product():
    # Code to add a product to products.txt
    pass

def update_product():
    # Code to update product details
    pass

def add_supplier():
    # Code to add a supplier to suppliers.txt
    import re # module for pattern matching and manipulation (validation)

    # Supplier categories
    categories = [
        "dairy", "fruits", "vegetables", "poultry", "seafood",
        "beverages", "bakery", "snacks", "condiments", "grains"
        ]
    
    # Load suppliers file
    suppliers = {} # Initialise dictionary to hold data, key is SupplierID
    try:
        with open('suppliers.txt', 'r') as f:
            for line in f:
                parts = line.strip().split(', ') #  remove spaces, and split the content with ','
                if len(parts) == 4: # follows the columns contents
                    supplier_id = parts[0] # parts[0] is the SupplierID (key)
                    suppliers[supplier_id] = line.strip()
    except FileNotFoundError:
        print("suppliers.txt not found.")
    except Exception as e:
        print(f"Error reading suppliers.txt: {e}")
        return

    # Add new supplier
    with open('suppliers.txt', 'a') as f:
        print('Enter supplier details or "done" to exit:\n')

        while True:
            try:
                # Display product categories
                print(f"Product Catehories: {', '.join(categories)}")

                # Validate product category
                product_category = input("Enter Product Category: ").strip().lower()
                if product_category.lower() == 'done':
                    break
                if product_category not in categories:
                    print(f"Invalid category. Choose one from {', '.join(categories)}.")
                    continue

                # Validate contact number
                contact_number = input('Enter Contact Number (format 01x-xxxxxxxx): ').strip()
                if not re.match(r"^01[0-9]-\d{7,8}$", contact_number): # Check if input follow the format
                    print("Invalid contact number. Please follow the format 01x-xxxxxxxx.")
                    continue

                # Validate supplier name
                supplier_name = input('Enter Supplier Name: ').strip()
                if not supplier_name:
                    print("Please enter supplier name.")
                    continue
                if " " in supplier_name: # Change the space to '_' if have space
                    supplier_name = supplier_name.replace(" ","_")
                
                # Generate Supplier ID
                new_supplier_id = f"S{len(suppliers) + 1:04d}" # Auto generate ID eg. S0003

                # Append file
                supplier_entry = f"{new_supplier_id}, {supplier_name}, {product_category}, {contact_number}\n"
                f.write(supplier_entry)

                # Update in-memory list for future reference (ID)
                suppliers[new_supplier_id] = supplier_entry.strip()

                # Display update status
                print(f"Supplier added successfully:\n"
                      f"Supplier ID: {new_supplier_id}\nCategory: {product_category}\n"
                      f"Contact Number: {contact_number}\nName: {supplier_name}\n")
            
            except Exception as e:
                print(f"An error occured: {e}")

def place_order():
    # Code to place an order
    # Initialise products dictionary
    products = {} # Initialise to hold data, the key is Product ID

    # Load products from products.txt
    with open('products.txt', 'r') as f:
        for line in f.readlines()[1:]: # Skip header
            product_data = line.strip().split(", ") # remove space and split content using ','
            product_id = product_data[0]
            product_name = product_data[1]
            product_category = product_data[2]
            quantity = product_data[3]
            incoming_price = float(product_data[4])
            selling_price = float(product_data[5])
            supplier_id = product_data[6]
            products[product_id] = {
                'product_name': product_name,
                'product_category': product_category,
                'quantity': quantity,
                'incoming_price': incoming_price,
                'selling_price': selling_price,
                'supplier_id': supplier_id
            }

    # Load existing orders from orders.txt
    orders = []
    with open('orders.txt', 'r') as f:
        orders = f.readlines()

    # Display mini menu for order type
    print("Welcome to Order Management System!")
    print("Please choose your order type: ")
    print("1 Place Order to Supplier (Add stock)")
    print("2 Place Order by Customer (Sell product)")
    order_type_choice = input("Option (1 or 2): ").strip()

    # check input response
    if order_type_choice == '1':
        order_type = 'supplier'
    elif order_type_choice == '2':
        order_type = 'customer'
    else:
        print("Invalid choice.")
        return
    
    # Get product information
    print("Available products:")
    for product_id, details in products.items():
        print(f"Product ID: {product_id}, Product Name: {details['product_name']}, Quantity: {details['quantity']}, "
              f"Category: {details['product_category']}, Incoming Price: {details['incoming_price']}, "
              f"Selling Price: {details['selling_price']}")
        
    # Prompt to enter Product ID
    product_id = input("Enter Product ID: ").strip()

    # Check if Product ID exists
    if product_id not in products:
        print("Invalid Product ID. Exiting...")
        return
    
    # Prompt to enter quantity
    quantity = input("Enter quantity: ").strip()
    if not quantity.isdigit() or int(quantity) <= 0:
        print("Invalid quantity. Exiting...")
        return
    quantity = int(quantity)

    # Generate Order ID
    order_prefix = 'O' if order_type == 'customer' else 'I'
    order_id_prefix = f"{order_prefix}0000"

    # Check the last ID
    last_order_id = 0
    for order in orders:
        if order.startswith(order_id_prefix):
            order_number = int(order[1:])
            if order_number > last_order_id:
                last_order_id = order_number
    
    new_order_id = last_order_id + 1
    new_order_id = f"{order_prefix}{new_order_id:04d}"

    # Get current date (format DD-MM-YYYY)
    order_date = datetime.datetime.now().strftime("%d-%m-#y")

    # Determine status and prices based on order type
    if order_type == 'supplier':
        status = f"+{quantity}" # Add stock
        incoming_price = products[product_id]['incoming_price'] * quantity
        selling_price = 0 # Not relevant
        supplier_id = input("Enter Supplier ID: ").strip()
    else:
        status = f"-{quantity}" # Sell product
        incoming_price = 0 # Not relevant
        selling_price = products[product_id]['selling_price'] * quantity
        supplier_id = '' # Not relevant

    # Prepare order data for the file
    order_data = f"{new_order_id}, {product_id}, {incoming_price:.2f}, {selling_price:.2f}, {status}, {supplier_id}, {order_date}\n"

    # Append new order to orders.txt
    with open('orders.txt', 'a') as f:
        f.write(order_data)
    
    # Update quantity in products.txt
    if order_type == 'supplier':
        products[product_id]['quantity'] += quantity
    else:
        products[product_id]['quantity'] -= quantity

    # Rewrite updated product data to products.txt
    with open('products.txt', 'w') as f:
        f.write("Product ID, Product Name, Product Category, Quantity, Incoming Price, Selling Price, Supplier ID\n")
        for product_id, details in products.items():
            product_line = f"{product_id}, {details['product_name']}, {details['product_category']}, {details['quantity']}, {details['incoming_price']:.2f}, {details['selling_price']:.2f}, {details['supplier_id']}\n"
            f.write(product_line)

    # Display update message
    print(f"Order {new_order_id} placed successfully!")

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

if __name__ == "__main__":
    add_supplier()
    place_order()