# Function to check if a given number is an Armstrong number or not, a function must return a boolean.
def armstrong(n):
    str_n = str(n)
    str_n_length = len(str_n)
    Sum = sum(int(digit) ** str_n_length for digit in str_n)
    if Sum == n:
        return True
    else:
        return False
n=int(input("Enter a number: "))
print(armstrong(n))
    
