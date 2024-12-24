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
        with open("products.txt",'r') as file:
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


from prettytable import PrettyTable

def generate_reports():
    # Code to generate reports
    try:
        with open("products.txt",'r') as file :
            lines = file.readlines()

            if len(lines) <=2:
                print("\nThe inventory is empty. Report are unable to be generated")
                return 

            total_product = 0
            total_value = 0.0
            low_stock = 20
            low_stock = []
            supplier_order = []

            table = PrettyTable()
            table.field_names = ["Product ID","Product Name","Price","Quantity"]


            for line in lines[2:]:
                    if line.strip():
                        product_id = line[0:10].strip()
                        product_name = line[10:30].strip()
                        quantity = int(line[30:35].strip())
                        price = float(line[35:45].strip())
                        total_product += 1
                        
                        total_value += price * quantity

                        table.add_row([product_id, product_name, quantity, f"${price:.2f}"])

                        if quantity < low_stock:
                            low_stock.append(product_name)
                            supplier_order.append ((product_name, low_stock - quantity))

            print("\n-- Inventory Report --\n")
            print(table)
            print(f"The total products: {total_product}")
            print(f"The total value of products: {total_value:.2f}")

            if low_stock:
                    print("\n-- Low Stock! --")
                    print("The products that are low stock: ")
                    for product in low_stock:
                        print(f"-{product}")

            if supplier_order :
                    print("\n-- Supplier Order --")
                    print("\n Products that need to be ordered:")
                    for product, order_quantity in supplier_order:
                        print(f" -{product}: Order {order_quantity} more units")

                
           
    except FileNotFoundError:
                print("\nError: the product does not exist. Add the product first\n")
           
    except FileNotFoundError:
                print("Invalid input. Try again")
                
    pass

def main_menu():
    while True:
        print("\nInventory Management System")
        print("1. Add a New Product")
        print("2. Update Product Details")
        print("3. Add a New Supplier")
        print("4. Place an Order")
        print("5. View Inventory")
        print("6. Generate Reports")
        print("7. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            add_product()
        elif choice == '2':
            update_product()
        elif choice == '3':
            add_supplier()
        elif choice == '4':
            place_order()
        elif choice == '5':
            view_inventory()
        elif choice == '6':
            generate_reports()
        elif choice == '7':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")