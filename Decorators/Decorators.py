import time

def decorator_example(basic_calculator):
    def inner_function(*args, **kwargs):
        basic_calculator(*args, **kwargs)
        print("Your code ran perfectly")
    return inner_function

@decorator_example
def basic_calculator():
    while True:
        try:
            x = int(input("Enter number 1 (e.g., 10, 15, 20): "))
            break
        except ValueError:
            print("Invalid input, Please enter a valid number for number 1.")

    while True:
        try:
            y = int(input("Enter number 2 (e.g., 10, 15, 20): "))
            break
        except ValueError:
            print("Invalid input, Please enter a valid number for number 2.")

    while True:
        choice = input("Which operation do you want to perform? (press: +, -, *, /): ")
        
        if choice == "+":
            print(f"{x} + {y} = {x + y}")
            break
        elif choice == "-":
            print(f"{x} - {y} = {x - y}")
            break
        elif choice == "*":
            print(f"{x}  {y} = {x * y}")
            break
        elif choice == "/":
            if y != 0:  
                print(f"{x} / {y} = {x / y}")
                break
            else:
                print("Error: Cannot divide by zero.")
        else:
            print("Invalid operation. Please enter one of the valid operations (+, -, *, /).")

start_time = time.time()
basic_calculator()  
end_time = time.time()
print("Execution time in millie seconds:", end_time - start_time)


