
seconds = input("Enter the number of seconds: >>> ")

SECONDS_IN_YEAR = 1051200
SECONDS_IN_MONTH = 86400
SECONDS_IN_WEEK = 20160
SECONDS_IN_DAY = 2880
SECONDS_IN_HOUR = 120
SECONDS_IN_MINUTE = 60

if seconds.isdecimal():
    seconds = int(seconds)
    years = int(seconds / SECONDS_IN_YEAR)
    remaining = seconds % SECONDS_IN_YEAR
    months = int(remaining / SECONDS_IN_MONTH)
    remaining %= SECONDS_IN_MONTH
    weeks = int(remaining / SECONDS_IN_WEEK)
    remaining %= SECONDS_IN_WEEK
    days = int(remaining / SECONDS_IN_DAY)
    remaining %= SECONDS_IN_DAY
    hours = int(remaining / SECONDS_IN_HOUR)
    remaining %= SECONDS_IN_HOUR
    minutes = int(remaining / SECONDS_IN_MINUTE)
    seconds = remaining % SECONDS_IN_MINUTE
    print(f"The number of years is: {years}\nThe number of months is: {months}\nThe number of weeks is: {weeks}")
    print(f"The number of days is: {days}\nThe number of hours is: {hours}\nThe number of minutes is: {minutes}")
    print(f"And the number of seconds is: {seconds}")

else:
    print("The input is not valid")
