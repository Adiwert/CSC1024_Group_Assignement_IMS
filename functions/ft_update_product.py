# Import necessary modules, functions and variables
from utils import PRODUCT_CATEGORIES, valid_products, valid_suppliers, format_name
from termcolor import colored

# Define the update_product function
def update_product():
    # Print a large ASCII art header
    print(r"""
      _   _           _       _         ____                _            _   
     | | | |_ __   __| | __ _| |_ ___  |  _ \ _ __ ___   __| |_   _  ___| |_ 
     | | | | '_ \ / _` |/ _` | __/ _ \ | |_) | '__/ _ \ / _` | | | |/ __| __|
     | |_| | |_) | (_| | (_| | ||  __/ |  __/| | | (_) | (_| | |_| | (__| |_ 
      \___/| .__/ \__,_|\__,_|\__\___| |_|   |_|  \___/ \__,_|\__,_|\___|\__|
           |_|                                                               
    """)
    
    # Load products from 'products.txt'
    products = []
    try:
        with open('products.txt', 'r') as f:
            lines = f.readlines()[2:]
            for line in lines:
                if line.strip():
                    fields = [item.strip() for item in line.split(", ")]
                    product = {  # Create a dictionary for each product
                        'ID': fields[0],  # Store product ID
                        'Name': fields[1],  # Store product name
                        'Category': fields[2],  # Store product category
                        'Quantity': int(fields[3]),  # Store product quantity
                        'Import Price': float(fields[4]),  # Store import price
                        'Retail Price': float(fields[5]),  # Store retail price
                        'Supplier ID': fields[6]  # Store supplier ID
                    }
                    products.append(product)  # Add the product dictionary to the products list

    except FileNotFoundError:
        print(colored("No products file found. Please add products first.", "red"))
        return None  # Exit the function if the file is not found
    except IndexError:
        print(colored("Malformed data. Please check the file format.", "red"))
        return None # Exit the function if the data format is incorrect
    
    print(colored("\nAvailable Products:", "cyan"))  # Print available products header in cyan
    valid_product_ids = valid_products()  # Get a list of valid product IDs

    # Prompt the user to input the product ID they wish to update
    while True:
        product_id = input('\nEnter product ID to update (or type "quit" to exit): ').strip()
        if product_id.lower() == 'quit':
            return None
        if product_id.strip() in [valid_id.strip() for valid_id in valid_product_ids]:
            break  # Exit the loop if a valid ID is entered
        else:
            print(colored("Invalid product ID. Please try again.", "red"))  # Print error message for invalid product ID

     # Iterate through the list of products to find the matching product ID
    for product in products:
        if product['ID'] == product_id:  # If the current product's ID matches the input product ID
            print(colored('Current Product Details:', "cyan"))  # Print the product details in cyan
            print(f"Name: {product['Name']}")
            print(f"Category: {product['Category']}")
            print(f"Quantity: {product['Quantity']}")
            print(f"Import Price: {product['Import Price']}")
            print(f"Retail Price: {product['Retail Price']}")
            print(f"Supplier ID: {product['Supplier ID']}")
            
            # Prompt the user to update the product name
            while True:
                new_name = input('Enter new Product Name (Press "Enter" if no updates): ').strip()
                if new_name.lower() == 'quit':  # Allow user to quit by typing 'quit'
                    return None
                if new_name == '':  # If the input is empty, skip updating the name
                    break
                formatted_name = format_name(new_name)  # Format the new name using the format_name function
                product['Name'] = formatted_name  # Update the product's name
                break

            # Prompt the user to update the product category
            while True:
                print(colored("Available Categories: Dairy, Fruits, Vegetables, Poultry, Seafood, Beverages, Bakery, Snacks, Frozen, Grains, Others", "cyan"))
                new_category = input('Enter new Product Category (Press "Enter" if no updates): ').strip().capitalize()
                if new_category.lower() == 'quit':
                    return None
                if new_category == '':
                    break
                if new_category:
                    # Check if the category is valid
                    if new_category not in PRODUCT_CATEGORIES:
                        print(colored("Invalid category. Defaulting to 'Others'.", "yellow"))  # Warn user about invalid category will set to 'Others'
                        product['Category'] = 'Others'  # Default category to 'Others'
                    else:
                        product['Category'] = new_category  # Default category to 'Others'
                break

            # Prompt the user to update the product quantity
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
                            raise ValueError  # If the new quantity is negative, raise an error
                        break
                except ValueError:  # Catch invalid input (e.g., non-numeric values)
                    print(colored("Invalid quantity entered. Please try again.", "red"))
            
            # Prompt the user to update the product import price
            while True:
                try:
                    new_import_price = input('Enter new Product Price (Press "Enter" if no updates): ').strip()
                    if new_import_price.lower() == 'quit':
                        return None
                    if new_import_price == '':
                        break
                    if new_import_price:  
                        product['Import Price'] = float(new_import_price)
                        if product['Import Price'] < 0:  # If the new price is negative, raise an error
                            raise ValueError
                        product['Import Price'] = f"{new_import_price:.2f}" # Convert input to float and format to 2 decimal places
                        break  # Exit the loop once the import price is updated
                except ValueError:
                    print(colored("Invalid import price entered. Please try again", "red"))
                    
            # Prompt the user to update the product retail price
            while True:
                try:
                    new_retail_price = input('Enter new Product Retail Price (Press "Enter" if no updates): ').strip()
                    if new_retail_price.lower() == 'quit':
                        return None
                    if new_retail_price == '':
                        break
                    if new_retail_price:
                        product['Retail Price'] = float(new_retail_price)
                        if product['Retail Price'] < 0:  # If the new price is negative, raise an error
                            raise ValueError
                        product['Retail Price'] = f"{new_retail_price:.2f}"  # Convert input to float and format to 2 decimal places
                        break  # Exit the loop once the retail price is updated
                except ValueError:
                    print(colored("Invalid retail price entered. Please try again.", "red"))

            # Prompt the user to update the product supplier ID
            print(colored("\nAvailable Suppliers:", "cyan"))
            valid_supplier_ids = valid_suppliers()  # Get the list of valid supplier IDs
            while True:
                try:
                    new_supplier_id = input('Enter new Supplier ID (Press "Enter" if no updates): ').strip()
                    if new_supplier_id.lower() == 'quit':
                        return None
                    if new_supplier_id == '':
                        break
                    if new_supplier_id in valid_supplier_ids:  # Validate supplier ID
                        product['Supplier ID'] = new_supplier_id  # Update supplier ID
                        break
                    else:
                        print(colored("Invalid Supplier ID. Try again.", "red"))
                except FileNotFoundError:
                    print(colored("No supplier data available. Please add suppliers first.", "red"))
                    return None # Exit the function if there is no suppliers data available
            
            print(colored("Product successfully updated.", "green"))
            break # Exit the loop once the product is updated
    else:
        # Check if product ID is invalid
        print(colored("Invalid Product ID.", "red"))
        return None
    
    # Write updated product data back to the file
    with open('products.txt', 'w') as f:
        # Write headers
        header = f"{'ProductID':<10}, {'ProductName':<25}, {'ProductCategory':<15}, {'ProductQuantity':<15}, {'ProductImportPrice':<20}, {'ProductRetailPrice':<20}, {'SupplierID':<10}\n\n"
        f.write(header)
        # Write product data
        for product in products:
            table = f"{product['ID']:<10}, {product['Name']:<25}, {product['Category']:<15}, {product['Quantity']:<15}, {product['Import Price']:<20}, {product['Retail Price']:<20}, {product['Supplier ID']:<10}\n"
            f.write(table)
    
    # Print success message if the data is successfully updated
    print(colored(f"Product with ID {product_id} has been successfully updated.", "green"))
