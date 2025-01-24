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

cur = conn.cursor()

# Create tables

cur.execute(""" 
CREATE TABLE customers (
    id serial PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
) 
""")

cur.execute(""" 
CREATE TABLE products (
    id serial PRIMARY KEY,
    name VARCHAR(100),
    price INT
)
""")

cur.execute(""" 
CREATE TABLE orders (
    id serial PRIMARY KEY,
    customer_id INT REFERENCES customers(id),
    product_id INT REFERENCES products(id),
    quantity INT,
    order_date DATE
)
""")

# Insert data
cur.execute(""" 
INSERT INTO customers (name, email)
VALUES 
    ('Alice', 'mailto:alice@email.com'),
    ('Bob', 'mailto:bob@email.com'),
    ('Charlie', 'mailto:charlie@email.com')
""")

cur.execute(""" 
INSERT INTO products (name, price)
VALUES 
    ('Mobile', 30),
    ('Laptop', 70),
    ('TV', 90)
""")

cur.execute(""" 
INSERT INTO orders (customer_id, product_id, quantity, order_date)
VALUES 
    (1, 2, 1, '2025-01-01'),
    (2, 1, 3, '2025-01-02')
""")

# LEFT JOIN Query
cur.execute("""
    SELECT customers.name, customers.email, COALESCE(products.name, '--'), COALESCE(orders.quantity, 0)
    FROM customers
    LEFT JOIN orders ON customers.id = orders.customer_id
    LEFT JOIN products ON products.id = orders.product_id
""")
output_query_1 = cur.fetchall()
print("LEFT JOIN: ", output_query_1)


cur.execute("""
CREATE TABLE leftjoin (
    name VARCHAR(100),
    email VARCHAR(100),
    product_name VARCHAR(100),
    quantity INT
)
""")
query_1 = 'INSERT INTO leftjoin (name, email, product_name, quantity) VALUES (%s, %s, %s, %s)'
for i in output_query_1:
    cur.execute(query_1, i)

# RIGHT JOIN Query
cur.execute("""
    SELECT products.name
    FROM products
    LEFT JOIN orders ON products.id = orders.product_id
    WHERE orders.id IS NULL
""")
output_query_2 = cur.fetchall()
print("RIGHT JOIN: ",output_query_2)

cur.execute("""
CREATE TABLE rightjoin (
    p_name VARCHAR(100)
)
""")
query_2 = 'INSERT INTO rightjoin (p_name) VALUES (%s)'
for i in output_query_2:
    cur.execute(query_2, i)

# INNER JOIN Query
cur.execute("""
    SELECT customers.name, customers.email, products.price * orders.quantity
    FROM products
    INNER JOIN orders ON orders.product_id = products.id
    INNER JOIN customers ON customers.id = products.id
    WHERE products.price > 50
""")
output_query_3 = cur.fetchall()
print("INNER JOIN: ",output_query_3)

cur.execute("""
CREATE TABLE innerjoin (
    c_name VARCHAR(100),
    c_email VARCHAR(100),
    total_order_value INT
)
""")
query_3 = 'INSERT INTO innerjoin (c_name, c_email, total_order_value) VALUES (%s, %s, %s)'
for i in output_query_3:
    cur.execute(query_3, i)

# Commit the changes
conn.commit()

# Exporting data to CSV files
#
# cur.execute("""
# COPY (SELECT * FROM leftjoin) TO '/home/odoo/pratham/leftjoin.csv' WITH DELIMITER ',' CSV HEADER
# """)
# cur.execute("""
# COPY (SELECT * FROM rightjoin) TO '/home/odoo/pratham/rightjoin.csv' WITH DELIMITER ',' CSV HEADER
# """)
# cur.execute("""
# COPY (SELECT * FROM innerjoin) TO '/home/odoo/pratham/innerjoin.csv' WITH DELIMITER ',' CSV HEADER
# """)

# Commit changes and close the connection
#conn.commit()
conn.close()

