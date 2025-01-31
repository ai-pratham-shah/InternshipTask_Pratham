#Write a program to create a list of numbers, and extract integer numbers from a list
#based on the below conditions.
#a. The number must be 4 digits long i.e (1000 to 9999)
#b. The first digit of the number must be odd and the last digit must be even.
#c. The number must be divisible by either 3 or 7.

def extract_integers(numbers):
    result = []
    
    for num in numbers:
        
        if 1000 <= num <= 9999:
            
            first_digit = (num // 1000) % 10
            
            last_digit = num % 10 
            
            if first_digit % 2 != 0 and last_digit % 2 == 0:
            
                if num % 3 == 0 or num % 7 == 0:
                    result.append(num)
    return result
    
user_input = input("Enter a list of 4 digit numbers (comma-separated): ")
try:    
    numbers = [int(num.strip()) for num in user_input.split(',')]
    filtered_numbers = extract_integers(numbers)
    if filtered_numbers:
        print("Valid filtered_numbers found:", filtered_numbers)
    else:
        print("No valid filtered numbers found.")
except ValueError:
    print("Invalid input")

# ------------------------------STEPS/PSUEDOCODE------------------------------

# FUNCTION extract_integers(numbers):
# 	STEP 1: CREATE ONE EMPYT LIST CALLED result
#	STEP 2: FOR EACH NUMBERS
#		A. USING IF IT CHECKS THAT NUMBER IS 4 DIGIT LONG OR NOT 
#		 	A. EXTRACT FIRST DIGIT FROM 4 DIGIT NUMBER
#			B. EXTRACT LAST DIGIT FROM 4 DIGIT NUMBER
#			C. USING IF IT CHECK THAT EXTRACTED FIRST DIGIT IS ODD OR NOT AND LAST DIGIT IS EVEN OR NOT
#				A. USING IF IT CHECKS THAT NUMBER IS DIVISIBLE BY EITHER 3 OR 7
#				B. DIVISIBLE NUMBER APPEND IN THE LIST(result)
#	STEP 3: RETURN RESULT AS LIST.
# END

  
                     
                     
