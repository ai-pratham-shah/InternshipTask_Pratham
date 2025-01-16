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
print("Database connected successfully")

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
                order_dat DATE)
            """)
                  
cur.execute (""" 
             INSERT INTO customers (id, name, email) 
             VALUES (1, "Alice", "alice@email.com"),
             (2, "Bob", "bob@email.com"),
             (3, "Charlie", "charlie@email.com")				
		""")                 
                        
conn.commit()
print("Table created successfully.")
#conn.close()




