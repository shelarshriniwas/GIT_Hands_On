# Create age calculator.

from datetime import date

birth_year = int(input("Enter Birth Year : "))
birth_month = int(input("Enter Birth Month : "))
birth_day = int(input("Enter Birth Day : "))

birth_date = date(birth_year, birth_month, birth_day)

today = date.today()

age = today.year - birth_date.year

print("Age :", age)