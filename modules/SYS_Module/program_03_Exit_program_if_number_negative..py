# Exit program if number negative.

import sys

number = int(input("Enter Number : "))

if number < 0:
    sys.exit("Negative Number Not Allowed")

print("Valid Number")