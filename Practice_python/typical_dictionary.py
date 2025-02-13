def take_input():
    # Number of key-value pairs
    n = int(input("Enter the number of key-value pairs: "))
    
    dict1 = {}
    
    # Taking inputs for each key
    for _ in range(n):
        # Input key
        key = int(input("Enter key: "))
        
        # Input values associated with the key, separated by commas
        values = input(f"Enter values for key {key} (comma separated): ").split(',')
        
        # Convert values from string to integers
        values = [int(x) for x in values]
        
        # Store in dictionary
        dict1[key] = values
    
    return dict1
def recursion(i,dict1,output):
    for j in dict1[i]:
        output.append(j)
        if j in dict1.keys():
            recursion(j,dict1,output)
    else:
        return output
    
i = list(dict1.keys())[0]
output = []
output.append(i)
dict1 = take_input()
print(recursion(i,dict1,output))
