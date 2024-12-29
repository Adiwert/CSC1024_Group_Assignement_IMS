# Import necessary functions and variables
from utils import PRODUCT_CATEGORIES, format_name, get_next_id, valid_suppliers
from termcolor import colored

# Function to add a product
def add_product():
    # Print a large ASCII art header
    print(r"""
         _       _     _   ____                _            _   
        / \   __| | __| | |  _ \ _ __ ___   __| |_   _  ___| |_ 
       / _ \ / _` |/ _` | | |_) | '__/ _ \ / _` | | | |/ __| __|
      / ___ \ (_| | (_| | |  __/| | | (_) | (_| | |_| | (__| |_ 
     /_/   \_\__,_|\__,_| |_|   |_|  \___/ \__,_|\__,_|\___|\__|
    
    """)
    # Trying to open the 'products.txt' file and check if it exists
    try:
        with open('products.txt', 'r') as f:
            lines = f.readlines()
            file_exists = bool(lines)
    except FileNotFoundError:
        file_exists = False

    # If the file doesn't exist, create it and write the table header
    if not file_exists:
        with open('products.txt', 'w') as f:
            table_header = f"{'ProductID':<10}, {'ProductName':<25}, {'ProductCategory':<15}, {'ProductQuantity':<15}, {'ProductImportPrice':<20}, {'ProductRetailPrice':<20}, {'SupplierID':<10}\n\n"
            f.write(table_header)  # Writing the header into the new file

    # Print a message prompting the user to input product details
    print('Enter product details (or "quit" to exit): ')
    
    # Get the next product ID using the get_next_id function
    product_id = get_next_id('products.txt', 'P', 0)
    print(f"Product ID: {product_id}")
    
    # Loop to get the product name from the user
    while True:
        product_name = input('Product Name: ').strip()
        if product_name.lower() == 'quit':
            return None    # Exit the function if the user enters "quit"
        formatted_name = format_name(product_name)
        if formatted_name:
            break
    
    # Loop to get a valid product category
    while True:
        # Display available categories in cyan color
        print(colored("Available Categories: Dairy, Fruits, Vegetables, Poultry, Seafood, Beverages, Bakery, Snacks, Frozen, Grains, Others", "cyan"))
        product_category = input('Product Category: ').strip().capitalize()
        if product_category.lower() == 'quit':
            return None
        if product_category not in PRODUCT_CATEGORIES:  # If the entered category is not valid
            print(colored("Invalid category. Defaulting to 'Others'.", "yellow"))
            product_category = 'Others'  # Default to 'Others' if invalid category
            break
        else:
            break  # Exit loop if valid category is entered

    # Loop to get a valid product quantity
    while True:
        product_quantity = input('Product Quantity: ').strip()
        if product_quantity.lower() == 'quit':
            return None
        try:
            product_quantity = int(product_quantity)
            if product_quantity < 0:
                raise ValueError  # Raise error if quantity is negative
            break
        except ValueError:
            print(colored("Invalid quantity. Enter a positive integer.", "red"))
    
    # Loop to get a valid product import price
    while True:
        product_import_price = input('Product Import Price (RM): ').strip()
        if product_import_price.lower() == 'quit':
            return None
        try:
            product_import_price = float(product_import_price)
            if product_import_price < 0:
                raise ValueError  # Raise error if price is negative
            product_import_price = f"{product_import_price:.2f}" # Ensure price is a float with 2 decimal places
            break
        except ValueError:
            print(colored("Invalid import price. Enter a valid number.", "red"))
    
    # Loop to get a valid product selling price
    while True:
        product_retail_price = input('Product Retail Price (RM): ').strip()
        if product_retail_price.lower() == 'quit':
            return None
        try:
            product_retail_price = float(product_retail_price)
            if product_retail_price < 0:
                raise ValueError  # Raise error if price is negative
            product_retail_price = f"{product_retail_price:.2f}"
            break
        except ValueError:
            print(colored("Invalid retail price. Enter a valid number.", "red"))
    
    # Print available suppliers and prompt user for valid Supplier ID
    print(colored("\nAvailable Suppliers:", "cyan"))
    valid_supplier_ids = valid_suppliers()  # Get list of valid supplier IDs
    while True:
        try:
            supplier_id = input("Supplier ID (SXXXX): ").strip()  # Take supplier ID input
            if supplier_id.lower() == 'quit':
                return None
            if supplier_id in valid_supplier_ids:
                break
            else:
                print(colored("Invalid supplier ID. Try again.", "red"))
        except FileNotFoundError:
            print(colored("No suppliers data available. Please add a supplier first.", "red"))
            return None  # Exit if the supplier data file doesn't exist
    
    # Write the new product details to the 'products.txt' file
    with open('products.txt', 'a') as f:
        table = f"{product_id:<10}, {formatted_name:<25}, {product_category:<15}, {product_quantity:<15}, {product_import_price:<20}, {product_retail_price:<20}, {supplier_id:<10}\n"
        f.write(table)  # Append the new product information to the file
    
    # Print success message
    print(colored(f"{formatted_name} with ID {product_id} has been added.", "green"))
