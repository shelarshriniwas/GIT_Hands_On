# Create program using sys.exit().

import sys

choice = input("Enter Choice (yes/no) : ")

if choice == "no":
    sys.exit("Program Terminated")

print("Program Running")
