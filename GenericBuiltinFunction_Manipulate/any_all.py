# Python any() function returns True if any of the elements of a given iterable( List, Dictionary, Tuple, set, etc) are True else it returns False.

l = [False, True, False]
print(any(l)) # True

l = [5, 6, 7]
print(any(l)) # True

l = [0, 0, False]
print(any(l)) # False

l = []
print(any(l)) # False

s = { 1, 2, 3}
print(any(s)) # True

s = { 0, 0, False}
print(any(s)) # False

s = { 1, 2, 0, 8, False}
print(any(s)) # True

s = {}
print(any(s)) # False

d = {1: "Hello", 2: "World"}
print(any(d)) # True

d = {0: "Hello", False: "World"}
print(any(d)) # False

s = "Hi There!"
print(any(s)) # True

s = ""
print(any(s)) # False

# Python any() Function with a Condition
lst = [4, 5, 8, 9, 10, 17]
print(lst)
result = any(ele > 10 for ele in lst)
print("element satisfy specified condition ?:", result) # True

# Python any() Function with For Loop
def example_any(my_list):
    for item in my_list:
        if item:
            return True
    return False
 
x = [4, 5, 8, 9, 10, 17]
print(example_any(x)) # True

# Check if any element in the list is greater than 5
my_list = [1, 3, 7, 2]
result = any(x < 5 for x in my_list)
print(result) #True

# all() outputs True solely when every element of the iterable is true; if not, it results in False.

# Check if all elements in the list are even numbers
my_list = [2, 4, 6, 8]
result = all(x % 2 == 0 for x in my_list)
print(result) # True

# List of dictionaries representing devices in a network
network_devices = [
{'name': 'Router1', 'type': 'Router', 'status': 'inactive'},
{'name': 'Switch1', 'type': 'Switch', 'status': 'active'},
{'name': 'Firewall1', 'type': 'Firewall', 'status': 'inactive'},
{'name': 'Switch2', 'type': 'Switch', 'status': 'inactive'},
]
# Check if any device in the network is active
is_any_device_active = any(device['status'] == 'active' for device in network_devices)
print(is_any_device_active) # True

# Check if all strings in a list have a length greater than 3
my_list = ['apple', 'banana', 'kiwi']
result = all(len(x) > 3 for x in my_list)
print(result) # True

# Validate user inputs for a password
password = "SecurePassword123"
is_valid = all([
    any(char.isupper() for char in password),
    any(char.isdigit() for char in password),
    len(password) >= 8
])
print(is_valid) # True
