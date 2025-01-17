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

