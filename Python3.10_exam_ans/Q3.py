def get_sales_data():
    """
    Function to take user input for sales data.
    The user will enter details like Product ID, Product Name, Sale Amount, and Sale Date.
    Returns a list of sales records entered by the user.
    """
    sales_data = []
    num_entries = int(input("Enter the number of sales records: "))

    for _ in range(num_entries):
        product_id = int(input("Enter Product ID: "))
        product_name = input("Enter Product Name: ")
        sale_amount = int(input("Enter Sale Amount: "))
        sale_date = input("Enter Sale Date (YYYY-MM-DD): ")

        sales_data.append({
            "product_id": product_id,
            "product_name": product_name,
            "sale_amount": sale_amount,
            "sale_date": sale_date
        })
    
    return sales_data


def calculate_total_sales(sales_data):
    """
    Function to calculate the total sales amount.
    Takes the sales_data list as input.
    Returns the total sales amount.
    """
    total_sales = sum(sale["sale_amount"] for sale in sales_data)
    return total_sales


def calculate_average_sales(sales_data):
    """
    Function to calculate the average sales per product.
    Takes the sales_data list as input.
    Returns the average sales amount.
    """
    if not sales_data:
        return 0  # If no sales data is available, return 0
    
    total_sales = calculate_total_sales(sales_data)
    average_sales = total_sales / len(sales_data)
    return round(average_sales, 2)


def find_highest_selling_product(sales_data):
    """
    Function to determine the highest-selling product.
    Takes the sales_data list as input.
    Returns a dictionary containing the product_id and product_name of the highest-selling product.
    """
    product_sales = {}

    for sale in sales_data:
        product_id = sale["product_id"]
        product_name = sale["product_name"]
        sale_amount = sale["sale_amount"]

        if product_id in product_sales:
            product_sales[product_id]["total_sales"] += sale_amount
        else:
            product_sales[product_id] = {"product_name": product_name, "total_sales": sale_amount}

    highest_selling_product = max(product_sales.items(), key=lambda x: x[1]["total_sales"])

    return {"product_id": highest_selling_product[0], "product_name": highest_selling_product[1]["product_name"]}


def main():
    """
    Main function to run the sales analysis program.
    It collects sales data from the user and calculates total sales, average sales, and highest-selling product.
    Finally, it prints the results.
    """
    sales_data = get_sales_data()
    
    # Total Sales
    total_sales = calculate_total_sales(sales_data)
    print("\nTotal Sales:", total_sales)

    # Average Sales
    average_sales = calculate_average_sales(sales_data)
    print("Average Sales per Product:", average_sales)

    # Highest Selling Product
    highest_selling_product = find_highest_selling_product(sales_data)
    print("Highest-Selling Product:", highest_selling_product)


if __name__ == "__main__":
    main()

