'''
5. Maximum Number of New People Who Can Be Seated
Question:
You are given a list of seats, where:
0 represents an empty seat.
1 represents an occupied seat.
Your task is to calculate the maximum number of new people who can be seated such that there is
at least a gap of 2 seats between any two occupied seats.

Example 1:
seats = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
Output:
2

'''

def seating_management(seats):
    counnter = 0
    for i in seats:
        if i == 0:
            print(index(i))
seats = [0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
obj = seating_manage(seats)
print(obj)


#STEPS
'''
FUNCTION seating_management
	STEP 1: USING FOR LOOP ITERATE THROUGH LIST 
	STEP 2: FIND THAT 1 IS COMING AFTER HOW MANY 0  
	STEP 3: USING IF THERE IS MORE THAN 2 ZERO IS COMING AFTER OR BEHIND 1 THEN ADDED COUNT IN THE OUTPUT.
	STEP 4: RETURN THE COUNTER  

'''
