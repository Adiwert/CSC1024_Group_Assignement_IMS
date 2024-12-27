from termcolor import colored
from prettytable import PrettyTable

def generate_reports():
    print(r"""
       ____                           _         ____                       _       
      / ___| ___ _ __   ___ _ __ __ _| |_ ___  |  _ \ ___ _ __   ___  _ __| |_ ___ 
     | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \ | |_) / _ \ '_ \ / _ \| '__| __/ __|
     | |_| |  __/ | | |  __/ | | (_| | ||  __/ |  _ <  __/ |_) | (_) | |  | |_\__ \
      \____|\___|_| |_|\___|_|  \__,_|\__\___| |_| \_\___| .__/ \___/|_|   \__|___/
                                                              |_|                       
    """)
    
    while True:
        print("\nSelect the type of report you want to generate:")
        print("[1] Inventory Report")
        print("[2] Sales Report")
        print("[3] Expenses Report")
        print("[4] Profit/Loss Summary")
        print("[5] Back to Main Menu")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '5':
            return None
        
        try:
            if choice == '1':
                with open("products.txt",'r') as f:
                    lines = f.readlines()
                    if len(lines) <= 2:
                        print(colored("\nThe inventory is empty. Report are unable to be generated", "red"))
                        return 

                    LOW_STOCK_THRESHOLD = 20
                    TARGET_STOCK_LEVEL = 50
                    low_stock_items = []
                    supplier_orders = []

                    inventory_table = PrettyTable()
                    headers = [header.strip() for header in lines[0].split(", ")]
                    inventory_table.field_names = headers

                    for line in lines[2:]:
                        fields = [field.strip() for field in line.split(", ")]
                        quantity = int(fields[3])

                        if quantity <= LOW_STOCK_THRESHOLD:
                            low_stock_items.append(fields)
                            supplier_orders.append((fields[6], fields[1], TARGET_STOCK_LEVEL - quantity))
                            colored_quantity = colored(fields[3], "red")
                        else:
                            colored_quantity = fields[3]

                        inventory_table.add_row([
                            fields[0],
                            fields[1],
                            fields[2],
                            colored_quantity,
                            fields[4],
                            fields[5],
                            fields[6]
                        ])

                    print("\n======================================================= Inventroy Report ========================================================\n")
                    print(inventory_table)

                    if low_stock_items:
                        print("\n======================================================= Low Stock Items ========================================================\n")
                        low_stock_table = PrettyTable()
                        low_stock_table.field_names = ["ProductID", "ProductName", "Quantity"]
                        for item in low_stock_items:
                            low_stock_table.add_row([item[0], item[1], colored(item[3], "red")])
                        print(low_stock_table)

                    if supplier_orders:
                        print("\n======================================================= Supplier Orders ========================================================\n")
                        supplier_order_table = PrettyTable()
                        supplier_order_table.field_names = ["SupplierID", "ProductName", "Quantity to Order"]
                        for order in supplier_orders:
                            supplier_order_table.add_row([order[0], order[1], colored(order[2], "green")])
                        print(supplier_order_table)

            elif choice == "2":
                with open("orders.txt", "r") as f:
                    lines = f.readlines()
            
                total_sales = 0.00
                sales_table = PrettyTable()
                sales_table.field_names = ["OutgoingOrderID", "ProductID", "Quantity", "RetailPrice"]
                
                for line in lines[2:]:
                    fields = [field.strip() for field in line.split(", ")]
                    if fields[0] != "0":
                        total_sales += float(fields[4]) * abs(int(fields[5]))
                        sales_table.add_row([fields[0], fields[2], fields[5], f"RM {float(fields[4]):.2f}"])
                
                print("\n======================================================= Sales Report ========================================================\n")
                print(sales_table)
                print(f"\nTotal Sales: RM {total_sales:.2f}\n")
            
            elif choice == "3":
                with open("orders.txt", "r") as f:
                    lines = f.readlines()
                
                total_expenses = 0.00
                expense_table = PrettyTable()
                expense_table.field_names = ["IncomingOrderID", "ProductID", "Quantity", "ImportPrice"]
                
                for line in lines[2:]:
                    fields = [field.strip() for field in line.split(", ")]
                    if fields[1] != "0":
                        total_expenses += float(fields[3]) * abs(int(fields[5]))
                        expense_table.add_row([fields[1], fields[2], fields[5], f"RM {float(fields[3]):.2f}"])
                        
                print("\n======================================================= Expenses Report ========================================================\n")
                print(expense_table)
                print(f"\nTotal Expenses: RM {total_expenses:.2f}\n")
            
            elif choice == "4":
                with open("orders.txt", "r") as f:
                    lines = f.readlines()
                
                total_sales = 0.00
                total_expenses = 0.00
                
                for line in lines[2:]:
                    fields = [field.strip() for field in line.split(", ")]
                    if fields[0] != "0": # Outgoing order
                        total_sales += float(fields[4]) * abs(int(fields[5]))
                    elif fields[1] != "0": # Incoming order
                        total_expenses += float(fields[3]) * abs(int(fields[5]))
                
                profit_or_loss = total_sales - total_expenses
                if profit_or_loss >= 0:
                    profit_color = "green"
                elif profit_or_loss < 0:
                    profit_color = "red"
                
                print(f"\n================================================== Profit/Loss Summary ===================================================\n")
                print(colored(f"Net Profit/Loss: RM {profit_or_loss:.2f}", profit_color))
                
            else:
                print(colored("Invalid choice. Please choose a valid option.", "red"))
            
        except FileNotFoundError:
            print(colored("File not found. Please ensure the data files are present.", "red"))
        except Exception as e:
            print(colored(f"An unexpected error occurred: {e}", "red"))