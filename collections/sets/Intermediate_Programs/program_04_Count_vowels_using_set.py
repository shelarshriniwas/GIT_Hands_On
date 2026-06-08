# program_04_Count_vowels_using_set.py

text = input("Enter the sentence : ")
vowels = {"a","e","i","o","u"}

count = 0

for i in text.lower():
    if i in vowels:
        count +=1

print("Total Count = ",count)
