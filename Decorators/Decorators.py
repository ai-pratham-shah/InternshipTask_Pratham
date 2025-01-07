def decorator_example(basic_calculator):
    def inner_function(*args, **kwargs):
        basic_calculator(*args, **kwargs)
        print("Your code run perfectly")
    return inner_function

@decorator_example
def basic_calculator():
    x = int(input("Enter number 1: "))
    y = int(input("Enter number 2: "))
    choice = input("which operation do you want to perform(press : +,-,*,/) :")
    if choice == "+":
        print("x + y = ", x + y)
    elif choice == "-":
        print("x - y = ", x - y)
    elif choice == "*":
        print("x * y = ", x * y)
    elif choice == "/":
        print("x / y = ", x / y)
    else:
        print("Invalid input.")
import time
basic_calculator()
start_time = time.time()
print("Start time:", start_time)
end_time = time.time()
print("End time:", end_time)
print("Execution time:", end_time-start_time)
