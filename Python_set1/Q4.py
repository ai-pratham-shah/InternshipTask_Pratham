''' 4. Write a program to extract string elements from a list based on the conditions below.
a. The first character must be lower and consonant.
b. The string must not contain any number and also does not contain any special character. '''


def extract_strings(input_list):
    
    def is_valid_string(s):
    
        if s[0].islower() and s[0] not in 'aeiou':
            if s.isalpha():
                return True
        return False
    
    return [s for s in input_list if is_valid_string(s)]

input_list = ['apple', 'banana', 'orange', '123abc', 'kiwi', 'grape!', 'melon', 'cherry']
result = extract_strings(input_list)
print(result)

