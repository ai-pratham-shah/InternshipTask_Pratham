# -> The min() and max() are built-in functions of Python programming language to find the smallest and the largest elements in any iterable.

# -> These functions come in handy when working with any iterables like lists, tuples, sets, and dictionaries in Python.

# -> The min() function takes an iterable as an argument and returns the smallest item in the iterable.

# -> The max() function accepts an iterable as an input and returns the iterable's largest item.

 # -> The basic syntax for both functions is 'max(iterable)' and 'min(iterable)'.

# -> The min() and max() functions in Python provide a convenient way to find the smallest and largest values in a given dataset or collection. Whether you're working with numbers, strings, or more complex objects, these functions offer flexibility and versatility.

l=[4,7,9,10,45,21,46,67,23]
print(l)
print(type(l))
print("min=", min(l))
print("max=", max(l))
print("------------------------------")
float_numbers = [3.14, 2.718, 1.618, 0.577, 2.236]
print(float_numbers)
max_float = max(float_numbers) 
print("Max =", max_float)
min_float = min(float_numbers)
print("Min =", min_float)
print("------------------------------")
l=[4,7,9,10,45,21,46,67,23]
larg = l[0]
small =l[0]

for num in l:
    if num > larg:
        larg = num
    if num < small:
        smallest = num
print("Largest:", larg)
print("Smallest:", small)  

print("------------------------------")

l1=[4,6 ,9,35,12,23,10]
l2=[0,9,29,56,23,56,18]
l3=[1,2,3,4,5,6,7,8,9,10] 
max_all = max(l1+l2+l3)
min_all = min(l1+l2+l3) 
print ("The maximum of all 3 lists is : " + str(max_all))
print ("The minimum of all 3 lists is : " + str(min_all))

print("------------------------------")

# Python code to find key with Maximum value in Dictionary
# Dictionary Initialization
Tv = {'BreakingBad':100, 'GameOfThrones':1292, 'TMKUC' : 88}
Keymax = max(zip(Tv.values(), Tv.keys()))[1]
print(Keymax)

print("------------------------------")

# Python code to find key with Maximum value in Dictionary
# Dictionary Initialization
Company = {'GFG':10000, 'Hashd':2292, 'Infy': 200}
# taking list of car values in v
v = list(Company.values())
# taking list of car keys in v
k = list(Company.keys())
print(k[v.index(max(v))])

print("------------------------------")

a = "hello"
smallest_char = min(a)
print(smallest_char) #The min() function finds the smallest character based on ASCII values.

print("------------------------------")

a = "HelloWorld"
smallest = min(a)
print(smallest)

s = "PythonProgramming"

print("------------------------------")

# Analyzing "Programming"
smallest = min(s[6:])  
print(smallest)

print("------------------------------")

s = "hello"
res = max(s)
print(res)

print("------------------------------")

s = "abc123"
print(max(s))

print("------------------------------")

s = "a!@#z"
print(max(s))

print("------------------------------")
