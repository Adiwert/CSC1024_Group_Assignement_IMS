from utils import PRODUCT_CATEGORIES, valid_products, valid_suppliers, format_name
from termcolor import colored

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
        print(colored("No products file found. Please add products first.", "red"))
        return
    except IndexError:
        print(colored("Malformed data. Please check the file format.", "red"))
        return
    
    print(colored("\nAvailable Products:", "cyan"))
    valid_product_ids = valid_products()

    while True:
        product_id = input('\nEnter product ID to update (or type "quit" to exit): ').strip()
        if product_id.lower() == 'quit':
            return None
        if product_id.strip() in [valid_id.strip() for valid_id in valid_product_ids]:
            break
        else:
            print(colored("Invalid product ID. Please try again.", "red"))

    for product in products:
        if product['ID'] == product_id:
            print(colored('Current Product Details:', "cyan"))
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
                        print(colored("Invalid category. Defaulting to 'Others'.", "yellow"))
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
                    print(colored("Invalid quantity entered. Keeping the old quantity.", "red"))
            
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
                    print(colored("Invalid import price entered. Keeping the old price.", "red"))
                    
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
                    print(colored("Invalid retail price entered. Keeping the old price.", "red"))

            print(coloered("\nAvailable Suppliers:", "cyan"))
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
                        print(colored("Invalid Supplier ID. Try again.", "red"))
                except FileNotFoundError:
                    print(colored("No supplier data available. Please add suppliers first.", "red"))
                    return None # Exit the function if there is no suppliers data available
            
            print(colored("Product successfully updated.", "green"))
            break
    else:
        print(colored("Invalid Product ID.", "red"))
        return None
    
    with open('products.txt', 'w') as f:
        header = f"{'ProductID':<10}, {'ProductName':<25}, {'ProductCategory':<15}, {'ProductQuantity':<15}, {'ProductImportPrice':<20}, {'ProductRetailPrice':<20}, {'SupplierID':<10}\n\n"
        f.write(header)
        for product in products:
            table = f"{product['ID']:<10}, {product['Name']:<25}, {product['Category']:<15}, {product['Quantity']:<15}, {product['Import Price']:<20}, {product['Retail Price']:<20}, {product['Supplier ID']:<10}\n"
            f.write(table)
    
    print(colored(f"Product with ID {product_id} has been successfully updated.", "green"))