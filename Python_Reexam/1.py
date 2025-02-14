def anagrams(str1,str2):
    '''
    Function to check if two string are anagrams or not
    '''
    str1 = str1.replace(" ","").lower()
    str2 = str2.replace(" ","").lower()
    return sorted(str1) == sorted(str2)
#UserInput
str1 = input("Enter string1: ")
str2 = input("Enter string2: ")
print("If output is true then strings are anagrams,"
      "if output is false then strings are not anagrams:",anagrams(str1, str2))
