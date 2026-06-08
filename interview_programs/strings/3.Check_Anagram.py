'''
Input:  
listen
silent

Output:
Anagram
'''
s1 = input("Enter 1st string: ")
s2 = input("Enter 2nd string: ")


if set(s1) == set(s2):
    print("Anagram")
else:
    print(" Not Anagram")

