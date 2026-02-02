# Inventory User History 2.

## Description.
This Python script implements an interactive inventory management system.
It allows you to add products with validations, display the complete inventory, calculate basic statistics (total products, total value and average price), and exit the program.
It uses a list of dictionaries to store the products.

## Requirements.
- Python 3 installed on the system.

## Usage.
1. Run the `inventory_h2.py` script in a Python environment.
2. Select an option from the menu.
    -**1. Add product**: Enter name, price and quantity with validations.
    -**2. Show inventory**: Shows alll registered products.
    -**3. Calculate statistics**: Calculates and shows total products, total value and average price (Only if there are products).
    -**0. Exit**: Ends the program.
3. Repeat the options as needed.

## Example of Execution.

```
Inventory Menu
1. Add product
2. Show inventory
3. Calculate statistics
0. Exit

Select an option: 1
Enter the product name: Apple
Enter the product price: 2.50
Enter the product quantity: 10

Select an option: 2
1. Name Apple, Price: 2.50, Quantity: 10

Select an option: 3
Total products: 1 
Total inventory value: 25.00
Average price per product: 25.00

Select an option: 0
Exiting inventory
```

## Validations.
- Name: Cannot be empty or contain numbers.
- Price: Must be a positive number with decimals.
- Quantity: Must be a positive integer.
- Statistics: Only calculated if there are products in inventory.

## Notes.
- Inventory is stored in memory and is lost when yoou exit the program.
- Uses loops to validate entries and a menu based on conditionals.
- Separate functions for each operation for better organization.