import datetime
from datetime import datetime, date

# TAKING BIRTHDATE FROM USER
date1_input = input("Enter the birth date (YYYY-MM-DD): ")

# PROPER FORMATION OF DATE
date1 = datetime.strptime(date1_input, "%Y-%m-%d")

# TAKING TODAY'S DATE
date2 = datetime.today()

# CALCULATE CURRENT AGE IN DAYS
current_age1 = abs((date2 - date1).days)

# CALCULATE CURRENT AGE IN YEAR
current_age = round(current_age1 / 365)
print("Current age of user:",current_age)

#STEPS:-

'''
IMPORT DATEIME
TAKE USER INPUT FOR BIRTHDAY
TAKE TODAY'S DATE
CALCULATE CURRENT AGE WITH TODAY'S DATE SUBTRACTS BIRTHDATE
PRINT THE CURRENT AGE
USING IF COUNT LEAP YEAR WITH BIRTHDAY YEAR TO CURRENT YEAR
PRINTS THE LEAP YEAR'S
'''

