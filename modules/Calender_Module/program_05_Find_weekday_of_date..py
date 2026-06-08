# Find weekday of date.
import calendar

year = int(input("Enter Year : "))
month = int(input("Enter Month : "))
day = int(input("Enter Day : "))

weekday = calendar.weekday(year, month, day)

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

print("Weekday :", days[weekday])