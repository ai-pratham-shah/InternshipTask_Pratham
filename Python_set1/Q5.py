''' Write a program to create a list of numbers, and extract integer numbers from a list based on the
below conditions.
a. The number must be 4 digits long i.e (1000 to 9999)
b. The second digit of the number must be odd and the last digit must be even.
c. The number must be divisible by either 8 or 5. '''

def extract_numbers(numbers):
    result = []
    
    for num in numbers:
        
        if 1000 <= num <= 9999:
        
            second_digit = (num // 100) % 10 
            last_digit = num % 10
            
            if second_digit % 2 != 0 and last_digit % 2 == 0:
            
                if num % 8 == 0 or num % 5 == 0:
                    result.append(num)
    
    return result

user_input = input("Enter a list of 4 digit numbers (comma-separated): ")
try:
    numbers = [int(num.strip()) for num in user_input.split(',')]
    filtered_numbers = extract_numbers(numbers)
    print("Filtered numbers:", filtered_numbers)
except ValueError:
    print("Invalid Input.")



