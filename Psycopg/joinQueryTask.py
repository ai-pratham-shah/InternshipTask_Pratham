import psycopg2
 
DB_NAME = "task"
DB_USER = "odoo"
DB_PASS = "odoo"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"
conn = psycopg2.connect(database=DB_NAME,
                        user=DB_USER,
                        password=DB_PASS,
                        host=DB_HOST,
                        port=DB_PORT)
'''print("Database connected successfully")'''

cur = conn.cursor()
cur.execute("""
            CREATE TABLE customers (
                id serial PRIMARY KEY,
                name VARCHAR(100),
                email VARCHAR(100))
            """)

cur.execute("""
            CREATE TABLE products (
                id serial PRIMARY KEY,
                name VARCHAR(100),
                price INT)
            """)
            
cur.execute("""
            CREATE TABLE orders (
                id serial PRIMARY KEY,
                customer_id INT,
                product_id INT,
                quantity INT,
                order_date DATE,
                FOREIGN KEY (id) REFERENCES customers(id),
                FOREIGN KEY (id) REFERENCES products(id))
            """)
                
cur.execute (""" 
             INSERT INTO customers (id, name, email) 
             VALUES (1, 'Alice', 'alice@email.com'),
             (2, 'Bob', 'bob@email.com'),
             (3, 'Charlie', 'charlie@email.com')				
		""")    
		
cur.execute (""" 
	     INSERT INTO products (id, name, price) 
	     VALUES (1, 'Mobile', 30), 
	     (2, 'Laptop', 70), 
	     (3, 'TV', 90)
	     """)                

cur.execute (""" 
	     INSERT INTO orders (id, customer_id, product_id, quantity, order_date) 
	     VALUES (1, 1, 2, 1, '2025-01-01'), 
	     (2, 2, 1, 3, '2025-01-02') 
	    """)       

'''Query 1: LEFT JOIN
    • Retrieves all customers, whether they have placed orders or not.
    • Joins the customers table with orders and products using LEFT JOIN.
    • Uses COALESCE to handle NULL values for customers without orders, showing 0 for their total order value.  - R&D on the COALESCE and 
use that on query  '''   
         
cur.execute ("""SELECT customers.name,customers.email,
		COALESCE(orders.quantity, 0) from customers
	    	left join products on customers.id = products.id
	    	left join orders on customers.id = orders.customer_id
	    """)
output_query_1 = cur.fetchall()
query_1 = 'INSERT INTO leftjoin (name, email, quantity) values (%s, %s, %s)'
for i in output_query_1:
    print(i)
    cur.execute(query_1, i)  

''' Query 2: RIGHT JOIN
    • Retrieves all products and filters to include only those that have never been ordered.
    • Uses a RIGHT JOIN between products and orders, with a WHERE o.id IS NULL clause to identify unmatched rows. '''
    
cur.execute ("""
	    SELECT products.name 
	    from orders
	    RIGHT JOIN products ON products.id = orders.id
	    WHERE orders.id is null	
	    """)

output_query_2 = cur.fetchone()
print(output_query_2)
query_2 = 'INSERT INTO rightjoin (p_name) values (%s)'  
cur.execute(query_2, output_query_2)

''' Query 3: INNER JOIN
    • Retrieves all high-value orders (where product price > $50).
    • Joins orders, customers, and products with an INNER JOIN.
    • Calculates the total value of each order (p.price * o.quantity) '''

cur.execute ("""
	 SELECT customers.name, customers.email,products.price*orders.quantity 
	 FROM products
	 INNER JOIN customers on customers.id = products.id
	 INNER JOIN orders on orders.product_id = products.id
	 where products.price >= 50
	  """)

output_query_3 = cur.fetchall()
print(output_query_3)
query_3 = 'INSERT INTO innerjoin (c_name, c_email, price_multiply_order) values (%s, %s, %s)'  
for i in output_query_3:
    print(i)
    cur.execute(query_3, i)	    
      
conn.commit()
'''print("Table created successfully.")'''
conn.close()




""" \copy (SELECT * FROM employees) to '/home/odoo/Documents/demo.csv' WITH DELIMITER ',' CSV header; """





