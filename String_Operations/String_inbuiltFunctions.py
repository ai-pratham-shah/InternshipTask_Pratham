text = "hello world" #Converts the first character to uppercase.
print(text.capitalize())  # Output: "Hello world"


text = "HELLO WORLD" #Converts all characters to lowercase.
print(text.lower())  # Output: "hello world"


text = "hello world" #Converts all characters to uppercase.
print(text.upper())  # Output: "HELLO WORLD"


text = "hello world" #Converts the first character of each word to uppercase.
print(text.title())  # Output: "Hello World"


text = "  hello world  " #Removes leading and trailing whitespace (or specified characters).
print(text.strip())  # Output: "hello world"


text = "  hello world  " #Removes leading (lstrip) or trailing (rstrip) whitespace (or specified characters).
print(text.lstrip())  # Output: "hello world  "
print(text.rstrip())  # Output: "  hello world"


text = "hello world" #Replaces occurrences of a substring with another substring.
print(text.replace("world", "Python"))  # Output: "hello Python"


text = "hello world Python" #Splits the string into list of substring
print(text.split())  # Output: ["hello", "world", "Python"]

words = ["hello", "world", "Python"] #Joins elements of a list or iterable into a single string using a specified separator.
print(" ".join(words))  # Output: "hello world Python"


text = "hello world" #Returns the index of the first occurrence of a substring, or -1 if not found.
print(text.find("world"))  # Output: 6


text = "hello world" #Similar to find() but raises a ValueError if the substring is not found.
print(text.index("world"))  # Output: 6


text = "hello world" #Checks if the string starts or ends with a specified substring.
print(text.startswith("hello"))  # Output: True
print(text.endswith("world"))    # Output: True


text = "hello hello world" #Counts the occurrences of a substring in the string.
print(text.count("hello"))  # Output: 2


text = "hello" #Checks if all characters in the string are alphabetic.
print(text.isalpha())  # Output: True


text = "12345" #Checks if all characters in the string are digits.
print(text.isdigit())  # Output: True


text = "hello123" #Checks if all characters in the string are alphanumeric.
print(text.isalnum())  # Output: True
 
text = "   " #Checks if the string contains only whitespace characters.
print(text.isspace())  # Output: True


text = "Hello World" #Swaps the case of all characters in the string.
print(text.swapcase())  # Output: "hELLO wORLD"


text = "42" #Pads the string with zeros on the left to reach a specified width.
print(text.zfill(5))  # Output: "00042"


text = "hello" #Centers the string within a specified width, padding with spaces or a specified character.
print(text.center(10, "-"))  # Output: "--hello---"

print("---------------------------------------------------------------------------------------------------------------")

# Example 1 : Given a user's full name in lowercase, format it so that the first letter of each name is capitalized.
username = "pratham shah"
print("Using of title function:", username.title())

print("---------------------------------------------------------------------------------------------------------------")

# Example 2 : Verify if a password contains only alphanumeric characters.
password = "Aktiv123"
if password.isalnum():
    print("Valid password")
else:
    print("Invalid password")

print("---------------------------------------------------------------------------------------------------------------")
    
# Example 3 : Extract the extension of a file from its filename.
file_new = "photo.jpg"
extension = file_new.split(".")[-1]
print(extension)

print("---------------------------------------------------------------------------------------------------------------")

# Example 4 : Check if the word "Python" appears in a job description and get its position.
job_description = "We are looking for python developers."
position = job_description.find("python")
if position != -1:
    print(f"Python found at position {position}")
else:
    print("Not found")
    
print("---------------------------------------------------------------------------------------------------------------")

# Example 4 : Mask all but the last 4 digits of a credit card number.
credit = "1234567812345678"
card = "*" *  12 + credit[-4:]
print(card)

# Example 5 : Palindrome
text = "Mam"
text = text.casefold()
rev_text = ''.join(reversed(text))
if text == rev_text:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")

