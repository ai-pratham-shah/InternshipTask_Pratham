''' 
Given a string var, reverse the string while keeping all non-alphabetic characters (spaces,
punctuation) in their original positions. Only reverse the alphabetic characters.
Input:
A string var of length 1 <= len(s) <= 100.
Output:
A new string with alphabetic characters reversed while keeping all other characters in the same
position.
Example 1:
var = "a-bC-dEf-ghIj"
Output:
"j-Ih-gfE-dCba"
'''

'''def reverse_position(var):
    def nested_function(s):
        for i in s:
            if i in s.isalpha():
                reversed(i)
    return s

var = "a-bC-dEf-ghIj"
print(reverse_position(var))'''


def reversed_text(text):
    text = text.casefold()
    rev_text = ''.join(reversed(text))
    return rev_text

text = input("Enter the text: ")
result = reversed_text(text)
print("Reversed text:", result)

#STEPS
'''
FUNCTION reversed_text(text)
	CONVERT TEXT INTO LOWERCASE
	REVERSE THE TEXT USING JOIN AND REVERSED FUNCTION
	THEN ITERATE THROUGH STRING AND CONVERT INTO LIST AND THEN FIND '-' INDEX 
	RETURN THE REVERSE TEXT
END
'''
