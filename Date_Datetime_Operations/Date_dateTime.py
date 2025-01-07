from datetime import date, time, datetime
my_date = date(1996, 12, 11)
print("Print date:", my_date)
print(type(my_date))

today = date.today() 
print(today)
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

Str = date.isoformat(today)
print("String representation", Str)

my_time = time(13, 24, 56)
print("Entered time", my_time)


my_time = time()
print("Time without arguement", my_time)

my_time = time(minute=12)
print("Time with one argument minute:", my_time)

my_time = time(hour=3)
print("Time with one argument hour:", my_time)

my_time = time(second=59)
print("Time with one argument second:", my_time)

Time = time(16, 40, 55)
print("Hour =", Time.hour)
print("Minute =", Time.minute)
print("Seconds =", Time.second)
print("microsecond =", Time.microsecond)
Str = Time.isoformat()
print("String Representation:", Str)

a = datetime(1999, 12, 12)
print(a)

a = datetime(1999, 12, 12, 12, 12, 12, 342380)
print(a)

a = datetime(1999, 12, 12, 12, 12, 12)
 
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

today = datetime.now()
print("Current date and time is", today)

now = datetime.now()
formatt = now.strftime("%Y-%m-%d %H:%M:%S")
print("Using strftime current date-time:", formatt)

