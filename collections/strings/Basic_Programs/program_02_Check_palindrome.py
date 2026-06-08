# program_02_Check_palindrome.py

s = "madam"

s1 = s[::-1]

print(s1 == s)

text = "moon"

reverse = ""

for char in text:
    reverse = char + reverse

print(reverse)
if text == reverse:
    print("Palindrome")

else:
    print("Not Palindrome")