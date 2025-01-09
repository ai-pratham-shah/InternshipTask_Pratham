# List comprehension
myl = [x**2 for x in [1,2,3,4,5]]
print("Square of each number through list comprehension :", myl)

print("-----------------------------------------")

even_numbers = [num for num in range(1, 10) if num % 2 == 0 ]
print("Even numbers through list comprehension:", even_numbers)

print("-----------------------------------------")

# List Comprehension with String
word = "Python"
vowel = "aeiou"
result = [char for char in word if char in vowel]
print(result)

print("-----------------------------------------")

# Nested list comprehension

nested_list_comprehension = [[i * j for j in range(1, 6)] for i in range(2, 5)]
print(nested_list_comprehension)
