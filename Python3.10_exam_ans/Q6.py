from datetime import datetime

def calculate_age(birth_date):
    """
    Recursively calculates the current age of the user based on birthdate.
    """
    today = datetime.today()
    birth_year, birth_month, birth_day = birth_date.year, birth_date.month, birth_date.day
    
    def age_recursive(year):
        if year == today.year:
            return 0 if (today.month, today.day) < (birth_month, birth_day) else 1
        return 1 + age_recursive(year + 1)
    
    return age_recursive(birth_year)

def find_leap_years(start_year, end_year):
    """
    Recursively finds all leap years between start_year and end_year.
    """
    if start_year > end_year:
        return []
    
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    return ([start_year] if is_leap_year(start_year) else []) + find_leap_years(start_year + 1, end_year)

# User input
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birth_date = datetime.strptime(birthdate_str, "%Y-%m-%d")
current_year = datetime.today().year

# Calculating age and leap years
age = calculate_age(birth_date)
leap_years = find_leap_years(birth_date.year + 1, current_year)

# Output results
print(f"Your current age is {age} years.")
print(f"Leap years after your birthdate: {leap_years}")

