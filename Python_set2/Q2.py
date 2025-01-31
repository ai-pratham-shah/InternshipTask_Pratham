#Write a program to extract string elements from a list based on the conditions below,
#using built-in functions.
#a. The first character must capitalize and consonant.
#b. The string must not contain any number.

def extract_string(input_list):
    '''Extracts valid strings from a list based on specific criteria.'''
    def is_valid_string(s):
        '''Checks if a string meets the validity criteria.'''
        if s[0].isupper() and s[0] not in 'AEIOU':
            # Check if the string is alphabetic
            if s.isalpha():
                return True
        return False

    return [s for s in input_list if is_valid_string(s)]

user_input = input("Enter a list of items (comma-separated): ")
if not user_input.strip():
    print("Input is not valid. Please enter a list of items.")
else:
    input_list = user_input.split(',')
    input_list = [item.strip() for item in input_list]
    result = extract_string(input_list)
    if result:
        print("Valid strings found:", result)
    else:
        print("No valid strings found. Please check your input.")

# ------------------------------STEPS/PSUEDOCODE------------------------------

# FUNCTION extract_string(input_list):
# 	STEP 1: CREATE ONE NESTED USER DEFINE FUNCTION CALLED is_valid_string(s):
#	STEP 2: USING IF CHECK THAT FIRST CHARACTER OF EACH WORD IN THE LIST IS CAPITAL OR NOT AND IF CAPITAL THEN IT CHECKS THAT CHARACTER IS CONSONANT.
#	STEP 3: USING IF CHECKS THAT THE WORD IS CONTAINING ONLY ALPHABETIC VALUES
#	STEP 4: EACH WORD IN THE INPUT LIST CHECK ACCORIDING TO THE CONDITIONS THAT DEFINED IN THE is_valid_string(s) AND STORE IN THE LIST.
# 	STEP 5: RETURN RESULT AS A LIST.
# END



