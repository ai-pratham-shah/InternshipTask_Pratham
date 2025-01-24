''' 
3. Sales Data Analysis
Question:
You are given a list of sales data, and you need to calculate:
The total sales for the given period.
The average sales per product.
The highest-selling product.
Input:
A list of dictionaries sales_data[] where each dictionary contains:
"Product ID": An integer identifier for the product.
"Product Name": A string name for the product.
"Sale Amount": An integer sale amount.
"Sale Date": A string representing the sale date.
Output:
A dictionary containing:
"Total Sales": The total sales amount.
"Average Sales": The average sales amount per product.
"Highest-Selling Product": A dictionary with "Product ID" and "Product Name" of the
highest-selling product.
Example:
sales_data = [
{"product_id": 101, "product_name": "Smartphone", "sale_amount": 500, "sale_date": "2025-01-01"},
{"product_id": 102, "product_name": "Laptop", "sale_amount": 300, "sale_date": "2025-01-02"},
{"product_id": 101, "product_name": "Smartphone", "sale_amount": 400, "sale_date": "2025-01-03"},
{"product_id": 103, "product_name": "Smartwatch", "sale_amount": 700, "sale_date": "2025-01-04"}
]
Output:
{
"Total Sales": 1900,
"Average Sales": 475,
"Highest-Selling Product": { "product_id": 101, "product_name": "Smartphone""}
}
'''

''' class sales_data_analysis:
    def __init__(self, Product_id, product_name, sale_amount, sale_date):
        self.sales_data = []
        self.Product_id = Product_id
        self.Product_name = Product_name
        self.sale_amount = sale_amount
        self.sale_date = sale_date

    def add_data(self, Product_id, product_name, sale_amount, sale_date):
        Product_id = int(input("Enter a product id: "))
        product_name = input("Enter a product name: ")
        sale_amount = int(input("Enter a sale amount"))
        sale_date = input("Enter date(YYYY-MM-DD)")
      
    def get_data(self, Product_id, product_name, sale_amount, sale_date):
        self.sales_data.append(add_data)
                
sda = sales_data_analysis
sda.add_data(Product_id, product_name, sale_amount, sale_date)
sda.get_data(Product_id, product_name, sale_amount, sale_date) '''

'''Initialize an empty list to store product data
sales_data = []

 Loop to allow user to enter data
while True:
    
    product_id = int(input("Enter product ID: "))
    product_name = input("Enter product name: ")
    sale_amount = float(input("Enter sale amount: "))
    sale_date = input("Enter sale date (YYYY-MM-DD): ")
    
     Create a dictionary for the product and append it to the list
    product = {
        "product_id": product_id,
        "product_name": product_name,
        "sale_amount": sale_amount,
        "sale_date": sale_date
    }
    
    sales_data.append(product)
    continue_input = input("Do you want to enter another product? (yes/no): ")
    if continue_input.lower() != "yes":
        break

 Print the collected data
print("\nSales Data Entered:")
for product in sales_data:
    print(product)'''


class sales_data_analysis: 
    def __init__(self):
        self.sales_data = []
    def add_data(self):
        product_id = input("Enter a product id: ")
        if not product_id.isdigit()
            print("Id invalid")       
            return add_data()
               
        product_name = input("Enter a product name: ")  
        if not product_name.isalpha():
            print("Product invalid")
            
        sale_amount = input("Enter sale amount: ")
        if not sale_amount.isdigit():
            print("Sale amount is not valid")
            
        sale_data = input("Enter the date(YYYY-MM-DD): ")
        
      
        
        
#STEPS
''' 
CREATE ONE CLASS sales_data_analysis
	STEP1 : CREATE ONE INIT METHOD AND INITIALIZE THE ONE LIST CALLED "sales_data"
	STEP2 : CREATE ANOTHER METHOD CALLED "add_data"
		A.TAKE USER INPUT FOR PRODUCT ID AND CHECK THAT USER ENTER ONLY NECESSARY FORMAT DATA
		B.TAKE USER INPUT FOR PRODUCT NAME AND CHECK THAT USER ENTER ONLY NECESSARY FORMAT DATA
		B.TAKE USER INPUT FOR SALE AMOUNT AND CHECK THAT USER ENTER ONLY NECESSARY FORMAT DATA
		B.TAKE USER INPUT FOR SALE DATA AND CHECK THAT USER ENTER ONLY NECESSARY FORMAT DATA
 	STEP3 : ADD ALL THE DATA INTO THE LIST IN DICTIONARY FORMAT
 	STEP4 : CREATE ANOTHE FUNCION TO CALCULATE TOTAL SALES FOR THAT TAKE SALE AMOUNT FROM LIST OF DICTIONARY AND USING FOR LOOP TAKE THE 	ALL VALUES OF SALE AMOUNT AND NEED TO DO ADDITION
 	STEP5 : CREATE ANOTHER FUNCTION FOR AVERAGE AND TAKE THE OUTPUT OF TOTAL SALES AND DIVIDED BY THE TOTAL NO OF PRODUCTS
 	STEP6 : CREATE ANOTHER FUNCTION FOR HIGHEST SELLING PRODUCT FOR THAT TAKE I HAVE TO CALCULATE PRODUCT_NAME OR PRODUCT ID THAT HOW MANY TIME THAT PRODUCT NAME OR PRODUCT ID COMING IN THE LIST OF DICTIONARY.
'''     
            
        
