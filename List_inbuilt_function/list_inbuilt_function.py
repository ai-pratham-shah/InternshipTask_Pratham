lst = [1, 2]
lst.append(3) #  adds a single element to the end of a list.
print(lst)  # Output: [1, 2, 3]


lst = [1, 2]
lst.extend([3, 4])
print(lst)  # Output: [1, 2, 3, 4]


lst = [1, 3]
lst.insert(1, 2)
print(lst)  # Output: [1, 2, 3]


lst = [1, 2, 3, 2]
lst.remove(2)
print(lst)  # Output: [1, 3, 2]


lst = [1, 2, 3]
item = lst.pop(1)
print(lst)  # Output: [1, 3]
print(item)  # Output: 2


lst = [1, 2, 3]
lst.clear()
print(lst)  # Output: []


lst = [1, 2, 3, 2]
print(lst.index(2))  # Output: 1
print(lst.index(2, 2))  # Output: 3


lst = [1, 2, 2, 3]
print(lst.count(2))  # Output: 2


# =>sort(key=None, reverse=False)
# Purpose: Sorts the list in place. By default, sorts in ascending order. Use key for custom sorting logic and reverse=True for descending order.
lst = [3, 1, 2]
lst.sort()
print(lst)  # Output: [1, 2, 3]
lst.sort(reverse=True)
print(lst)  # Output: [3, 2, 1]


lst = [1, 2, 3]
lst.reverse()
print(lst)  # Output: [3, 2, 1]


lst = [1, 2, 3]
lst_copy = lst.copy()
print(lst_copy)  # Output: [1, 2, 3]




#1. Create a list of integers [5, 10, 15, 20].
# Add the number 25 at the end of the list.
# Insert the number 12 at index 2.
# Add another list [30, 35] to the current list.
# Print the final list.


lst = [5,10,15,20]
lst.append(25)
lst.insert(2,12)
lst.extend([30,35])
print(lst)


#2. Create a list of words: ["apple", "banana", "apple", "cherry", "apple", "banana"].
# Count how many times the word "apple" appears.
# Remove the first occurrence of "banana".
# Print the updated list and the count of "apple".


lst = ["apple", "banana", "apple", "cherry", "apple", "banana"]
print(lst.count("apple"))
lst.remove("banana")
print(lst)


# To remove both occurrences of "banana" from the list lst, you can use a loop or list comprehension. Here's how:
#USING WHILE LOOP
lst = ["apple", "banana", "apple", "cherry", "apple", "banana"]


while "banana" in lst:
    lst.remove("banana")
#lst = [i for i in lst if i != "banana"] list comprehension
print(lst)  # Output: ['apple', 'apple', 'cherry', 'apple']


#Using List Comprehension
lst = ["apple", "banana", "apple", "cherry", "apple", "banana"]


lst = [item for item in lst if item != "banana"]


print(lst)  # Output: ['apple', 'apple', 'cherry', 'apple']


#Using Filter Function
lst = ["apple", "banana", "apple", "cherry", "apple", "banana"]


lst = list(filter(lambda x: x != "banana", lst))


print(lst)  # Output: ['apple', 'apple', 'cherry', 'apple']




#3. Create a list of integers [40, 10, 20, 50, 30].
# Sort the list in ascending order.
# Reverse the sorted list.
# Add the number 60 to the reversed list.
# Print the final list.


lst = [40,10,20,50,30]
lst.sort()
print(lst)
lst.reverse()
print(lst)
lst.append(60)
print(lst)


#4. Create a list of tuples representing student names and their marks: [("Alice", 85), ("Bob", 75), ("Charlie", 95), ("David", 80)].
# Sort the list in descending order of marks.
# Extract only the names of the students into a new list.
# Print both the sorted list and the list of names.


lst = [("Alice",85), ("Bob", 75), ("Charlie", 95), ("David", 80)]
lst.sort(key=lambda x: x[1],reverse=True)
print(lst)
names = [lst[0] for lst in lst]
print(names)


#5. Create a list of numbers [1, 2, 3, 4, 5, 6].
# Find the index of the number 4.
# Insert the number 10 right after 4.
# Print the updated list.


lst = [1,2,3,4,5,6]
print(lst.index(4))
lst.insert(4, 10)
print(lst)




#6. Create a list of your favorite fruits: ["mango", "apple", "grape"].
# Make a copy of the list.
# Clear all elements from the original list.
# Print both the original and copied lists.


lst = ["mango","apple","grape"]
lst_copy = lst.copy()
print(lst)
lst.clear()
print(lst)
print(lst_copy)


#7. Create a list of numbers: [10, 20, 30, 40, 50, 60].
# Add the number 25 between 20 and 30.
# Remove the number 60.
# Count how many numbers are greater than 25 in the list.
# Reverse the list.
# Print the final list and the count.


# Step 1: Create a list of numbers
numbers = [10, 20, 30, 40, 50, 60]


# Step 2: Add the number 25 between 20 and 30
numbers.insert(numbers.index(30), 25)


# Step 3: Remove the number 60
numbers.remove(60)


# Step 4: Count how many numbers are greater than 25
count_greater_than_25 = sum(1 for num in numbers if num > 25)


# Step 5: Reverse the list
numbers.reverse()


# Step 6: Print the final list and the count
print("Final list:", numbers)
print("Count of numbers greater than 25:", count_greater_than_25)




#8. Create two lists of numbers: [15, 10, 5] and [30, 25, 20].
# Extend the first list with the second list.
# Sort the combined list in descending order.
# Print the final list.


lst1 = [15,10,5]
lst2 = [30,25,20]
lst2.extend(lst1)
lst2.sort(reverse=True)
print(lst2)




.count(4))
while 4 in lst:
    lst.remove(4)
print(lst)




#10. Create a to-do list: ["study", "exercise", "grocery shopping"].
# Add a new task "cleaning".
# Mark the task "exercise" as completed by removing it from the list.
# Insert "reading" as the second task.
# Sort the tasks alphabetically and print the updated list.


lst = ["study","exercise","grocery shopping"]
lst.append("cleaning")
lst.remove("exercise")
lst.insert(2,"reading")
lst.sort()
print(lst)


#11. Write a program to find and print common elements between two lists:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]


# Convert the lists to sets and find the intersection
common_elements = set(list1) & set(list2)


# Convert the result back to a list (optional)
common_elements = list(common_elements)


print("Common elements:", common_elements)

