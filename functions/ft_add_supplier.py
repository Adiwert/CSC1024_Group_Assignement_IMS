from utils import PRODUCT_CATEGORIES, format_name, get_next_id
from termcolor import colored

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

    print('Enter supplier details (or "quit" to exit): ')

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
        print(colored("Available Categories: Dairy, Fruits, Vegetables, Poultry, Seafood, Beverages, Bakery, Snacks, Frozen, Grains, Others", "cyan"))
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
        contact_number = input('Enter Contact Number (format 0xx-xxxxxxxx): ').strip()
        if contact_number.lower() == 'quit':
            return None # Exit the function if the user enters "quit"
        if len(contact_number) not in [11, 12]:
            print(colored("Invalid contact number. Please try again.", "red"))
            continue
        if contact_number[0] != '0' or contact_number[3] != '-':
            print(colored("Invalid contact number. Please try again.", "red"))
            continue
        if not contact_number[1:3].isdigit() or not contact_number[4:].isdigit():
            print(colored("Invalid contact number. Please try again.", "red"))
            continue
        break # Exit loop if valid contact number is entered

    with open('suppliers.txt', 'a') as f:
        table = f"{supplier_id:<10}, {formatted_name:<30}, {product_category:<15}, {contact_number:<15}\n"
        f.write(table)
    
    print(colored(f"{formatted_name} with ID of {supplier_id} has been added.\n", "green"))