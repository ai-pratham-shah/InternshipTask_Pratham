from datetime import datetime
def days_until_next_birthday(birth_date):
    """
    Calculates the number of days until the next birthday.
    """
    today = datetime.today().date()
    next_birthday = birth_date.replace(year=today.year)
    # If the birthday has passed this year, move to next year
    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)
    return (next_birthday - today).days

def is_leap_year(year):
    '''
    year is leap year or not , calculate leap year
    '''
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def next_leap_year(birth_date):
    '''
    Function returns next leap year after the birth year
    '''
    birth_year = birth_date.year
    year = birth_year + 1
    while not is_leap_year(year):
        year += 1
    return year

#UserInput
birth_date = input("Enter your birthdate (YYYY-MM-DD): ") #  2025-09-09
birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
print(f"Days left until your next birthday : {days_until_next_birthday ( birth_date)} days") #  207 days
next_leap = next_leap_year(birth_date)
print(f"Next leap year after the current year: {next_leap}") # 2028