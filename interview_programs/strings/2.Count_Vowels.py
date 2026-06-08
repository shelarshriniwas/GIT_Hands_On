'''
Program 2.Count_Vowels.py
text = "python programming"

Output:

4
'''
text = input("Enter the string: ")
v= "aeiou"
count = 0
for i in text.lower():
    if i in v:
        count +=1
    else:
        continue


print("Total Vowels are: ",count)