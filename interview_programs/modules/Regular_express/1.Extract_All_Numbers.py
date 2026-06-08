'''
Program 1.Extract_All_Numbers.py
text = "Ram scored 95 marks and Shyam scored 88"

Output:

['95', '88']
'''

import re

text = input("Enter the text include number and char: ")

numbers = re.findall(r'\d+', text)

print(numbers)