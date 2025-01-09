# map() : Python's map() method applies a specified function to each item of an iterable (such as a list, tuple, or string) and then returns a new iterable containing the results.

# syntax : map(function, iterable)

#Example1

# Using map() to square each element of the data list  
data = [10, 20, 30, 40] 
squares = list(map(lambda x: x ** 2, data))
print(squares)

print("-------------------------------------")

#Example2
data1 = list(map(int, input("Enter integer values: ").split()))  
print(f"Integer data = {data1}")
data2 = list(map(float, input("Enter Floating values: ").split()))  

print(f"Float data = {data2}")

print("-------------------------------------")

#Example3
base = [1,2,3,4,5]
power = [2,4,6,8,10]
answer = list(map(pow,base,power))
print(answer)

print("-------------------------------------")

# filter() - The filter() function in Python filters elements from an iterable based on a given condition or function and returns a new iterable with the filtered elements.

# syntax : filter(function, iterable)

#Example 1
# Using filter() to filter even numbers from a list  
data = [10, 20, 33, 43, 50]  
find_even = list(filter(lambda x:x % 2 == 0,data))
print("Even number:", find_even)

print("-------------------------------------")

#Example 2

names = ["Harun", "Sonu", "Harsh", "Harry", "Anu", "Hassi"]  
name_H = list(filter(lambda x:x[0]=='H', names))

print("Names start with H:", name_H)

