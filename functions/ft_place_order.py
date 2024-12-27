from utils import valid_products, get_next_id
from termcolor import colored
import datetime

def place_order():
    print(r"""
      ____  _                   ___          _           
     |  _ \| | __ _  ___ ___   / _ \ _ __ __| | ___ _ __ 
     | |_) | |/ _` |/ __/ _ \ | | | | '__/ _` |/ _ \ '__|
     |  __/| | (_| | (_|  __/ | |_| | | | (_| |  __/ |   
     |_|   |_|\__,_|\___\___|  \___/|_|  \__,_|\___|_|   
    
    """)
    # Check if the orders.txt exists and create it if not
    try:
        with open('orders.txt', 'r') as f:
            lines = f.readlines()
            file_exists = bool(lines)
    except FileNotFoundError:
        file_exists = False
    
    if not file_exists:
        with open('orders.txt', 'w') as f:
            header = f"{'OutgoingOrderID':<15}, {'IncomingOrderID':<15}, {'ProductID':<10}, {'ImportPrice':<12}, {'RetailPrice':<12}, {'OrderStatus':<12}, {'SupplierID':<10}, {'OrderDate':<10}\n\n"
            f.write(header)

    # Display mini menu for order type
    while True:
        print("Mini Menu for Placing Order")
        print("[1] Place Order to Supplier (Add stock)")
        print("[2] Place Order from Customer (Sell product)")
        print("[3] Back to Main Menu")
    
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice == '3':
            return None
        if choice not in ['1', '2']:
            print(colored("Invalid choice. Please try again.", "red"))
            continue
            
        print(colored("\nAvailable Products:", "cyan"))
        valid_product_ids = valid_products()
        if not valid_product_ids:
            print(colored("No valid products found. Please add products first.", "red"))
            return None
        
        while True:
            product_id = input("\nEnter Product ID: ").strip()
            if product_id.lower() == 'quit':
                return None
            if product_id.strip() in valid_product_ids:
                break
            else:
                print(colored("Invalid Product ID. Please try again.", "red"))
        
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
                print(colored("Invalid quantity. Please enter a positive integer.", "red"))
        
        if choice == '1':
            outgoing_order_id = '0'
            incoming_order_id = get_next_id('orders.txt', 'I', 1)
            
            with open('products.txt', 'r') as f:
                products = f.readlines()
                for product in products:
                    if product.strip():
                        fields = [item.strip() for item in product.split(", ")]
                        if fields[0] == product_id:
                            import_price = f"{float(fields[4]):.2f}"
                            retail_price = 0 # Not applicable for supplier orders
                            supplier_id = fields[6]
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
                            retail_price = f"{float(fields[5]):.2f}"
                            supplier_id = '0'
                            break
            order_status = f"-{quantity}"
    
        order_date = datetime.datetime.now().strftime("%d/%m/%Y")
        
        with open('orders.txt', 'a') as f:
            table = f"{outgoing_order_id:<15}, {incoming_order_id:<15}, {product_id:<10}, {import_price:<12}, {retail_price:<12}, {order_status:<12}, {supplier_id:<10}, {order_date:<10}\n"
            f.write(table)
        
        updated_products = []
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
                updated_products.append(fields)
        
        with open('products.txt', 'w') as f:
            f.write(header)
            f.write(blank_line)
            for product in updated_products:
                table = f"{product[0]:<10}, {product[1]:<25}, {product[2]:<15}, {product[3]:<15}, {product[4]:<20}, {product[5]:<20}, {product[6]:<10}\n"
                f.write(table)
        
        if choice == '1':
            order_id = incoming_order_id
            quantity_change = f"increased by {quantity}"
        elif choice == '2':
            order_id = outgoing_order_id
            quantity_change = f"decreased by {quantity}"
        
        print(colored(f"\nOrder {order_id} has been placed successfully!", "green"))
        print(colored(f"Quantity of {product_id} has been {quantity_change}.", "green"))
        
        break