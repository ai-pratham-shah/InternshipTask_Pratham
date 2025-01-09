# Dictionary comprehension
myDict1 = {x: x**2 for x in [1,2,3,4,5]}
print (myDict1)

print("----------------------------------------------------")

# Nested dictionary comprehnesion

pratham = "Aktiv"
dic = {x : {y : x + y for y in pratham} for x in pratham}
print(dic)

print("----------------------------------------------------")

dict1 = {'a' : 1, 'b' : 2, 'c' : 3}
double_dict_value = {k:v*2 for (k,v) in dict1.items()}
print(double_dict_value)

print("----------------------------------------------------")

dict1 = {'a' : 1, 'b' : 2, 'c' : 3}
double_dict_key = {k*2:v for (k,v) in dict1.items()}
print(double_dict_key)

print("----------------------------------------------------")

numbers = range(15)
new_dict_comp = {n:n**2 for n in numbers if n%2 == 0}
print(new_dict_comp)

