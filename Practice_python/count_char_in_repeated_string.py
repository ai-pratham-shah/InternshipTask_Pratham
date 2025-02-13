'''
Count occurrences of a character in a repeated string
'''
def count_char_in_repeated_string(s: str, char: str, n: int) -> int:
    # Count the occurrences of char in the original string s
    count_in_s = s.count(char)
    
    # Find how many full repetitions of s fit into n
    full_repeats = n // len(s)
    
    # Count occurrences of char in the full repetitions
    total_count = full_repeats * count_in_s
    
    # Account for the remaining part of the string
    remainder = n % len(s)
    total_count += s[:remainder].count(char)
    
    return total_count

# Example usage:
s = "abcac"
char = "a"
n = 10
output = count_char_in_repeated_string(s, char, n)
print(f"The character '{char}' appears {output} times in the first {n} characters of the repeated string.")

'''Input:-
{
    1:[2,3,5,8]
    2:[4,7,9]
    3:[15,17,19]
    4:[25,27]
}
output :- 1 2 4 7 9 3 15 17 19 5 8


Logic behind this :
starting from first key then check its first index value if value is in the dict as a key like 2 is key then print its all values like 4,7,9 after again its check 3 which is key 1's value so after that 3 is in the key so now its printing key 3rd value like 15,17,19 after that it again check key 1's and check values after 5 if 5 is in the keys then its print all 5 values if 5 is not in the key then its print 5 after that it again check next index like 8 if 8 is key then its print all values of 8 and if 8 is not found as a key then its printing 8

so this is how output comes : 1 2 4 7 9 3 15 17 19 5 8 

Starting from first key like 1 and values of 1 found 2 then its printing 1 2
after 2 found its check that 2 is in the keys if found then its printing all values of 2 like 4 7 9 so till now output is 1 2 4 7 9
after it again goes to first key like 1 and checks value after 2 then 3 is found so 3 will be add in the output like 1 2 4 7 9 3 
after 3 is found in the key then it prints all the values of 3 in the output so output looks like 1 2 4 7 9 3 15 17 19
then again it goes to first key and checks after 3 if like found 5 if 5 is in the keys then prints its all values but 5 is not in key then its print 5 so now output looks like  1 2 4 7 9 3 15 17 19 5
then again it goes to first key and checks after 3 if like found 8 if 8 is in the keys then prints its all values but 8 is not in key then its print 8 so now output looks like  1 2 4 7 9 3 15 17 19 5 8

so this is how recursively program runs'''




