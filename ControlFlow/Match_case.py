# Syntax 
# match subject:
#    case pattern1:
#        # Code
#    case pattern2:
#	 # Code
#    Case_:
#	 # Default case if no other pattern match

# match subject : the variable to match against
# case pattern : A pattern to match the subject
# _ : A default catch-all pattern

# 1.Match Case Statements with Constants.
def greet(person):
    match person:
    	case "A":
    	    print("HELLO A!")
    	case "B":
    	    print("HELLO B!")
    	case _:
    	    print("HELLO STRANGER")
greet("A")
greet("C") 

# 2.Match Case Statement with OR Operator
def num_check(X):
    match X:
        case 10 | 20 | 50 :
            print(f"number found : {X}")
        case _:
            print("No number found")
num_check(10)
num_check(40)  	

# 3.Match Case Statement with Python If Condition
def number_check(y):
    match y:
        case 4 if y % 2 == 0:
            print("Matched 4 and it is even")
        case 4:
            print("Matched 4")
        case _:
            print("No match")
number_check(4)
number_check(8)

# 4.Match Case Statement on Sequences
def sequence(lst):
    match lst:
        case [x,y]:
            print(f"This is two element list: {x} {y}")
        case _:
            print("Unknown data")
sequence([1,2,3])       

# 5.Match Case Statement on Mappings (Dictionaries)
def people(people):
    match people:
        case {"name":name, "age":age}:
            print(f"Name:{name},Age:{age}")
        case {"Name":name}:
            print(f"Name:{name}")
        case _:
            print("No Format")
people({"name":"Aktiv", "age":10})
