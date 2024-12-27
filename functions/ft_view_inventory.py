# Import necessary modules
from termcolor import colored  # Import colored for colored terminal text
from prettytable import PrettyTable  # Import PrettyTable for displaying formatted tables

# Define a function to display a inventory table
def view_inventory():
    # Print a large ASCII art header
    print(r"""
     __     ___                 ___                      _                   
     \ \   / (_) _____      __ |_ _|_ ____   _____ _ __ | |_ ___  _ __ _   _ 
      \ \ / /| |/ _ \ \ /\ / /  | || '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |
       \ V / | |  __/\ V  V /   | || | | \ V /  __/ | | | || (_) | |  | |_| |
        \_/  |_|\___| \_/\_/   |___|_| |_|\_/ \___|_| |_|\__\___/|_|   \__, |
                                                                       |___/ 
    """)
    try:
        # Attempt to open the "products.txt" file for reading
        with open("products.txt",'r') as file:
            lines = file.readlines()

            if len(lines) <= 2:
                print(colored("The inventory is currently empty. Add some products first", "red"))
                return
            
            # Create a PrettyTable object to display data in a table format
            table = PrettyTable()
            
            # Extract the headers from the first line of the file and add to the table
            headers = [header.strip() for header in lines[0].split(", ")]
            table.field_names = headers
            
            # Process each data line and format it for the table
            for line in lines[2:]:
                rows = [column.strip() for column in line.split(", ")]
                rows[4] = f"RM {float(rows[4]):.2f}" # Format the import price
                rows[5] = f"RM {float(rows[5]):.2f}" # Format the retail price
                # Add the row to the PrettyTable object
                table.add_row(rows)
            
            # Print the table with additional headings and separators
            print("\n========================================================= Inventroy List ==========================================================\n")
            print(table)
            print("\nTotal Products:", len(lines) - 2) # Substract header and blank line
            
            # Calculate the total inventory value
            total_value = 0.00
            for line in lines[2:]:
                if line.strip():  # Check if the line is not empty
                    fields = [field.strip() for field in line.split(", ")]
                    product_quantity = int(fields[3])  # Extract the quantity
                    import_price = float(fields[4])  # Extract the import price
                    total_value += product_quantity * import_price  # Accumulate the total value
            
            # Display the total inventory value
            print(f"Total Inventory Value: RM {total_value:.2f}")
            print("\n" + "=" * 132 + "\n")  # Print a line separator
    
    # Handle the case where the file does not exist
    except FileNotFoundError:
        print(colored("\nError: The file does not exist. add product to create the file.", "red"))
    # Handle any unexpected errors and display the error message
    except Exception as e:
        print(colored(f"An error occurred: {e}", "red"))
