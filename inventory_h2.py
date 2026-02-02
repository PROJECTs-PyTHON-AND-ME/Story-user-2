# Data validation with conditionals.
inventory = [] # Global variable that creates a list.
def main(): # Function that allows you to create an interactive menu from a list.
    while True:
        print("\n Inventory Menu")
        print("1. Add product")
        print("2. Show inventory")
        print("3. Calculate statistics")
        print("0. Exit")
        option = input("Select an option: ").strip()

        if option == '1':
            add_product()
        elif option == '2':
            show_inventory()
        elif option == '3':
            if not inventory:
                print("Inventory is empty. Statistics cannot be calculated.")
            else:
                calculate_statistics()
        elif option == '0':
            print("Leaving inventory")
            break
        else:
            print("Invalid option. Please try again.")

# Implement a loop for multiple records.
def add_product():
    while True: # Loop that allows you to add a product.
        name = input("Enter the name of the product: ").strip()
        if name == "":
            print("The name cannot be empty. Please try again.")
            continue
        elif name.isdigit():
            print("The name cannot be a number. Please try again.")
            continue
        break

    while True: # Loop that allows you to add a markup to an added product.
        try:
            price = float(input("Enter the product price: "))
            if price < 0:
                print("The price cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid value. Please enter a number.")
    
    while True: # Loop that allows you to add the quantity to an added product.
        try:
            quantity = int(input("Enter the product quantity: "))
            if quantity < 0:
                print("The quantity cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    product = {"name": name, "price": price, "quantity": quantity}
    inventory.append(product) # append = Adds elements to the end of a list.
    print(f"{name} Added product successfully.") 

# Calculate basic statistics.
def calculate_statistics():
    total_products = len(inventory) # len = Get the length of the list.
    value_total = sum(p['price'] * p['quantity'] for p in inventory) # sum = Add up all the numerical elements.
    average_price = value_total / total_products if total_products > 0 else 0
    print("\n Statistics")
    print(f"Total products: {total_products}")
    print(f"Total inventory value: {value_total:,.2f}")
    print(f"Average product price: {average_price:,.2f}")

# Display all products in inventory.
def show_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    
    print("\n Current Inventory")
    for i, p in enumerate(inventory, 1):
        print(f"{i:2d}. {p['name']:<25} ${p['price']:8.2f} * {p['quantity']:3d} = ${p['price'] * p['quantity']:,.2f}")

if __name__ == "__main__": 
    main()  # Call to main function to start the program.