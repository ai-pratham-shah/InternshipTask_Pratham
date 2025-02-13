def reverse_alphabetic(s):
    """
    This function reverses only the alphabetic characters in a string while keeping non-alphabetic 
    characters (spaces, punctuation, numbers) in their original positions.
    """
    alphabetic_chars = [char for char in s if char.isalpha()]  # Extract alphabetic characters
    alphabetic_chars.reverse()  # Reverse the list of alphabetic characters
    result = []  # To store the final string
    alpha_index = 0  # Pointer for reversed alphabetic characters
    
    for char in s:
        if char.isalpha():
            result.append(alphabetic_chars[alpha_index])  # Replace with reversed character
            alpha_index += 1
        else:
            result.append(char)  # Keep non-alphabetic characters unchanged
    
    return "".join(result)

s = input("Enter a string: ")
print(reverse_alphabetic(s))

