'''
Input: Hello@123#
Output: 2
'''

s1 = "Hello@123#"
num = 0
char = 0
total = 0

for ch in s1:
    if ch.isalnum():
        num += 1 
    elif ch.isalpha():
        char += 1
    else:
        total = len(s1) - num -char 

print("Total Special Char : ", total)