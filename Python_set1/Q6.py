class Storemanagement_system:
    def __init__(self):
        self.store_data = {}
        
    def create_shelf(self):
        """ Create a new shelf. """
        shelf_name = input("Enter the new shelf name:").strip()
        if shelf_name in self.store_data:
            print(f"Shelf {shelf_name} already exists.")
        else:
            self.store_data[shelf_name] = {}
            print(f"shelf {shelf_name} created successfully.")
        print(self.store_data)    
    def add_product(self):
        """ Add a product, set category, and enter cost prices. """
        shelf_name = input("Enter the shelf name:").strip()
        if shelf_name not in self.store_data:
            print("Shelf does not exist.Create the shelf first.")
            return
        product_name = input("Enter the product name:").strip()
        if product_name not in self.store_data[shelf_name]:
            self.store_data[shelf_name][product_name] = {"Category":None, "Cost Price": {}, "Sale Price": {}}
            print(f"Product {product_name} added to {shelf_name}")
            
        category = input(f"Enter category for '{product_name}': ").strip()
        self.store_data[shelf_name][product_name]["Category"] = category
        print(f" Category '{category}' set for {product_name}.")
        
        while True:
            month = input("Enter the month (or type 'done' to finish): ").strip().capitalize()
            if month.lower() == "done":
                break

            cost_prices = input(f"Enter cost prices for {month} (comma-separated): ").strip()
            self.store_data[shelf_name][product_name]["Cost Price"][month] = [float(x) for x in cost_prices.split(",")]

            print(f"Cost prices added for {product_name} in {month}.")

        print(self.store_data)
        
    def update_sale_price(self):
        """Update the sale price of a specific product for a given month."""
        shelf_name = input("Enter the shelf name:").strip()
        if shelf_name not in self.store_data:
            print("Shelf does not exist.")
            return
       
        product_name = input("Enter the product name:").strip()
        if product_name not in self.store_data[shelf_name]:
            print("Product does not exist.")
            return
            
        month = input("Enter the month: ").strip().capitalize()
        if month not in self.store_data[shelf_name][product_name]["Cost Price"]:
            print("No cost price data for this month.")
            return
            
        percentage = float(input("Enter the percentage increase for sale price: ").strip())
        cost_prices = self.store_data[shelf_name][product_name]["Cost Price"][month]
        sale_prices = [round(cp * (1 + percentage / 100), 2) for cp in cost_prices]
        self.store_data[shelf_name][product_name]["Sale Price"][month] = sale_prices
        
        print(f"Sale prices updated for {product_name} in {month}.")
        print(self.store_data)
        
    def update_sale_price_for_shelf(self):
        """Update sale prices for all products in a shelf by a given percentage."""
        shelf_name = input("Enter the shelf name: ").strip()
        if shelf_name not in self.store_data:
            print(" Shelf does not exist.")
            return
        
        percentage = float(input("Enter the percentage increase for sale price: ").strip())

        for product_name, product_data in self.store_data[shelf_name].items():
            for month, cost_prices in product_data["Cost Price"].items():
                if cost_prices:
                    sale_prices = [round(cp * (1 + percentage / 100), 2) for cp in cost_prices]
                    self.store_data[shelf_name][product_name]["Sale Price"][month] = sale_prices
        
        print(f" Sale prices updated for all products in '{shelf_name}'.")
        print(self.store_data)
        
    def set_category(self):
        """Set or update the category of a product."""
        shelf_name = input("Enter the shelf name: ").strip()
        if shelf_name not in self.store_data:
            print("Shelf does not exist.")
            return

        product_name = input("Enter the product name: ").strip()
        if product_name not in self.store_data[shelf_name]:
            print("Product does not exist.")
            return

        category = input(f"Enter new category for '{product_name}': ").strip()
        self.store_data[shelf_name][product_name]["Category"] = category
        print(f"Category updated to '{category}' for {product_name}.")
        print(self.store_data)
	 
    def reset_cost_price(self):
        """Reset cost price with 0 for a given shelf, product, and month."""
        shelf_name = input("Enter the shelf name: ").strip()
        if shelf_name not in self.store_data:
            print("Shelf does not exist.")
            return

        product_name = input("Enter the product name: ").strip()
        if product_name not in self.store_data[shelf_name]:
            print("Product does not exist.")
            return

        month = input("Enter the month: ").strip().capitalize()
        if month not in self.store_data[shelf_name][product_name]["Cost Price"]:
            print("No cost price data for this month.")
            return

        self.store_data[shelf_name][product_name]["Cost Price"][month] = [0]  # Resetting to zero
        print(f"Cost prices reset to 0 for '{product_name}' in {month}.")
        print(self.store_data)
    
    def get_min_max_price(self):
        """Get the maximum or minimum cost price with the shelf name of a product."""
        product_name = input("Enter the product name: ").strip()
        price_type = input("Do you want 'max' or 'min' price? ").strip().lower()

        # Check if the user entered a valid price type
        if price_type not in ["max", "min"]:
            print(" Invalid choice. Please enter 'max' or 'min'.")
            return

        # Define the function based on the user's choice
        price_func = max if price_type == "max" else min

        min_max_price = None
        shelf_with_price = None

        # Iterate through shelves and products
        for shelf, products in self.store_data.items():
            if product_name in products:
                for month, prices in products[product_name]["Cost Price"].items():
                    if prices:  # Check if there are prices available
                        current_price = price_func(prices)

                        # Set the min/max price and shelf
                        if min_max_price is None or (price_func([min_max_price, current_price]) == current_price):
                            min_max_price = current_price
                            shelf_with_price = shelf

        # Output the result
        if min_max_price is not None:
            print(f" {price_type.capitalize()} price of '{product_name}' is {min_max_price} in '{shelf_with_price}'.")
        else:
            print(f" No cost price data found for '{product_name}'.")
    
        
    def run(self):
        """Main menu for user interaction."""
        while True:
            print("\n Store Management System")
            print("1. Create Shelf")
            print("2. Add Product, Set Category & Cost Prices")
            print("3. Update Sale Price for a Product")
            print("4. Update sale prices for all products in a shelf by a given percentage.")
            print("5. Set or update the category of a product.")
            print("6. Reset cost price with 0 for a given shelf, product, and month.")
            print("0. Exit")
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.create_shelf()
            elif choice == "2":
                self.add_product()
            elif choice == "3":
                self.update_sale_price()
            elif choice == "4":
                self.update_sale_price_for_shelf()
            elif choice == "5":
                self.set_category()
            elif choice == "6":
                self.reset_cost_price()
            elif choice == "0":
                print("Exiting Store Management System.")
                break
            else:
                print("Invalid choice. Please try again.")


store = Storemanagement_system()
store.run()

