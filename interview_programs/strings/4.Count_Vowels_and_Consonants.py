'''
Input:  python
Output:
Vowels = 1
Consonants = 5
'''

s = input("Enter the string : ")
vowels = "aeiou"
v_count = 0
count = 0

for i in s.lower():
    if i in vowels:
        v_count += 1 
    else:
        count += 1

print(f"Total Vowels in String: {v_count} and Total Consonants: {count} ") 

