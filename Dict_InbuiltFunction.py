my_dict = {"apple": 1, "banana": 2, "cherry": 3} #Removes all elements from the dictionary.
my_dict.clear()
print(my_dict)  # Output: {}


my_dict = {"apple": 1, "banana": 2, "cherry": 3} #Returns a shallow copy of the dictionary.
copied_dict = my_dict.copy()
print(copied_dict)  # Output: {'apple': 1, 'banana': 2, 'cherry': 3}


keys = ["apple", "banana", "cherry"] #Returns a new dictionary with the specified keys and the given value.
value = 0
new_dict = dict.fromkeys(keys, value)
print(new_dict)  # Output: {'apple': 0, 'banana': 0, 'cherry': 0}


my_dict = {"apple": 1, "banana": 2} #Returns the value for the specified key if the key exists in the dictionary. If the key is not found, it returns the default value (optional).
print(my_dict.get("apple"))  # Output: 1
print(my_dict.get("grapes", "Not Found"))  # Output: Not Found


my_dict = {"apple": 1, "banana": 2}# Returns a view object that displays a list of dictionary's key-value tuple pairs.
print(my_dict.items())  # Output: dict_items([('apple', 1), ('banana', 2)])


my_dict = {"apple": 1, "banana": 2}
print(my_dict.keys())  # Output: dict_keys(['apple', 'banana'])


my_dict = {"apple": 1, "banana": 2}
value = my_dict.pop("apple")##Removes and returns the value for the specified key
print(value)  # Output: 1
print(my_dict)  # Output: {'banana': 2}


my_dict = {"apple": 1, "banana": 2}
item = my_dict.popitem()#Removes and returns a random (key, value) pair from the dictionary. If the dictionary is empty, it raises a KeyError.
print(item)  # Output: ('banana', 2)
print(my_dict)  # Output: {'apple': 1}


my_dict = {"apple": 1, "banana": 2} #Returns the value of a key if it exists. If it doesn't, inserts the key with a specified default value.
print(my_dict.setdefault("cherry", 3))  # Output: 3 (cherry key is added)
print(my_dict)  # Output: {'apple': 1, 'banana': 2, 'cherry': 3}


my_dict = {"apple": 1, "banana": 2} #Updates the dictionary with elements from another dictionary or iterable of key-value pairs. It adds new keys and updates existing keys.
my_dict.update({"cherry": 3, "banana": 4})
print(my_dict)  # Output: {'apple': 1, 'banana': 4, 'cherry': 3}


my_dict = {"apple": 1, "banana": 2} #Returns a view object that displays a list of all the values in the dictionary.
print(my_dict.values())  # Output: dict_values([1, 2])


my_dict = {"apple": 1, "banana": 2} #del (not a method, but an operator used for deleting key-value pairs) ,Deletes a specified key from the dictionary.
del my_dict["apple"]
print(my_dict)  # Output: {'banana': 2}


my_dict = {"apple": 1, "banana": 2} #Checks if the dictionary contains a specific key. This is used by the in operator.
print("apple" in my_dict)  # Output: True
print("grapes" in my_dict)  # Output: False

#4. Create a dictionary to store word frequencies.
# Print the dictionary.


words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)


#5.Extract and print only the titles of books with more than 2 copies.
library = {
    "The Catcher in the Rye": 1,
    "To Kill a Mockingbird": 4,
    "1984": 3,
    "Pride and Prejudice": 6,
}


available_books = [title for title, copies in library.items() if copies > 2]
print(available_books)


#6You have two dictionaries of products and their prices from two stores. Merge them into one dictionary.
store1 = {"apple": 1.5, "banana": 0.8}
store2 = {"cherry": 2.0, "apple": 1.6}


# Merge the two dictionaries (store2 overwrites store1 for common keys)
merged_store = {**store1, **store2}


print("Merged Store:", merged_store)


#7.You are given a dictionary of countries and their capitals. Find the country for a given capital.
countries = {"India": "New Delhi", "USA": "Washington", "France": "Paris"}


# Find the country for a given capital
capital = "Paris"
country = [key for key, value in countries.items() if value == capital]
print(country)
#print(f"Country for capital {capital}:", country[0] if country else "Not Found")


#8You have a dictionary of students and their marks. Sort the dictionary by marks in descending order.


students = {"Alice": 85, "Bob": 75, "Charlie": 95, "David": 80}


sorted_students = dict(sorted(students.items(), key=lambda x: x[1], reverse=True))


print(sorted_students)


#9You are given a dictionary where student names are keys, and their subjects are values. Group students by subjects.


students = {
    "Alice": "Math",
    "Bob": "Science",
    "Charlie": "Math",
    "David": "Science",
}


# Group students by subjects
subjects = {}
for student, subject in students.items():
    subjects.setdefault(subject, []).append(student)


print("Students Grouped by Subject:", subjects)



#1. Add a new employee "Eve" with a salary of 70000.
# Remove "Bob" from the directory.
# Check if "Alice" is in the directory.
# Print the updated directory.


employess = {"Alice":50000, "Bob":45000, "Charlie":60000}


employess["Eve"]=70000


employess.pop("Bob")


is_alice_present = "Alice" in employess


print(employess)
print(is_alice_present)


#2. Update the stock of "apples" to 50.
# Add a new product "oranges" with a stock of 20.
# Check if "bananas" are available.
# Remove "grapes" from the inventory if it exists.


fruits = {"apples":30, "bananas":25, "grapes":15}


fruits["apples"]=50


fruits["oranges"]=20


are_bananas_available = "bananas" in fruits
print(are_bananas_available)
print(fruits)
fruits.pop("grapes")
print(fruits)


#3. Find the student with the highest grade.
# Print their name and grade.


grades = {"Alice": 85, "Bob": 75, "Charlie": 95, "David": 80}


highest_grader = max(grades, key=grades.get)
highest_grade = grades[highest_grader]


print(highest_grader)
print(highest_grade)



