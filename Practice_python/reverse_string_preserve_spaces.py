'''
Write a program to reverse the given string while preserving the position of spaces.
Examples: 
Input  : "abc de"
Output : edc ba
'''

def reverse_string_preserve_spaces(s: str) -> str:
    # Convert the string to a list so we can modify it
    s_list = list(s)
    
    # Get a list of non-space characters and reverse them
    non_space_chars = [char for char in s if char != ' ']
    non_space_chars.reverse()  # Reverse the non-space characters
    
    # Replace non-space characters in the original positions with the reversed ones
    idx = 0
    for i in range(len(s_list)):
        if s_list[i] != ' ':
            s_list[i] = non_space_chars[idx]
            idx += 1
    
    # Join the list back to a string and return it
    return ''.join(s_list)

# Example usage:
input_str = input("Enter a string:")
output_str = reverse_string_preserve_spaces(input_str)
print("Input  :", input_str)
print("Output :", output_str)

