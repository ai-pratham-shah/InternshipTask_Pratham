def decorator(factorial):
    def wrapper(n):
        if n < 0:
            return "Does not exist" 
        return factorial(n)
    return wrapper
@decorator
def factorial(n):
    if n == 0 or n == 1: 
        return 1
    else:
        return n * factorial(n - 1)
n = int(input("Enter a number:"))
print("Facorial number:",factorial(n))


