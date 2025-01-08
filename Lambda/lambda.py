# A lambda function is a small anonymous function.A lambda function can take any number of arguments, but can only have one expression.
# Syntax : lambda arguments : expression

#simple example
x = lambda a : a + 10
print("Simple example of lambda function:", x(10))

xa = lambda a : a
print("Simple example of lambda function:", xa(1))

#lambda with multiple arguments
xaa = lambda a, b : a * b
print("Example of multiple arguments in lambda:", xaa(5, 5))

xy = lambda a, b, c : a + b + c
print("Example of multiple arguments in lambda:", xy(1, 2, 3))

calc = lambda x, y: {x + y, x * y}
val = calc(6, 7)
print("Example of multiple arguments in lambda:", val)
print(type(calc))
print(type(val))

#lambda with another function
def myfunc(n):
    return lambda a : a * n
multiply = myfunc(5)
print("Example of lambda with another function:", multiply(10))

def anothermyFunc(n):
    return lambda a : a * n
multiply1 = anothermyFunc(7)
multiply2 = anothermyFunc(9)
print("Example of lambda with another function:", multiply1(10))
print("Example of lambda with another function:", multiply2(8))

#lambda with string inbuilt function
s1 = "Aktiv"
string = lambda s1 : s1.upper()
print("Lambda with string inbuilt function:", string(s1))

#lambda with conditional checking
# Example: Check if a number is positive, negative, or zero

y = lambda x: "Postive" if x > 0 else "Negative" if x < 0 else "Zero"
print("Using lambda Check if a number is positive, negative, or zero:", y(50))  
print("Using lambda Check if a number is positive, negative, or zero:", y(-50))  
print("Using lambda Check if a number is positive, negative, or zero:", y(0))  

# Lambda with List Comprehension

l_lc = [lambda arg=x: arg * 10 for x in range(1,10)]
for i in l_lc:
    print("Lambda with List Comprehension:", i())
    
# Lambda with if-else
# Example: Check if a number is even or odd
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print("This number is:", check(100))
print("This number is:", check(101))

# Using lambda with filter()
# Example: Filter even numbers from a list
lst = [10, 21, 34, 43, 67, 12, 0]
even = filter(lambda x: x % 2 == 0, lst)
print("Example of lambda with filter function without converting to filter:", even)
print("Example of lambda with filter function:", list(even))

# Using lambda with map()
# Example: Double each number in a list
lst = [10, 20, 30, 40, 50]
lst1 = map(lambda x: x * 2, lst)
print("Example of lambda with map function:", list(lst1))

# Using lambda with reduce()
# Example: Find the product of all numbers in a list
from functools import reduce

lst3 = [10, 20, 30, 40]
lst4 = reduce(lambda x, y: x * y, lst3)
print("Example of lambda with reduce function:", lst4)
