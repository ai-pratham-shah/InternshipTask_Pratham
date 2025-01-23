''' You are given an array of integers and a target integer. Your task is to find the indices of two
numbers in the array whose sum equals the target. You may assume that there is exactly one
solution, and you cannot use the same element twice. Return the indices of the two numbers.'''

''' Input:
A list of integers nums[] where 1 <= len(nums) <= 10^4 and -10^9 <= nums[i] <= 10^9.
A target integer target where -10^9 <= target <= 10^9.
Output:
A list of two integers [i, j] such that nums[i] + nums[j] = target.
Example 1:
nums = [2, 7, 11, 15]
target = 9 
output : [0, 1] '''

def find_target(nums, target):
    dict1 = {} 
    
    for i, num in enumerate(nums):
        find = target - num
    if find in dict1:
        return[dict1[find], i]
           
nums = [2, 7, 11, 15]
target = 9
obj = find_target(nums, target)
print(obj)              


#nums = list(map, int(input("Enter a number: ")).split(','))
#target = int(input("Enter a number"))

'''
FUNCTION find_target
	STEP1 : CREATE ONE EMPTY DICT
	STEP2 : ITERATE THROUGH ENUMERATE FUNCTION FOR INDEX AND VALUE AND SUBTRACT TARGET - WITH NUM
	STEP3 : USING IF CONDITION IN DICTIONARY RETURN THE THE LIST OF INDEX WHICH MATCH WITH TARGET
	STEP4 : CREATE OBJECT OF FUNCTION
	STEP5 : PRINT THE OBJECT
'''
