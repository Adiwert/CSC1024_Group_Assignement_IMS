import datetime
from termcolor import colored

# Predefined food categories for the user to choose from
PRODUCT_CATEGORIES = [
    "Dairy", "Fruits", "Vagetables", "Poultry", "Seafood", 
    "Beverages", "Bakery", "Snacks", "Frozen", "Grains", "Others"
]

# Function to format names when append it into .txt files
def format_name(name):
    words = name.split() # Splits the name into individual words.
    cap_words = [word.capitalize() for word in words] # Capitalizes the first letter of each word.
    formatted_name = '_'.join(cap_words) # Joins the capitalized words with underscores.
    
    return formatted_name

# General helper function to get the next ID for any file
def get_next_id(file_name, prefix, column_index):
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
        if len(lines) <= 2:
            return f'{prefix}0001'
        
        for line in reversed(lines[2:]):
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

# Function to get the next ID for suppliers.txt
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
        print(colored("No suppliers found. Add suppliers first.", "red"))
    
    return valid_supplier_ids

# Function to get the next ID for customers.txt
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
        print(colored("No products found. Add products first.", "red"))
        
    return valid_product_ids