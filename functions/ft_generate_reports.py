from termcolor import colored  # Import the colored module from termcolor to print colored text in the terminal
from prettytable import PrettyTable  # Import PrettyTable for displaying tables in a user-friendly format

# Define the function to generate reports
def generate_reports():
    # Print a large ASCII art header
    print(r"""
       ____                           _         ____                       _       
      / ___| ___ _ __   ___ _ __ __ _| |_ ___  |  _ \ ___ _ __   ___  _ __| |_ ___ 
     | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \ | |_) / _ \ '_ \ / _ \| '__| __/ __|
     | |_| |  __/ | | |  __/ | | (_| | ||  __/ |  _ <  __/ |_) | (_) | |  | |_\__ \
      \____|\___|_| |_|\___|_|  \__,_|\__\___| |_| \_\___| .__/ \___/|_|   \__|___/
                                                              |_|                       
    """)
    
    while True:  # Start an infinite loop for the menu options
        print("\nSelect the type of report you want to generate:")  # Prompt the user to select a report type
        print("[1] Inventory Report")
        print("[2] Sales Report")
        print("[3] Expenses Report")
        print("[4] Profit/Loss Summary")
        print("[5] Back to Main Menu")
        # Get user input and remove leading/trailing whitespace
        choice = input("Enter your choice (1-5): ").strip()

        # If the user selects '5', exit the function and return to the main menu
        if choice == '5':
            return None
        
        # Try to generate the selected report, and handle any potential exceptions
        try:
            if choice == '1':
                with open("products.txt",'r') as f:
                    lines = f.readlines()
                    if len(lines) <= 2:
                        print(colored("\nThe inventory is empty. Report are unable to be generated", "red"))
                        return None  # Exit the function if no report can be generated

                    LOW_STOCK_THRESHOLD = 20  # Define the threshold for low stock
                    TARGET_STOCK_LEVEL = 50  # Define the target stock level
                    low_stock_items = []  # Initialize an empty list to store low stock items
                    supplier_orders = []  # Initialize an empty list to store supplier orders

                    inventory_table = PrettyTable()  # Create a PrettyTable object to display the inventory
                    headers = [header.strip() for header in lines[0].split(", ")]
                    inventory_table.field_names = headers  # Set the table headers

                    for line in lines[2:]:
                        fields = [field.strip() for field in line.split(", ")]
                        quantity = int(fields[3])  # Get the quantity of the product (field 3)

                        # Check if the product is below the low stock threshold
                        if quantity <= LOW_STOCK_THRESHOLD:
                            low_stock_items.append((fields[0], fields[1], fields[3]))  # Add the product details to the low stock list
                            supplier_orders.append((fields[6], fields[1], TARGET_STOCK_LEVEL - quantity))  # Create a suggested supplier order
                            colored_quantity = colored(fields[3], "red")  # Color the quantity red to indicate low stock
                        else:
                            colored_quantity = fields[3]  # Otherwise, leave the quantity as is

                        inventory_table.add_row([
                            fields[0],  # Product ID
                            fields[1],  # Product Name
                            fields[2],  # Product Category
                            colored_quantity,  # Product Quantity (colored red if low stock)
                            fields[4],  # Product Import Price
                            fields[5],  # Product Retail Price
                            fields[6]   # Supplier ID
                        ])

                    # Print the inventory table
                    print("\n======================================================= Inventroy Report ========================================================\n")
                    print(inventory_table)

                    # If there are any low stock items, create a new PrettyTable for them
                    if low_stock_items:
                        print("\n======================================================= Low Stock Items ========================================================\n")
                        low_stock_table = PrettyTable()
                        low_stock_table.field_names = ["ProductID", "ProductName", "Quantity"]  # Set the table headers
                        for item in low_stock_items:
                            low_stock_table.add_row([item[0], item[1], colored(item[2], "red")])  # Add each low stock item as a row
                        print(low_stock_table)

                    # If there are any suggested supplier orders, create a new PrettyTable for them
                    if supplier_orders:
                        print("\n================================================== Suggested Supplier Orders ===================================================\n")
                        supplier_order_table = PrettyTable()
                        supplier_order_table.field_names = ["SupplierID", "ProductName", "Quantity to Order"]  # Set the table headers
                        for order in supplier_orders:
                            supplier_order_table.add_row([order[0], order[1], colored(order[2], "green")])  # Add each suggested supplier order as a row
                        print(supplier_order_table)

            elif choice == "2":
                with open("orders.txt", "r") as f:
                    lines = f.readlines()
            
                total_sales = 0.00 # Initialize a variable to store the total sales
                sales_table = PrettyTable()  # Create a PrettyTable object for the sales report
                sales_table.field_names = ["OutgoingOrderID", "ProductID", "Quantity", "RetailPrice"]  # Set the table headers
                
                for line in lines[2:]:
                    fields = [field.strip() for field in line.split(", ")]
                    if fields[0] != "0":  # If the order is outgoing (not a incoming order)
                        total_sales += float(fields[4]) * abs(int(fields[5]))  # Calculate the total sales
                        sales_table.add_row([fields[0], fields[2], fields[5], f"RM {float(fields[4]):.2f}"])  # Add the sale to the sales table
                
                # Print the sales report table and the total sales
                print("\n======================================================= Sales Report ========================================================\n")
                print(sales_table)
                print(f"\nTotal Sales: RM {total_sales:.2f}\n")
            
            elif choice == "3":
                with open("orders.txt", "r") as f:
                    lines = f.readlines()
                
                total_expenses = 0.00  # Initialize a variable to store the total expenses
                expense_table = PrettyTable()  # Create a PrettyTable object for the expenses report
                expense_table.field_names = ["IncomingOrderID", "ProductID", "Quantity", "ImportPrice"]  # Set the table headers
                
                for line in lines[2:]:
                    fields = [field.strip() for field in line.split(", ")]
                    if fields[1] != "0":  # If the order is incoming (not an outgoing order)
                        total_expenses += float(fields[3]) * abs(int(fields[5]))  # Calculate the total expenses
                        expense_table.add_row([fields[1], fields[2], fields[5], f"RM {float(fields[3]):.2f}"])  # Add the expense to the expenses table
                
                # Print the expenses report table and the total expenses
                print("\n======================================================= Expenses Report ========================================================\n")
                print(expense_table)
                print(f"\nTotal Expenses: RM {total_expenses:.2f}\n")
            
            elif choice == "4":
                with open("orders.txt", "r") as f:
                    lines = f.readlines()
                
                total_sales = 0.00  # Initialize total sales
                total_expenses = 0.00  # Initialize total expenses
                
                for line in lines[2:]:
                    fields = [field.strip() for field in line.split(", ")]
                    if fields[0] != "0": # Outgoing order
                        total_sales += float(fields[4]) * abs(int(fields[5]))  # Calculate total sales
                    elif fields[1] != "0": # Incoming order
                        total_expenses += float(fields[3]) * abs(int(fields[5]))  # Calculate total expenses
                
                # Calculate profit or los
                profit_or_loss = total_sales - total_expenses  
                if profit_or_loss >= 0:
                    profit_color = "green"  # Set the color for profit
                elif profit_or_loss < 0:
                    profit_color = "red"  # Set the color for loss
                
                # Print the profit or loss in the appropriate color
                print(f"\n================================================== Profit/Loss Summary ===================================================\n")
                print(colored(f"Net Profit/Loss: RM {profit_or_loss:.2f}", profit_color))
                
            else:
                # If the user selects an invalid choice
                print(colored("Invalid choice. Please choose a valid option.", "red"))

        except FileNotFoundError:
            print(colored("File not found. Please ensure the data files are present.", "red"))
        except Exception as e:
            print(colored(f"An unexpected error occurred: {e}", "red"))