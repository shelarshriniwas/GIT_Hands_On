# program_10_Check_anagram.py

text1 = "listen"
text2 = "silent"

if sorted(text1) == sorted(text2):
    print("Anagram")

else:
    print("Not Anagram")


text1 = "listen"
text2 = "silent"

frequency1 = {}
frequency2 = {}

for char in text1:
    frequency1[char] = frequency1.get(char, 0) + 1

for char in text2:
    frequency2[char] = frequency2.get(char, 0) + 1

print(frequency1 == frequency2)