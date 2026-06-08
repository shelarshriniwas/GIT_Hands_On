'''
Input:

01-01-2025
10-01-2025

Output:

9 Days

'''

from datetime import datetime

date1 = input("Enter First Date (dd-mm-yyyy): ")
date2 = input("Enter Second Date (dd-mm-yyyy): ")

d1 = datetime.strptime(date1, "%d-%m-%Y")
d2 = datetime.strptime(date2, "%d-%m-%Y")

print((d2 - d1).days, "Days")