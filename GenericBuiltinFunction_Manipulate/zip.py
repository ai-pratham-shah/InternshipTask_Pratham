# The zip() function in Python combines multiple iterables such as lists, tuples, strings, dict etc, into a single iterator of tuples. Each tuple contains elements from the input iterables that are at the same position.

name = ['Pratham', 'Rushil', 'Yash', 'Raj']
score = [99, 91, 98, 97]

result = zip(name, score)
print(list(result)) #[('Pratham', 99), ('Rushil', 91), ('Yash', 98), ('Raj', 97)]

print("-----------------------------------")

name = ['Pratham', 'Rushil', 'Yash', 'Raj']
score = [99, 91, 98, 97]

res = zip()
print(list(res))
res = zip(name)
print(list(res))
res = zip(name, score)
print(list(res))

print("-----------------------------------")

# Unzipping data with zip()
a = [('Pratham', 99), ('Rushil', 91), ('Yash', 98), ('Raj', 97)]

name, score = zip(*a)

print(f"Name: {name}")
print(f"Score: {score}")

print("-----------------------------------")

#Using enumerate() and zip() together in Python
# create a list of names
names = ['sravan', 'bobby', 'ojaswi', 'rohith', 'gnanesh']
subjects = ['java', 'python', 'R', 'cpp', 'bigdata']
# create a list of marks
marks = [78, 100, 97, 89, 80]
# use enumerate() and zip() function
# to iterate the lists
for i, (names, subjects, marks) in enumerate(zip(names, subjects, marks)):
    print(i, names, subjects, marks)

