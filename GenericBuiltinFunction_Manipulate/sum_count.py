# Python sum () function is a built-in function that returns the sum of all numerical values provided in an iterable.

arr = [1, 5, 2]
print(sum(arr)) # 8

print("---------------------------------")

numbers = [1,2,3,4,5,1,4,5]
Sum = sum(numbers)
print(Sum) # 25

Sum = sum(numbers, 10)
print(Sum) # 35

print("---------------------------------")

#Python Sum Function on a Dictionary

my_dict = {'a': 20, 'b': 20, 'c': 70}
total = sum(my_dict.values())
print(total) # 110

print("---------------------------------")

# Python Sum Function on a Set

my_set = {5, 7, 9, 10, 15}
total = sum(my_set)
print(total) # 46

print("---------------------------------")

# Python Sum Function on a Tuple

my_tuple = (1, 2, 3, 4, 5)
total = sum(my_tuple)
print(total) # 15

print("---------------------------------")

# The sum in Python with For Loop

numbers = [1, 5, 10, 50, 20]
total = 0
for num in numbers:
    total += num
print("The sum of the numbers is:", total) # 86

print("---------------------------------")

numbers = [5,2,3,4,6,1,4,4]

# start = 10
Sum = sum(numbers)
print(Sum)
average= Sum/len(numbers) 
print (average)

print("---------------------------------")
#The count() method is used to find the number of times a specific element occurs in a list.
a = [1, 2, 3, 1, 2, 1, 4]
# count given number in list
c = a.count(1)
print(c)

print("---------------------------------")

#Count the elements in a list until an element is a Tuple.
def Count(lst):
    counter = 0
    for num in lst:
        if isinstance(num, tuple):
            break
        counter = counter + 1
    return counter
lst = [4, 5, 6, 10, (1, 2, 3), 11, 2, 4]
print(Count(lst))
