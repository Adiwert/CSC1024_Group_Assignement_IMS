# Importing functions from other folder
from functions.ft_add_product import add_product
from functions.ft_update_product import update_product
from functions.ft_add_supplier import add_supplier
from functions.ft_place_order import place_order
from functions.ft_view_inventory import view_inventory
from functions.ft_generate_reports import generate_reports
# Importing the colored function to print colored text in the terminal
from termcolor import colored

# Main menu function
def main_menu():
    # Printing a large header in blue color
    print(colored("""
                                ██████████████████████████████████████████████████████                                                                  
                                █████████████        ████████████         ████████████                                                                  
                                █████████████████████████████████    █████████████████                                                                  
                                   █████████████        █████████████          █████████████                                                            
                             ██████████████         ██████████████          █████████████                                                               
                            ██████████████          ██████████████           ██████████████                                                             
                          ███████████████          ███████████████            ███████████████                                                           
                        ████████████████           ████████████████            ███████████████                                                          
                       ███████████████████████████████████████████████   ████  █████████████████                                                        
                       ████████████████            ████████████████             ████████████████                                                        
                       ██  ████████████            ████████████████             ████████████████                                                        
                       ██  ████████████            ████████████████             ███████████████      █████████                                          
                       ███  ████████████          ██████████████████           ████████████████    ████████████                                         
                        ████  █  ████ ████      ███  █████████████ ██        ███ █████████████    ███  █████████                                        
                          █████████     █████████      █████████     █████████     █████████      ███ ███████████                                       
                          ██                                                              ██     ████  ██████████                                       
                          ██████████████████████████████████████████████████████████████████    ███   █████████████                                     
                          ██████████████      ████████          ██████████    ██████████████   ███  ███████████████                                     
                          ██                   ███████          ██   ███         ████     ██  ██████████████████████                                    
                          ██   █              ████████          ██  ██             █████████  ███  █████████████████                                    
                            ██              ███████ ██          ████              ███████ ██  ███ ██████████████████                                    
                          ██              ███████   ██          ██              ███████   ██   █████████████████████                                    
                          ██             ██████     ██          ██            ███████     ██    ███████████████████                                     
                          ██           ██████      ███          ██           ██████     ████     █████████████████                                      
                          ██         ██████      █████          ██         ██████      █████       █████████████                                        
                          ███  ███████████████████████          ███  ██████████████████████           █████                                             
                          ██                        ██          ██                        ██            ██                                              
        ████ ███ ████     ██                        ██          ██                        ██            ██                                              
        █ ████ ███ ██     ██                        ██          ██                        ██            ██                                              
        █ ████ ███ ███████████████████████████████████████████████████████████████████████████████████████                                              
    ___________________________________________________________________________________________________________________
                                      ___                      _                   
                                     |_ _|_ ____   _____ _ __ | |_ ___  _ __ _   _ 
                                      | || '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |
                                      | || | | \ V /  __/ | | | || (_) | |  | |_| |
                                     |___|_| |_|\_/ \___|_| |_|\__\___/|_|   \__, |
                                        __  __                               |___/ 
                                       |  \/  | __ _ _ __   __ _  __ _  ___ _ __     
                                       | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|    
                                       | |  | | (_| | | | | (_| | (_| |  __/ |       
                                       |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|       
                                                                 |___/        
    ____________________________________________________________________________________________________________________
    """, "blue"))
    
    # Infinite loop to show the main menu until the user exits
    while True:
        # Displaying the main menu options
        print("\n====== Main Menu ======")
        print("[1] Add a New Product")
        print("[2] Update Product Details")
        print("[3] Add a New Supplier")
        print("[4] Place an Order")
        print("[5] View Inventory")
        print("[6] Generate Reports")
        print("[7] Exit")

        # Taking input for menu choice
        choice = input("Enter your choice (1-7): ").strip()
        # Calling the respective function based on the user's choice
        if choice == '1':
            add_product()  # Add a new product
        elif choice == '2':
            update_product()  # Update existing product details
        elif choice == '3':
            add_supplier()  # Add a new supplier
        elif choice == '4':
            place_order()  # Place a new order
        elif choice == '5':
            view_inventory()  # View the current inventory
        elif choice == '6':
            generate_reports()  # Generate reports
        elif choice == '7':
            # Printing a message and exiting the program
            print(r"""
                  ____             __   __               _               _       _ 
                 / ___|  ___  ___  \ \ / /__  _   _     / \   __ _  __ _(_)_ __ | |
                 \___ \ / _ \/ _ \  \ V / _ \| | | |   / _ \ / _` |/ _` | | '_ \| |
                  ___) |  __/  __/   | | (_) | |_| |  / ___ \ (_| | (_| | | | | |_|
                 |____/ \___|\___|   |_|\___/ \__,_| /_/   \_\__, |\__,_|_|_| |_(_)
                                                             |___/                 
            """)
            break  # Exits the infinite loop and ends the program
        else:
            # If the user enters an invalid option, display an error message
            print(colored("Invalid choice. Please try again.", "red"))

# Running the script directly by calling main_menu()
if __name__ == "__main__":
    main_menu()