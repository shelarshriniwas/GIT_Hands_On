'''
Input: python
Output:    nohtyp
'''

s1 = "python"

print(s1[::-1])

rev = ""

for ch in s1:
    rev = ch + rev

print(rev)