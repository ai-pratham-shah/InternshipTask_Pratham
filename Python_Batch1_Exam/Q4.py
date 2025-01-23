'''
4. List Up an Array of Strings in a Proper Way
Question:
You are given an array of strings (nouns). Your task is to list them up in a grammatically correct
sentence.
Explanation:
The sentence should start with a capital letter.
Each noun should be preceded by the correct article:
Use "A" for words starting with a consonant.
Use "An" for words starting with a vowel (a, e, i, o, u).
Join the words with commas, except for the last two, which should be joined with "and".
The sentence should end with a period (.).
Do not change the order of the nouns.
There are at least two nouns in the array.
Input:
An array of string nouns[] where each string represents a noun.
The length of the array is at least 2.
Output:
A grammatically correct sentence that lists the nouns with appropriate articles and punctuation.
Example 1:
nouns = ["orange", "apple", "pear"]
Output:
"An orange, an apple and a pear."
'''

def check_strings(nouns):
    consonants = "A"
    vowels = "An"
        
    def validate_sentence(s):
        for i in s:
            if i[0].startswith("AEIOUaeiou"):
                print(vowels + i)
            else:
                print(consonants + i)
        words = [i for i in s ]
    return ' ,'.join    
nouns = ["orange", "apple", "pear"]
result = check_strings(nouns)
print(result)


#STEPS
'''
1. FUNCTION "check_strings(nouns)"
2. 	TAKE TWO VARIABLES AND ASSIGN VALUES "consonants" , "vowels"
3. 	CREAE ONE NESTED USER DEFINE FUNCTION 
   	A. ITERATE THROUGH STRING 
   	    A. USING IF AND INBUILT FUNCTION CHECK START WITH VOWELS OR NOT AND THEN CONCATENATE TO THE STRING 
   	    B. IN ELSE ADD CONSONANTS IF VOWELS ARE NOT THERE IN THE FIRST INDEX OF STRING.
4. 	AFTER ADDING A AND AN I HAVE TO SPLIT THE STRING AND JOIN WITH COMMAS ","
5. 	THEN ITERATE AND ACCORIDING TO LENGTH OF LIST OF STRING I HAVE TO ADD "and"
6. 	USING SLICING AT THE LAST POSTION ADD "."
7. 	RETURN THE validate_sentence(s)
   END    
'''   
