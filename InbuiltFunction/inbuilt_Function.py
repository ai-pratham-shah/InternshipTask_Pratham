x = abs(-1.23) # Returns the absolute value of a number 
y = abs(3+5j)  
print("Example of abs function:", x,y) # 1.23, 5.830951894845301

mylist = [True, True, True] # The all() function returns True if all items in an iterable are true, otherwise it returns False.If the iterable object is empty, the all() function also returns True.
X = all(mylist)
print("Example of all function:", X)

mylist1 = [True, False, False] # he any() function returns True if any item in an iterable are true, otherwise it returns False.If the iterable object is empty, the any() function will return False.
x1 = any(mylist1)
print("Example of any function:", x1)

mytuple = (0, 1, False)
print("Check if any item in tuple is true: ",any(mytuple))

myset = {0,1,0}
print("Check is any item in set true:",any(myset))

mydict = {0 : "Apple", 00 : "Orange"}
print("Check if any item in dictionary is true:", any(mydict))

ax = ascii("Aktiv Software")
print("Example of Ascii function is:", ax, ascii(mylist))

print("Example of bin function :", bin(12))

print("Example of bool function:", bool(10))

print("Example of bytearray function:", bytearray(4)) # The bytearray() function returns a bytearray object.It can convert objects into bytearray objects, or create empty bytearray object of the specified size.

print("Example of chr function:", chr(97)) # The chr() function returns the character that represents the specified unicode.

print("Example of complex function:", complex(4, 7)) # The complex() function returns a complex number by specifying a real number and an imaginary number.

print("Example of dict function", dict(name = "Pratham", age = 22)) # The dict() function creates a dictionary.A dictionary is a collection which is unordered, changeable and indexed.

print("Example of divmod function", divmod(10,3)) # The divmod() function returns a tuple containing the quotient  and the remainder when argument1 (dividend) is divided by argument2 (divisor).

a1 = ("data1","data2","data3")
a11 = enumerate(a1, 1)
print("Example of enumerate function", list(a11)) # The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.The enumerate() function adds a counter as the key of the enumerate object.

xe = 'print(55)' 
print("Example of eval function:", eval(xe)) # The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.

xex = 'name = "John"\nprint(name)'
("Example of exec function:", exec(xex)) # The exec() function executes the specified Python code.e exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression

ages = [5, 12, 17, 18, 24, 32] # the filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
def myFunc(x):
  if x < 18:
    return False
  else:
    return True
# syntax : filter(function, iterable)
adults = list(filter(myFunc, ages))
print(adults)

print("Example of float function:", float(5)) # The float() function converts the specified value into a floating point number.

print("Example of format function",format(0.5, '%')) # The format() function formats a specified value into a specified format.

frozensett = ['Apple', 'Banana', 'Cherry']
print("Example of frozenset", frozenset(frozensett))

print("Example of hexadecimal(hex) function:", hex(255)) # The hex() function converts the specified number into a hexadecimal value.The returned string always starts with the prefix 0x.

idx  = ('apple', 'banana', 'cherry')
print("Example of id function:", id(idx))

print("Example of Int function:", int(4.9))

print("Example of isinstance:", isinstance(10, int)) # The isinstance() function returns True if the specified object is of the specified type, otherwise False.If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.

# The issubclass() function returns True if the specified object is a subclass of the specified object, otherwise False.
class myAge:
  age = 36

class myObj(myAge):
  name = "John"
  age = myAge

xisb = issubclass(myObj, myAge)
print("Example of issubclass", xisb)

xit = iter(["apple", "banana", "cherry"])
print("Example of iter function", next(xit))
print("Example of iter function", next(xit))
print("Example of iter function", next(xit))

mylistl = ["apple", "banana", "cherry"]
print("Example of len function", len(mylistl)) # The len() function returns the number of items in an object.When the object is a string, the len() function returns the number of characters in the string.

print("Example of list function", list(('apple', 'banana', 'cherry'))) # The list() function creates a list object.A list object is a collection which is ordered and changeable.

def myfunc(n):
  return len(n) 
# syntax = map(function, iterables)
xa = map(myfunc, ('apple', 'banana', 'cherry')) # The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
print("Example of map function:", list(xa))

def myfuncc(a, b):
  return a + b
xy = map(myfuncc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'ppineapple'))
print("Example of map function:", list(xy)) 

print("Example of max function:", max(50, 100)) # The max() function returns the item with the highest value, or the item with the highest value in an iterable.If the values are strings, an alphabetically comparison is done.

mv = memoryview(b"Pt")
print("Example of memoryview function:", mv[0]) # The memoryview() function returns a memory view object from a specified object.

print("Example of min function:", min(50,100)) # The min() function returns the item with the lowest value, or the item with the lowest value in an iterable.If the values are strings, an alphabetically comparison is done.

print("Example of oct function:", oct(10)) # The oct() function converts an integer into an octal string.Octal strings in Python are prefixed with 0o.

# f = open("demofile.txt", "r") 
# print("Example of open function", f.read()) # The open() function opens a file, and returns it as a file object.
# file modes: "r" : Read, "a" : Append, "w" : Write, "x" : Create

print("Example of pow function:", pow(2, 3)) # The pow() function returns the value of x to the power of y (xy).

xr = range(5, 10, 2)
for i in xr:
  print("Example of range function:", i) # start: Optional. An integer number specifying at which position to start. Default is 0.stop: Required. An integer number specifying at which position to stop (not included).step: Optional. An integer number specifying the incrementation. Default is 1

alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
print("Example of reversed function:", ralph)
for x in ralph:
  print("Example of Reversed function:", x) # The reversed() function returns a reversed iterator object.

xrr = round(5.76543, 2)
print("Example of round function:", x) # he round() function returns a floating point number that is a rounded version of the specified number, with the specified number of decimals.The default number of decimals is 0, meaning that the function will return the nearest integer.

xset = set(('apple', 'banana', 'cherry'))
print("Example of set function:", xset) # The set() function creates a set object.The items in a set list are unordered, so it will appear in random order.

asl = ("a", "b", "c", "d", "e", "f", "g", "h")
xsl = slice(2)
print(asl[xsl])
print(asl[3:5]) # The slice() function returns a slice object.A slice object is used to specify how to slice a sequence. You can specify where to start the slicing, and where to end. You can also specify the step, which allows you to e.g. slice only every other item.

aso = ("b", "g", "a", "d", "f", "c", "h", "e")
xso = sorted(aso)
print(xso)
xsor = sorted(aso, reverse=True)
print(xsor) # The sorted() function returns a sorted list of the specified iterable object.You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically

print("Example of str function:", str(5.5)) # The str() function converts the specified value into a string.

asu = (1, 2, 3, 4, 5)
xsu = sum(asu, 5)
print("Example of sum function:", xsu) # The sum() function returns a number, the sum of all items in an iterable.iterable: Required. The sequence to sum.start: Optional. A value that is added to the return value

#The super() function is used to give access to methods and properties of a parent or sibling class.The super() function returns an object that represents the parent class.


xt = tuple(('apple', 'banana', 'cherry'))
print("Example of tuple:", xt) # The tuple() function creates a tuple object. "You cannot change or remove items in a tuple."

aa = ('apple', 'banana', 'cherry')
bb = "Hello World"
cc = 33
xx = type(aa)
yy = type(bb)
zz = type(cc)
print("Example of type function:", xx, yy, zz) # Will return type of a variable

az = ("John", "Charles", "Mike")
bz = ("Jenny", "Christy", "Monica")
xz = zip(az, bz) # The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.If the passed iterables have different lengths, the iterable with the least items decides the length of the new iterator.
print("Example of xz:", list(xz))



