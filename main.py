import datetime # Imports the datetime module to add date/time to details.
from prettytable import PrettyTable # Imports the PrettyTable library for formatted table output.

# Predefined food categories for the user to choose from
PRODUCT_CATEGORIES = [
    "Dairy", "Fruits", "Vagetables", "Poultry", "Seafood", 
    "Beverages", "Bakery", "Snacks", "Frozen", "Grains", "Others"
]

# Function to format names when append it into txt files
def format_name(name):
    words = name.split() # Splits the name into individual words.
    cap_words = [word.capitalize() for word in words] # Capitalizes the first letter of each word.
    formatted_name = '_'.join(cap_words) # Joins the capitalized words with underscores
    
    return formatted_name

# General helper function to get the next ID for any file
def get_next_id(file_name, prefix, column_index):
    column_index = 0
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
        if len(lines) <= 2:
            return f'{prefix}0001'
        
        for line in reversed(line[2:]):
            columns = [column.strip() for column in line.split(", ")]
            last_id = columns[column_index]
            # Skip if ID is '0'
            if last_id == '0':
                continue
            if last_id.startswith(prefix) and len(last_id[1:]) == 4 and last_id[1:].isdigit():
                last_numeric_id = int(last_id[1:])
                next_id = f'{prefix}{last_numeric_id + 1:04d}'
                return next_id
        # If no valid ID is found, return the first ID
        return f'{prefix}0001'
    # If the file does not exist, return the prefix followed by 0001
    except FileNotFoundError:
        return f'{prefix}0001'
    
def valid_suppliers(filename='suppliers.txt'):
    valid_supplier_ids = []
    try:
        with open(filename, "r") as f:
            suppliers = f.readlines()[2:]
        for supplier in suppliers:
            supplier_info = [item.strip() for item in supplier.split(", ")]
            valid_supplier_ids.append(supplier_info[0])
            print(f"{supplier_info[0]} - {supplier_info[1]}")
    except FileNotFoundError:
        print("No suppliers found.")
    
    return valid_supplier_ids

def valid_products(filename='products.txt'):
    valid_product_ids = []
    try:
        with open(filename, "r") as f:
            products = f.readlines()[2:]
        for product in products:
            product_info = [item.strip() for item in product.split(", ")]
            valid_product_ids.append(product_info[0])
            print(f"{product_info[0]} - {product_info[1]}")
    except FileNotFoundError:
        print("No products found.")
        
    return valid_product_ids

# Defines the `add_product` function to add new products to an inventory management system.
def add_product():
    print(r"""
         _       _     _   ____                _            _   
        / \   __| | __| | |  _ \ _ __ ___   __| |_   _  ___| |_ 
       / _ \ / _` |/ _` | | |_) | '__/ _ \ / _` | | | |/ __| __|
      / ___ \ (_| | (_| | |  __/| | | (_) | (_| | |_| | (__| |_ 
     /_/   \_\__,_|\__,_| |_|   |_|  \___/ \__,_|\__,_|\___|\__|
    
    """)
    try:
        with open('products.txt', 'r') as f:
            lines = f.readlines() 
            file_exists = bool(lines)
    except FileNotFoundError:
        file_exists = False

    if not file_exists:
        with open('products.txt', 'w') as f:
            table_header = f"{'ProductID':<10}, {'ProductName':<25}, {'ProductCategory':<15}, {'ProductQuantity':<15}, {'ProductImportPrice':<20}, {'ProductRetailPrice':<20}, {'SupplierID':<10}\n\n"
            f.write(table_header)

    print('Enter product details or "quit" to exit: ')
    
    product_id = get_next_id('products.txt', 'P', 0)
    print(f"Product ID: {product_id}")
    
    while True:
        product_name = input('Product Name: ').strip()
        if product_name.lower() == 'quit':
            return None # Exit the function if the user enters "quit"
        formatted_name = format_name(product_name)
        if formatted_name:
            break
    
    while True:
        print("Available Categories: Dairy, Fruits, Vegetables, Poultry, Seafood, Beverages, Bakery, Snacks, Frozen, Grains, Others")
        product_category = input('Product Category: ').strip().capitalize()
        if product_category.lower() == 'quit':
            return None # Exit the function if the user enters "quit"
        if product_category not in PRODUCT_CATEGORIES:
            print("Invalid category, defaulting to 'Others'.")
            product_category = 'Others'
            break
        else:
            break # Exit loop if valid category is entered

    while True:
        product_quantity = input('Product Quantity: ').strip()
        if product_quantity.lower() == 'quit':
            return None # Exit the function if the user enters "quit"
        try:
            product_quantity = int(product_quantity)
            if product_quantity < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid quantity input.")
    
    while True:
        product_import_price = input('Product Import Price (RM): ').strip()
        if product_import_price.lower() == 'quit':
            return None # Exit the function if the user enters "quit"
        try:
            product_import_price = f"{float(product_import_price):.2f}"
            if product_import_price < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid import price input.")
            
    while True:
        product_retail_price = input('Product Retail Price (RM): ').strip()
        if product_retail_price.lower() == 'quit':
            return None # Exit the function if the user enters "quit"
        try:
            product_retail_price = f"{float(product_retail_price):.2f}"
            if product_retail_price < 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid retail price input.")
    
    print("\nAvailable Suppliers:")
    valid_supplier_ids = valid_suppliers()
    while True:
        try:
            supplier_id = input("Supplier ID (SXXXX): ").strip()
            if supplier_id.lower() == 'quit':
                return None # Exit the function if the user enters "quit"
            if supplier_id in valid_supplier_ids:
                break
            else:
                print("Invalid supplier ID. Please try again.")
        except FileNotFoundError:
            print("No suppliers data available. Please add a supplier first.")
            return None # Exit the function if there is no suppliers data available
    
    with open('products.txt', 'a') as f:
        table = f"{product_id:<10}, {formatted_name:<25}, {product_category:<15}, {product_quantity:<15}, {product_import_price:<20}, {product_retail_price:<20}, {supplier_id:<10}\n"
        f.write(table)
        print(f'{formatted_name} with ID of {product_id} has been added.\n')



def update_product():
    print(r"""
      _   _           _       _         ____                _            _   
     | | | |_ __   __| | __ _| |_ ___  |  _ \ _ __ ___   __| |_   _  ___| |_ 
     | | | | '_ \ / _` |/ _` | __/ _ \ | |_) | '__/ _ \ / _` | | | |/ __| __|
     | |_| | |_) | (_| | (_| | ||  __/ |  __/| | | (_) | (_| | |_| | (__| |_ 
      \___/| .__/ \__,_|\__,_|\__\___| |_|   |_|  \___/ \__,_|\__,_|\___|\__|
           |_|                                                               
    """)
    # Load products
    products = []
    try:
        with open('products.txt', 'r') as f:
            lines = f.readlines()[2:]
            for line in lines:
                if line.strip():
                    fields = [item.strip() for item in line.split(", ")]
                    product = {
                        'ID': fields[0],
                        'Name': fields[1],
                        'Category': fields[2],
                        'Quantity': int(fields[3]),
                        'Import Price': float(fields[4]),
                        'Retail Price': float(fields[5]),
                        'Supplier ID': fields[6]
                    }
                    products.append(product)

    except FileNotFoundError:
        print("No products file found. Please add products first.")
        return
    except IndexError:
        print("Malformed data. Please check the file format.")
        return
    
    print("\nAvailable Products:")
    valid_product_ids = valid_products()

    while True:
        product_id = input('\nEnter product ID to update (or type "quit" to exit): ').strip()
        if product_id.lower() == 'quit':
            return None
        if product_id.strip() in [valid_id.strip() for valid_id in valid_product_ids]:
            break
        else:
            print("Invalid product ID. Please try again.")

    for product in products:
        if product['ID'] == product_id:
            print('Current Product Details:')
            print(f"Name: {product['Name']}")
            print(f"Category: {product['Category']}")
            print(f"Quantity: {product['Quantity']}")
            print(f"Import Price: {product['Import Price']}")
            print(f"Retail Price: {product['Retail Price']}")
            print(f"Supplier ID: {product['Supplier ID']}")
            
            while True:
                new_name = input('Enter new Product Name (Press "Enter" if no updates): ').strip()
                if new_name.lower() == 'quit':
                    return None
                if new_name == '':
                    break
                formatted_name = format_name(new_name)
                product['Name'] = formatted_name
                break

            while True:
                print("Available Categories: Dairy, Fruits, Vegetables, Poultry, Seafood, Beverages, Bakery, Snacks, Frozen, Grains, Others")
                new_category = input('Enter new Product Category (Press "Enter" if no updates): ').strip().capitalize()
                if new_category.lower() == 'quit':
                    return None
                if new_category == '':
                    break
                if new_category: # If the input is empty, keep the current category
                    if new_category not in PRODUCT_CATEGORIES:
                        print("Invalid category, defaulting to 'Others'.")
                        product['Category'] = 'Others'
                    else:
                        product['Category'] = new_category
                break

            while True:
                try:
                    new_quantity = input('Enter new Product Quantity (Press "Enter" if no updates): ').strip()
                    if new_quantity.lower() == 'quit':
                        return None
                    if new_quantity == '':
                        break
                    if new_quantity:
                        product['Quantity'] = int(new_quantity)
                        if product['Quantity'] < 0:
                            raise ValueError
                        break
                except ValueError:
                    print('Invalid quantity entered. Keeping the old quantity.')
            
            while True:
                try:
                    new_import_price = input('Enter new Product Price (Press "Enter" if no updates): ').strip()
                    if new_import_price.lower() == 'quit':
                        return None
                    if new_import_price == '':
                        break
                    if new_import_price:  
                        product['Import Price'] = f"{float(new_import_price):.2f}"
                        if product['Import Price'] < 0:
                            raise ValueError
                        break
                except ValueError:
                    print('Invalid import price entered. Keeping the old import price.')
                    
            while True:
                try:
                    new_retail_price = input('Enter new Product Retail Price (Press "Enter" if no updates): ').strip()
                    if new_retail_price.lower() == 'quit':
                        return None
                    if new_retail_price == '':
                        break
                    if new_retail_price:
                        product['Retail Price'] = f"{float(new_retail_price):.2f}"
                        if product['Retail Price'] < 0:
                            raise ValueError
                        break
                except ValueError:
                    print('Invalid retail price entered. Keeping the old retail price.')

            print("\nAvailable Suppliers:")
            valid_supplier_ids = valid_suppliers()
            while True:
                try:
                    new_supplier_id = input('Enter new Supplier ID (Press "Enter" if no updates): ').strip()
                    if new_supplier_id.lower() == 'quit':
                        return None
                    if new_supplier_id == '':
                        break
                    if new_supplier_id in valid_supplier_ids:
                        product['Supplier ID'] = new_supplier_id
                        break
                    else:
                        print("Invalid Supplier ID. Please try again.")
                except FileNotFoundError:
                    print("No suppliers data available. Please add a supplier first.")
                    return None # Exit the function if there is no suppliers data available
            
            print('Product successfully updated.')
            break
    else:
        print('Invalid Product ID.')
        return None
    
    with open('products.txt', 'w') as f:
        table_header = f"{'ProductID':<10}, {'ProductName':<25}, {'ProductCategory':<15}, {'ProductQuantity':<15}, {'ProductImportPrice':<20}, {'ProductRetailPrice':<20}, {'SupplierID':<10}\n\n"
        f.write(table_header)
        for product in products:
            table = f"{product['ID']:<10}, {product['Name']:<25}, {product['Category']:<15}, {product['Quantity']:<15}, {product['Import Price']:<20}, {product['Retail Price']:<20}, {product['Supplier ID']:<10}\n"
            f.write(table)
    
    print(f"Product with ID {product_id} has been successfully updated.")



def add_supplier():
    print(r"""
         _       _     _   ____                    _ _           
        / \   __| | __| | / ___| _   _ _ __  _ __ | (_) ___ _ __ 
       / _ \ / _` |/ _` | \___ \| | | | '_ \| '_ \| | |/ _ \ '__|
      / ___ \ (_| | (_| |  ___) | |_| | |_) | |_) | | |  __/ |   
     /_/   \_\__,_|\__,_| |____/ \__,_| .__/| .__/|_|_|\___|_|   
                                      |_|   |_|                  
    """)
    # Code to add a supplier to suppliers.txt
    try:
        with open('suppliers.txt', 'r') as f:
            lines = f.readlines()
            file_exists = bool(lines)
    except FileNotFoundError:
        file_exists = False

    if not file_exists:
        with open('suppliers.txt', 'w') as f:
            table_header = f"{'SupplierID':<10}, {'SupplierName':<30}, {'ProductCategory':<15}, {'ContactNumber':<15}\n\n"
            f.write(table_header)

    print('Enter supplier details or "quit" to exit: ')

    supplier_id = get_next_id('suppliers.txt', 'S', 0)
    print(f"Supplier ID: {supplier_id}")
    
    while True:
        supplier_name = input('Supplier Name: ').strip()
        if supplier_name.lower() == 'quit':
            return None # Exit the function if the user enters "quit"
        formatted_name = format_name(supplier_name)
        if formatted_name:
            break
    
    while True:
        print("Available Categories: Dairy, Fruits, Vegetables, Poultry, Seafood, Beverages, Bakery, Snacks, Frozen, Grains, Others")
        product_category = input('Product Category: ').strip().capitalize()
        if product_category.lower() == 'quit':
            return None # Exit the function if the user enters "quit"
        if product_category not in PRODUCT_CATEGORIES:
            print("Invalid category, defaulting to 'Others'.")
            product_category = 'Others'
            break
        else:
            break # Exit loop if valid category is entered

    while True:
        contact_number = input('Enter Contact Number (format 01x-xxxxxxxx): ').strip()
        if contact_number.lower() == 'quit':
            return None # Exit the function if the user enters "quit"
        if len(contact_number) not in [11, 12]:
            print("Invalid contact number. Please try again.")
            continue
        if contact_number[:2] != '01' or contact_number[3] != '-':
            print("Invalid contact number. Please try again.")
            continue
        if not contact_number[2:3].isdigit() or not contact_number[4:].isdigit():
            print("Invalid contact number. Please try again.")
            continue
        break # Exit loop if valid contact number is entered

    with open('suppliers.txt', 'a') as f:
        table = f"{supplier_id:<10}, {formatted_name:<30}, {product_category:<15}, {contact_number:<15}\n"
        f.write(table)
        print(f'{formatted_name} with ID of {supplier_id} has been added.\n')



def place_order():
    print(r"""
      ____  _                   ___          _           
     |  _ \| | __ _  ___ ___   / _ \ _ __ __| | ___ _ __ 
     | |_) | |/ _` |/ __/ _ \ | | | | '__/ _` |/ _ \ '__|
     |  __/| | (_| | (_|  __/ | |_| | | | (_| |  __/ |   
     |_|   |_|\__,_|\___\___|  \___/|_|  \__,_|\___|_|   
    
    """)
    # Code to place an order
    
    # Check if the orders.txt exists and create it if not
    try:
        with open('orders.txt', 'r') as f:
            lines = f.readlines()
            file_exists = bool(lines)
    except FileNotFoundError:
        file_exists = False
    
    if not file_exists:
        with open('orders.txt', 'w') as f:
            table_header = f"{'OutgoingOrderID':<15}, {'IncomingOrderID':<15}, {'ProductID':<10}, {'ImportPrice':<12}, {'RetailPrice':<12}, {'OrderStatus':<12}, {'SupplierID':<10}, {'OrderDate':<10}\n\n"
            f.write(table_header)

    # Display mini menu for order type
    while True:
        print("\nMini Menu for Placing Order")
        print("[1] Place Order to Supplier (Add stock)")
        print("[2] Place Order from Customer (Sell product)")
        print("[3] Back to Main Menu")
    
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice == '3':
            return None
        if choice not in ['1', '2']:
            print("Invalid choice. Please try again.")
            continue
            
        print("\nAvailable Products:")
        valid_product_ids = valid_products()
        if not valid_product_ids:
            print("No valid products found. Please add products first.")
            return None
        
        while True:
            product_id = input("\nEnter Product ID: ").strip()
            if product_id.lower() == 'quit':
                return None
            if product_id.strip() in [valid_id.strip() for valid_id in valid_product_ids]:
                break
            else:
                print("Invalid Product ID. Please try again.")
        
        while True:
            try:
                quantity = input("Enter incoming or outgoing quantity: ").strip()
                if quantity.lower() == 'quit':
                    return None
                quantity = int(quantity)
                if quantity <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Invalid quantity. Please enter a positive integer.")
        
        if choice == '1':
            outgoing_order_id = '0'
            incoming_order_id = get_next_id('orders.txt', 'I', 1)
            
            print("\nAvailable Suppliers:")
            valid_supplier_ids = valid_suppliers()
            while True:
                supplier_id = input("\nEnter Supplier ID: ").strip()
                if supplier_id.lower() == 'quit':
                    return None
                if supplier_id.strip() in [valid_id.strip() for valid_id in valid_supplier_ids]:
                    break
                else:
                    print("Invalid Supplier ID. Please try again.")
            
            with open('products.txt', 'r') as f:
                products = f.readlines()
                for product in products:
                    if product.strip():
                        fields = [item.strip() for item in product.split(", ")]
                        if fields[0] == product_id:
                            import_price = float(fields[4])
                            retail_price = 0 # Not applicable for supplier orders
                            break
            
            order_status = f"+{quantity}"
        
        elif choice == '2':
            outgoing_order_id = get_next_id('orders.txt', 'O', 0)
            incoming_order_id = '0'
            
            with open('products.txt', 'r') as f:
                products = f.readlines()
                for product in products:
                    if product.strip():
                        fields = [item.strip() for item in product.split(", ")]
                        if fields[0] == product_id:
                            import_price = 0 # Not applicable for supplier orders
                            retail_price = float(fields[5])
                            break
                        
            order_status = f"-{quantity}"
    
        order_date = datetime.datetime.now().strftime("%d-%m-%Y")
        
        with open('orders.txt', 'a') as f:
            table = f"{outgoing_order_id:<15}, {incoming_order_id:<15}, {product_id:<10}, {import_price:<12}, {retail_price:<12}, {order_status:<10}, {quantity:<10}, {order_date:<10}\n"
            f.write(table)
        
        updated_products_with_new_quantity = []
        with open('products.txt', 'r') as f:
            header = f.readline()
            blank_line = f.readline()
            for line in f:
                fields = [item.strip() for item in line.split(", ")]
                if fields[0] == product_id:
                    current_quantity = int(fields[3])
                    if choice == '1':
                        new_quantity = current_quantity + quantity
                    elif choice == '2':
                        new_quantity = current_quantity - quantity
                    fields[3] = int(new_quantity)
                updated_products_with_new_quantity.append(fields)
        
        with open('products.txt', 'w') as f:
            f.write(header)
            f.write(blank_line)
            for product in updated_products_with_new_quantity:
                table = f"{product[0]:<10}, {product[1]:<25}, {product[2]:<15}, {product[3]:<15}, {product[4]:<20}, {product[5]:<20}, {product[6]:<10}\n"
                f.write(table)
        
        if choice == '1':
            order_id = incoming_order_id
            quantity_change = f"increased by {quantity}"
        elif choice == '2':
            order_id = outgoing_order_id
            quantity_change = f"decreased by {quantity}"
        
        print(f"\nOrder {order_id} has been placed successfully!")
        print(f"Quantity of {product_id} has been {quantity_change}.")
        
        break

def view_inventory():
    print(r"""
     __     ___                 ___                      _                   
     \ \   / (_) _____      __ |_ _|_ ____   _____ _ __ | |_ ___  _ __ _   _ 
      \ \ / /| |/ _ \ \ /\ / /  | || '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |
       \ V / | |  __/\ V  V /   | || | | \ V /  __/ | | | || (_) | |  | |_| |
        \_/  |_|\___| \_/\_/   |___|_| |_|\_/ \___|_| |_|\__\___/|_|   \__, |
                                                                       |___/ 
    """)
    try:
        with open("products.txt",'r') as file:
            lines = file.readlines()

            if len(lines) <= 2:
                print("The inventory is currently empty. Add some products first")
                return

            print("\n-- Inventroy List --\n")
            for line in lines:
                print(line, end="")
            print("\n-------------------")

    except FileNotFoundError:
        print("\nError: The file does not exist. add product to create the file ")

    pass

def generate_reports():
    print(r"""
       ____                           _              ____                       _       
      / ___| ___ _ __   ___ _ __ __ _| |_ ___  ___  |  _ \ ___ _ __   ___  _ __| |_ ___ 
     | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \/ __| | |_) / _ \ '_ \ / _ \| '__| __/ __|
     | |_| |  __/ | | |  __/ | | (_| | ||  __/\__ \ |  _ <  __/ |_) | (_) | |  | |_\__ \
      \____|\___|_| |_|\___|_|  \__,_|\__\___||___/ |_| \_\___| .__/ \___/|_|   \__|___/
                                                              |_|                       
    """)
    # Code to generate reports
    try:
        with open("products.txt",'r') as file :
            lines = file.readlines()

            if len(lines) <=2: #checking the inventory
                print("\nThe inventory is empty. Report are unable to be generated")
                return 

            total_product = 0
            total_value = 0.0
            low_stock = 20
            low_stock = []
            supplier_order = []

            table = PrettyTable()
            table.field_names = ["Product ID","Product Name","Price","Quantity"]


            for line in lines[2:]:
                    if line.strip():
                        product_id = line[0:10].strip()
                        product_name = line[10:30].strip()
                        quantity = int(line[30:35].strip())
                        price = float(line[35:45].strip())
                        total_product += 1
                        
                        total_value += price * quantity

                        table.add_row([product_id, product_name, quantity, f"${price:.2f}"])

                        if quantity < low_stock:
                            low_stock.append(product_name)
                            supplier_order.append ((product_name, low_stock - quantity))

            print("\n-- Inventory Report --\n")
            print(table)
            print(f"The total products: {total_product}")
            print(f"The total value of products: {total_value:.2f}")

            if low_stock:
                    print("\n-- Low Stock! --")
                    print("The products that are low stock: ")
                    for product in low_stock:
                        print(f"-{product}")

            if supplier_order :
                    print("\n-- Supplier Order --")
                    print("\n Products that need to be ordered:")
                    for product, order_quantity in supplier_order:
                        print(f" -{product}: Order {order_quantity} more units")

        with open("order.txt","r") as order_file, open("supplier.txt","r") as supplier_file:
            order_line = order_file.readlines()
            supplier_lines = supplier_file.readlines()

            total_sales = sum(float(line.strip().split()[1]) for line in order_line if line.strip())
            total_supplier_cost = sum(float(line.strip().split()[1]) for line in supplier_lines if line.strip())

            profit = total_sales - total_supplier_cost
            print(f"\n-- The profit summary --")
            print(f"Total sales : ${total_sales:.2f}")
            print(f"Total supplier cost : ${total_supplier_cost:.2f}")
            print(f"Profit : ${profit:.2f}")

    except FileNotFoundError:
                print("\nError: the product does not exist. Add the product first\n")

    except FileNotFoundError:
                print("Invalid input. Try again")
                
    pass


def main_menu():
    print(r"""                                                                                                                                                                                   
                                ██████████████████████████████████████████████████████                                                                  
                                █████████████        ████████████         ████████████                                                                  
                                █████████████████████████████████    █████████████████                                                                  
                                   █████████████        █████████████          █████████████                                                                
                             ██████████████         ██████████████          █████████████                                                               
                            ██████████████          ██████████████           ██████████████                                                             
                          ███████████████          ███████████████            ███████████████                                                           
                        ████████████████           ████████████████            ███████████████                                                          
                       ███████████████████████████████████████████████   ████  █████████████████                                                        
                       ████████████████            ████████████████             ████████████████                                                        
                       ██  ████████████            ████████████████             ████████████████                                                        
                       ██  ████████████            ████████████████             ███████████████      █████████                                          
                       ███  ████████████          ██████████████████           ████████████████    ████████████                                         
                        ████  █  ████ ████      ███  █████████████ ██        ███ █████████████    ███  █████████                                        
                          █████████     █████████      █████████     █████████     █████████      ███ ███████████                                       
                          ██                                                              ██     ████  ██████████                                       
                          ██████████████████████████████████████████████████████████████████    ███   █████████████                                     
                          ██████████████      ████████          ██████████    ██████████████   ███  ███████████████                                     
                          ██                   ███████          ██   ███         ████     ██  ██████████████████████                                    
                          ██   █              ████████          ██  ██             █████████  ███  █████████████████                                    
                            ██              ███████ ██          ████              ███████ ██  ███ ██████████████████                                    
                          ██              ███████   ██          ██              ███████   ██   █████████████████████                                    
                          ██             ██████     ██          ██            ███████     ██    ███████████████████                                     
                          ██           ██████      ███          ██           ██████     ████     █████████████████                                      
                          ██         ██████      █████          ██         ██████      █████       █████████████                                        
                          ███  ███████████████████████          ███  ██████████████████████           █████                                            
                          ██                        ██          ██                        ██            ██                                              
        ████ ███ ████     ██                        ██          ██                        ██            ██                                              
        █ ████ ███ ██     ██                        ██          ██                        ██            ██                                              
        █ ████ ███ ███████████████████████████████████████████████████████████████████████████████████████                                            
    ___________________________________________________________________________________________________________________
                                      ___                      _                   
                                     |_ _|_ ____   _____ _ __ | |_ ___  _ __ _   _ 
                                      | || '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |
                                      | || | | \ V /  __/ | | | || (_) | |  | |_| |
                                     |___|_| |_|\_/ \___|_| |_|\__\___/|_|   \__, |
                                        __  __                               |___/ 
                                       |  \/  | __ _ _ __   __ _  __ _  ___ _ __     
                                       | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|    
                                       | |  | | (_| | | | | (_| | (_| |  __/ |       
                                       |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|       
                                                                 |___/        
    ____________________________________________________________________________________________________________________
    """)
    while True:
        print("\nMain Menu")
        print("[1] Add a New Product")
        print("[2] Update Product Details")
        print("[3] Add a New Supplier")
        print("[4] Place an Order")
        print("[5] View Inventory")
        print("[6] Generate Reports")
        print("[7] Exit")

        choice = input("Enter your choice (1-7): ")
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
            print(r"""
                  ____             __   __               _               _       _ 
                 / ___|  ___  ___  \ \ / /__  _   _     / \   __ _  __ _(_)_ __ | |
                 \___ \ / _ \/ _ \  \ V / _ \| | | |   / _ \ / _` |/ _` | | '_ \| |
                  ___) |  __/  __/   | | (_) | |_| |  / ___ \ (_| | (_| | | | | |_|
                 |____/ \___|\___|   |_|\___/ \__,_| /_/   \_\__, |\__,_|_|_| |_(_)
                                                             |___/                 
            """)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()