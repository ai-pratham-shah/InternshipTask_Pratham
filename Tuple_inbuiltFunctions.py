t = (1, 2, 3, 2, 4)
print(t.count(2))  # Output: 2

t = (10, 20, 30, 20, 40)
print(t.index(20))  # Output: 1

t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)  # Output: (1, 2, 3, 4)

t = (1, 2)
print(t * 3)  # Output: (1, 2, 1, 2, 1, 2)

t = (10, 20, 30)
print(20 in t)  # Output: True
print(40 not in t)  # Output: True

t = (1, 2, 3)
for item in t:
    print(item)

t = (1, 2, 3, 4, 5)
print(t[1:4])  # Output: (2, 3, 4)

t = (1, 2, 3)
print(len(t))  # Output: 3

t = (10, 20, 30)
print(max(t))  # Output: 30
print(min(t))  # Output: 10


t = (1, 2, 3)
print(sum(t))  # Output: 6

t = (3, 1, 2)
print(sorted(t))  # Output: [1, 2, 3]

t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst)  # Output: [1, 2, 3, 4]

lst = [1, 2, 3]
t = tuple(lst)
print(t)  # Output: (1, 2, 3)

#1.Find how many times "apple" appears in the inventory.
inventory = [("apple", 30), ("banana", 50), ("cherry", 20), ("apple", 40), ("banana", 10)]

apple_count = sum(1 for item in inventory if item[0] == "apple")

print(apple_count)

#2.Write a program that finds the index of "Charlie" in the list of employees.

employees = [("Alice", 50000), ("Bob", 45000), ("Charlie", 60000), ("David", 70000)]

# Find the index of "Charlie"
charlie_index = next(index for index,employee in enumerate(employees) if employee[0] == "Charlie")

print("The index of Charlie is:", charlie_index)

#3.Find the highest and lowest sales amount and the salesperson who made the sale.
sales_data = [("John", 500), ("Mary", 750), ("Alice", 600), ("Bob", 400)]

# Finding the highest sale
max_sale = max(sales_data, key=lambda x: x[1])
# Finding the lowest sale
min_sale = min(sales_data, key=lambda x: x[1])

print("Highest sale:", max_sale)  # ('Mary', 750)
print("Lowest sale:", min_sale)   # ('Bob', 400)

#4.Sort the students by their marks in descending order and display their names along with marks.
students = [("Alice", 85), ("Bob", 75), ("Charlie", 95), ("David", 80)]

# Sort students by marks in descending order
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)

print("Sorted students by marks (descending):")
for student in sorted_students:
    print(student)

#5. Remove "Rome" from the list of destinations.
destinations = [("Paris", 5), ("London", 4), ("Rome", 3), ("Tokyo", 7)]
destinations = [destination for destination in destinations if destination[0] != "Rome"]
print(destinations)

# Use filter to remove "Rome"
destinations = list(filter(lambda x: x[0] != "Rome", destinations))
print("Updated destinations:", destinations)

#6.Check if "Shampoo" is in the list of products.
products = [("Shampoo", 5.99), ("Toothpaste", 2.49), ("Soap", 1.99), ("Conditioner", 6.49)]

# Check if "Shampoo" is in the list of products
#product_exists = any(product[0] == "Shampoo" for product in products)
product_exists = any("Shampoo" in product for product in products)
print("Is Shampoo available in the store?", product_exists)
#7.Count how many times "Math" appears in the list of courses.
courses = [("Math", 30), ("Physics", 20), ("Chemistry", 25), ("Math", 40), ("Biology", 15)]
count_math = sum(1 for course in courses if course[0]=="Math")
print(count_math)

#8.Extract and print only the book titles from the library list.
library = [("The Catcher in the Rye", 5), ("To Kill a Mockingbird", 2), ("1984", 4), ("Pride and Prejudice", 6)]

books_titlw = [book[0] for book in library]
print(books_titlw)

