'''
Program 1.Check_Palindrome.py
text = "madam"

Output:

Palindrome
'''

text = input("Enter the string: ")

if text == text[::-1]:
    print("Palinddrome")
else:
    print("Not Palindrome")