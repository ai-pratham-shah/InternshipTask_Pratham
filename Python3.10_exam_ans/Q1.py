def two_sum(nums, target):
    """
    This function finds two numbers in the list whose sum equals the target.
    It returns their indices as a list.
    """
    seen = {}  # Dictionary to store numbers and their indices
    
    for i, num in enumerate(nums):  # Loop through the list
        diff = target - num  # Calculate the required number
        
        if diff in seen:  # Check if required number exists in dictionary
            return [seen[diff], i]  # Return indices of the pair
        
        seen[num] = i  # Store the current number and its index
    
    return []  # Return empty list if current number and its index not find

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
target = int(input("Enter target number: "))
print(two_sum(nums, target))



def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        
        if diff in seen:
            return [seen[diff], i]
            
        seen[num] = i
    return []
    
nums = list(map(int, input("Enter numbers separeted by spaces: ").split()))
target = int(input("Enter target number:"))
print(two_sum(nums, target))
