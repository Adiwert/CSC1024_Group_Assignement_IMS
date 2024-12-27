# Import necessary modules and functions
from utils import valid_products, get_next_id  # Import utility functions
from termcolor import colored  # Import colored function for text output in terminal
import datetime  # Import datetime module for getting the current date

def place_order():
    # Print a large ASCII art header
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
    
    # If the file doesn't exist, create it with a header
    if not file_exists:
        with open('orders.txt', 'w') as f:
            header = f"{'OutgoingOrderID':<15}, {'IncomingOrderID':<15}, {'ProductID':<10}, {'ImportPrice':<12}, {'RetailPrice':<12}, {'OrderStatus':<12}, {'SupplierID':<10}, {'OrderDate':<10}\n\n"
            f.write(header)

    # Display a mini menu for selecting the type of order to place
    while True:
        print("Mini Menu for Placing Order")
        print("[1] Place Order to Supplier (Add stock)")
        print("[2] Place Order from Customer (Sell product)")
        print("[3] Back to Main Menu")

        # Take input for the order type choice
        choice = input("\nEnter your choice (1-3): ").strip()
        if choice == '3':
            return None
        if choice not in ['1', '2']:
            print(colored("Invalid choice. Please try again.", "red"))
            continue  # Re-display the menu if invalid choice is made
        
        # Show available products for order
        print(colored("\nAvailable Products:", "cyan"))
        # Get list of valid product IDs
        valid_product_ids = valid_products()
        if not valid_product_ids:
            print(colored("No valid products found. Please add products first.", "red"))
            return None  # Exit if no valid products exist
        
        # Get the product ID from the user
        while True:
            product_id = input("\nEnter Product ID: ").strip()
            if product_id.lower() == 'quit':
                return None
            if product_id.strip() in valid_product_ids:
                break
            else:
                print(colored("Invalid Product ID. Please try again.", "red"))  # Error message for invalid ID
        
        # Get the quantity for the order from the user
        while True:
            try:
                quantity = input("Enter incoming or outgoing quantity: ").strip()
                if quantity.lower() == 'quit':
                    return None
                quantity = int(quantity)
                if quantity <= 0:  # Ensure quantity is positive
                    raise ValueError
                break
            except ValueError:
                print(colored("Invalid quantity. Please enter a positive integer.", "red"))  # Error message for invalid quantity
        
        # If the user chose to place an order to the supplier
        if choice == '1':
            outgoing_order_id = '0'  # Not applicable for supplier orders
            incoming_order_id = get_next_id('orders.txt', 'I', 1)  # Generate incoming order ID for supplier
            
            # Read product details from 'products.txt' to fetch prices and supplier information
            with open('products.txt', 'r') as f:
                products = f.readlines()
                for product in products:
                    if product.strip():
                        fields = [item.strip() for item in product.split(", ")]
                        if fields[0] == product_id:  # Find the product matching the entered product ID
                            import_price = f"{float(fields[4]):.2f}"
                            retail_price = 0  # Not applicable for supplier orders
                            supplier_id = fields[6]
                            break
            order_status = f"+{quantity}"  # Mark order status as addition for supplier orders
        
        # If the user chose to place an order from the customer
        elif choice == '2':
            outgoing_order_id = get_next_id('orders.txt', 'O', 0)  # Generate outgoing order ID for customer
            incoming_order_id = '0'  # Not applicable for customer orders
            
            # Read product details from 'products.txt' to fetch prices and customer information
            with open('products.txt', 'r') as f:
                products = f.readlines()
                for product in products:
                    if product.strip():
                        fields = [item.strip() for item in product.split(", ")]
                        if fields[0] == product_id:  # Find the product matching the entered product ID
                            import_price = 0  # Not applicable for customer orders
                            retail_price = f"{float(fields[5]):.2f}"
                            supplier_id = '0'  # Not applicable for customer orders
                            break
            order_status = f"-{quantity}"  # Mark order status as subtraction for customer orders

        # Get the current date in the format dd/mm/yyyy
        order_date = datetime.datetime.now().strftime("%d/%m/%Y")
        
        # Append the new order details to 'orders.txt'
        with open('orders.txt', 'a') as f:
            table = f"{outgoing_order_id:<15}, {incoming_order_id:<15}, {product_id:<10}, {import_price:<12}, {retail_price:<12}, {order_status:<12}, {supplier_id:<10}, {order_date:<10}\n"
            f.write(table)
        
        # Update the product quantity in 'products.txt'
        updated_products = []  # List to store updated product data
        with open('products.txt', 'r') as f:
            header = f.readline()
            blank_line = f.readline()
            for line in f:
                fields = [item.strip() for item in line.split(", ")]
                if fields[0] == product_id:
                    current_quantity = int(fields[3])
                    if choice == '1':  # If it's a supplier order, increase the quantity
                        new_quantity = current_quantity + quantity
                    elif choice == '2':  # If it's a customer order, decrease the quantity
                        new_quantity = current_quantity - quantity
                    fields[3] = int(new_quantity)  # Update the quantity
                updated_products.append(fields)  # Append the updated product to the list
        
        # Overwrite the updated product data back to 'products.txt'
        with open('products.txt', 'w') as f:
            f.write(header)
            f.write(blank_line)
            for product in updated_products:
                # Write each updated product to the file
                table = f"{product[0]:<10}, {product[1]:<25}, {product[2]:<15}, {product[3]:<15}, {product[4]:<20}, {product[5]:<20}, {product[6]:<10}\n"
                f.write(table)
        
        # Print confirmation message with the order ID and quantity change
        if choice == '1':
            order_id = incoming_order_id
            quantity_change = f"increased by {quantity}"
        elif choice == '2':
            order_id = outgoing_order_id
            quantity_change = f"decreased by {quantity}"
        
        # Success message for placing the order
        print(colored(f"\nOrder {order_id} has been placed successfully!", "green"))
        # Success message for updating product quantity
        print(colored(f"Quantity of {product_id} has been {quantity_change}.", "green"))
        
        break  # Exit the loop after placing the order