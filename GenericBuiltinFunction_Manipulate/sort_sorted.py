#-> The sort() method in Python is a built-in function that allows us to sort the elements of a list in ascending or descending order and it modifies the list in place which means there is no new list created.
#-> This method is useful when working with lists where we need to arranged the elements in a specific order, whether numerically or alphabetically.
#-> list_name.sort(key=None, reverse=False)
# key (Optional): This is an optional parameter that allows we to specify a function to be used for sorting. For example, we can use the len() function to sort a list of strings based on their length.
# reverse (Optional): This is an optional Boolean parameter. By default, it is set to False to sort in ascending order. If we set reverse=True, the list will be sorted in descending order.
#->The sort() method modifies the list in place and returns None.
#->The default behavior of sort() is ascending order. Use reverse=True to sort in descending order.
#->The key parameter can be used for customizing the sorting logic.
# ->We can use sorted() method, if we need to create a new sorted list without altering the original.

a = [1,5,9,7,5,3]
# Sort the value in increasing order
a.sort()
print(a)

b = [1,5,9,7,5,3]
b.sort(reverse=True)
print(b)

ab = ["apple", "banana", "kiwi", "cherry"]
ab.sort(key=len)
print(ab)

ac = ["apple", "banana", "kiwi", "cherry"]
ac.sort(key=lambda x: x[-1])
print(ac)

az = ["Banana", "apple", "Grape", "pear"]
az.sort(key=str.lower)
print(az)

print("-------------------------------------")

# ->sorted() function returns a new sorted list from the elements of any iterable like (e.g., list, tuples, strings ). It creates and returns a new sorted list and leaves the original iterable unchanged.

a = [50,20,70,90]
b = sorted(a)
print("Print list:", b)
c = sorted(a, reverse=True)
print("Reverse list:", c)

azz = [
    {"name": "Pratham", "score": 99},
    {"name": "Shah", "score": 98},
    {"name": "Raj", "score": 97}
]
bz = sorted(azz, key=lambda x: x['score'])
print(bz)
