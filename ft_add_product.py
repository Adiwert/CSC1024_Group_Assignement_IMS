from utils import PRODUCT_CATEGORIES, format_name, get_next_id, valid_suppliers
from termcolor import colored

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

    print('Enter product details (or "quit" to exit): ')
    
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
            print(colored("Invalid category. Defaulting to 'Others'.", "yellow"))
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
            print(colored("Invalid quantity. Enter a positive integer.", "red"))
    
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
            print(colored("Invalid import price. Enter a valid number.", "red"))
            
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
            print(colored("Invalid retail price. Enter a valid number.", "red"))
    
    print(colored("\nAvailable Suppliers:", "cyan"))
    valid_supplier_ids = valid_suppliers()
    while True:
        try:
            supplier_id = input("Supplier ID (SXXXX): ").strip()
            if supplier_id.lower() == 'quit':
                return None # Exit the function if the user enters "quit"
            if supplier_id in valid_supplier_ids:
                break
            else:
                print(colored("Invalid supplier ID. Try again.", "red"))
        except FileNotFoundError:
            print(colored("No suppliers data available. Please add a supplier first.", "red"))
            return None # Exit the function if there is no suppliers data available
    
    with open('products.txt', 'a') as f:
        table = f"{product_id:<10}, {formatted_name:<25}, {product_category:<15}, {product_quantity:<15}, {product_import_price:<20}, {product_retail_price:<20}, {supplier_id:<10}\n"
        f.write(table)
    print(colored(f"{formatted_name} with ID {product_id} has been added.", "green"))