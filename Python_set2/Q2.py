#Write a program to extract string elements from a list based on the conditions below,
#using built-in functions.
#a. The first character must capitalize and consonant.
#b. The string must not contain any number.

def extract_string(input_list):
    def is_valid_string(s):
        if s[0].isupper() and s[0] not in 'AEIOU':
            if s.isalpha():
                return True
        return False
    return [s for s in input_list if is_valid_string(s)]

input_list = ['Apple', 'Banana', 'cat', 'Alpha', 'Dog']
result = extract_string(input_list)
print(result)

# ------------------------------STEPS/PSUEDOCODE------------------------------

# FUNCTION extract_string(input_list):
# 	STEP 1: CREATE ONE NESTED USER DEFINE FUNCTION CALLED is_valid_string(s):
#	STEP 2: USING IF CHECK THAT FIRST CHARACTER OF EACH WORD IN THE LIST IS CAPITAL OR NOT AND IF CAPITAL THEN IT CHECKS THAT CHARACTER IS CONSONANT.
#	STEP 3: USING IF CHECKS THAT THE WORD IS CONTAINING ONLY ALPHABETIC VALUES
#	STEP 4: EACH WORD IN THE INPUT LIST CHECK ACCORIDING TO THE CONDITIONS THAT DEFINED IN THE is_valid_string(s) AND STORE IN THE LIST.
# 	STEP 5: RETURN RESULT AS A LIST.
# END

