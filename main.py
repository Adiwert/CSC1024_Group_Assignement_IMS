def add_product():
    # Code to add a product to products.txt
    pass

def update_product(): ## always check the sticky notes 
    # Code to update product details
   

    pass

def add_supplier():
    # Code to add a supplier to suppliers.txt
    pass

def place_order():
    # Code to place an order
    pass

def view_inventory():
    try:
        with open("product.txt",'r') as file:
            lines = file.readlines()

            if len(lines) <= 2:
                print("The inventory is currently empty. Add some products first")
                return

            print("\n-- Inventroy List --\n")
            for line in lines:
                print(line, end="")
            print("\n-------------------")

    except FileNotFoundError:
        print("\nError: The file does not exist. add product to create the file ")

    pass

def generate_reports():
    # Code to generate reports
    try:
        with open("product.txt",'r') as file :
            lines = file.readlines()

            if len(lines) <=2:
                print("\nThe inventory is empty. Report are unable to be generated")
                return

                total_product = 0
                total_value = 0.0

                for line in lines[2:]:
                    if line.strip():
                        total_product += 1
                        price = float(line[30:40].strip())
                        total_value += price

                print("\n-- Inventory Report --\n")
                print(f"The total products: {total_product}")
                print(f"The total value of products: {total_value:.2f}")
           
    except FileNotFoundError:
                print("\nError: the product does not exist. Add the product first\n")
           
    except FileNotFoundError:
                print("Invalid input. Try again")
                
    pass

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
            print("Invalid choice. Please try again.")
            print("Hello world!")