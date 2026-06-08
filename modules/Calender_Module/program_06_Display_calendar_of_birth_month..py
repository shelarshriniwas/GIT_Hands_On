# Display calendar of birth month.
import calendar

birth_year = int(input("Enter Birth Year : "))
birth_month = int(input("Enter Birth Month : "))

print(calendar.month(birth_year, birth_month))