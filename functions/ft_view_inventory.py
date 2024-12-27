from termcolor import colored
from prettytable import PrettyTable

def view_inventory():
    print(r"""
     __     ___                 ___                      _                   
     \ \   / (_) _____      __ |_ _|_ ____   _____ _ __ | |_ ___  _ __ _   _ 
      \ \ / /| |/ _ \ \ /\ / /  | || '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |
       \ V / | |  __/\ V  V /   | || | | \ V /  __/ | | | || (_) | |  | |_| |
        \_/  |_|\___| \_/\_/   |___|_| |_|\_/ \___|_| |_|\__\___/|_|   \__, |
                                                                       |___/ 
    """)
    try:
        with open("products.txt",'r') as file:
            lines = file.readlines()

            if len(lines) <= 2:
                print(colored("The inventory is currently empty. Add some products first", "red"))
                return
            
            table = PrettyTable()
            
            headers = [header.strip() for header in lines[0].split(", ")]
            table.field_names = headers
            
            for line in lines[2:]:
                rows = [column.strip() for column in line.split(", ")]
                rows[4] = f"RM {float(rows[4]):.2f}" # Import Price
                rows[5] = f"RM {float(rows[5]):.2f}" # Retail Price
                
                table.add_row(rows)
                

            print("\n========================================================= Inventroy List ==========================================================\n")
            print(table)
            print("\nTotal Products:", len(lines) - 2) # Substract header and blank line
            
            total_value = 0.00
            for line in lines[2:]:
                if line.strip():
                    fields = [field.strip() for field in line.split(", ")]
                    product_quantity = int(fields[3])
                    import_price = float(fields[4])
                    total_value += product_quantity * import_price
            
            print(f"Total Inventory Value: RM {total_value:.2f}")
            print("\n" + "=" * 132 + "\n")
            
    except FileNotFoundError:
        print(colored("\nError: The file does not exist. add product to create the file.", "red"))
    except Exception as e:
        print(colored(f"An error occurred: {e}", "red"))
