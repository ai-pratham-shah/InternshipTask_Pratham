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

def find_highest_selling_product(sales_data):
    """
    Function to determine the highest-selling product.
    Takes the sales_data list as input.
    Returns a dictionary containing the highest selling product date
    """
    product_sales = {}

    for sale in sales_data:
        product_id = sale["product_id"]
        sale_date = sale["sale_date"]
        sale_amount = sale["sale_amount"]

        if product_id in product_sales:
            product_sales[product_id]["total_sales"] += sale_amount
        else:
            product_sales[product_id] = {"highest selling day":sale_date, "total_sales": sale_amount}

    highest_selling_day = max(product_sales.items(), key=lambda x: x[1]["total_sales"])
    return {"sale_date": highest_selling_day[1]}

def main():
    """
    Main function to run the sales program.
    It collects sales data from the user and calculates total sales per day and highest-selling .
    """
    sales_data = get_sales_data()
    highest_selling_product = find_highest_selling_product(sales_data)
    print(highest_selling_product)
if __name__ == "__main__":
    main()


