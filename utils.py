# Importing necessary modules
from termcolor import colored  # Used to print colored text to the terminal

# Predefined food categories for the user to choose from
PRODUCT_CATEGORIES = [
    "Dairy", "Fruits", "Vegetables", "Poultry", "Seafood", 
    "Beverages", "Bakery", "Snacks", "Frozen", "Grains", "Others"
]

# Function to format names when append it into .txt files
def format_name(name):
    words = name.split() # Splits the name into individual words
    cap_words = [word.capitalize() for word in words] # Capitalizes the first letter of each word
    formatted_name = '_'.join(cap_words) # Joins the capitalized words with underscores
    
    return formatted_name

# General helper function to get the next ID for any file
def get_next_id(file_name, prefix, column_index):
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
        if len(lines) <= 2:
            return f'{prefix}0001'  # If the file has two or fewer lines, return the first ID
        
        for line in reversed(lines[2:]):  # Loop through lines in reverse, skipping first 2 header lines
            columns = [column.strip() for column in line.split(", ")]  # Split each line by ", " and strip extra spaces
            last_id = columns[column_index]  # Get the ID from the specified column
            # Skip if ID is '0'
            if last_id == '0':
                continue
            if last_id.startswith(prefix) and len(last_id[1:]) == 4 and last_id[1:].isdigit():  # Validates the ID
                last_numeric_id = int(last_id[1:])  # Extracts the numeric part of the ID and converts it to an integer
                next_id = f'{prefix}{last_numeric_id + 1:04d}'  # Increments the ID by 1 and formats it with leading zeros
                return next_id  # Returns the next ID in the sequence
        
        # If no valid ID is found, return the first ID
        return f'{prefix}0001'
    
    # If the file does not exist, return the prefix followed by 0001
    except FileNotFoundError:
        return f'{prefix}0001'

# Function to get the next ID for suppliers.txt
def valid_suppliers(filename='suppliers.txt'):
    valid_supplier_ids = []  # Initialize an empty list to store valid supplier IDs
    try:
        with open(filename, "r") as f:
            suppliers = f.readlines()[2:]
        for supplier in suppliers:  # Loop through each supplier in the file
            supplier_info = [item.strip() for item in supplier.split(", ")]
            valid_supplier_ids.append(supplier_info[0])  # Add the supplier ID to the list
            print(f"{supplier_info[0]} - {supplier_info[1]}")  # Print the supplier ID and name
    except FileNotFoundError:
        print(colored("No suppliers found. Add suppliers first.", "red"))  # Print an error message if the file doesn't exist
    
    return valid_supplier_ids

# Function to get the next ID for customers.txt
def valid_products(filename='products.txt'):
    valid_product_ids = []  # Initialize an empty list to store valid product IDs
    try:
        with open(filename, "r") as f:
            products = f.readlines()[2:]
        for product in products:  # Loop through each product in the file
            product_info = [item.strip() for item in product.split(", ")]
            valid_product_ids.append(product_info[0])  # Add the product ID to the list
            print(f"{product_info[0]} - {product_info[1]}")  # Print the product ID and name
    except FileNotFoundError:
        print(colored("No products found. Add products first.", "red")) # Print an error message if the file doesn't exist
        
    return valid_product_ids