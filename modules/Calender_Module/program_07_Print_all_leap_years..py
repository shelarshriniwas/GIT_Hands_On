#Print all leap years.
import calendar

start = int(input("Enter Start Year : "))
end = int(input("Enter End Year : "))

print("Leap Years")

for year in range(start, end + 1):

    if calendar.isleap(year):
        print(year)