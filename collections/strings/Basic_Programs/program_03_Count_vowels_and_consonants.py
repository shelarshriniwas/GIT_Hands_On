# program_03_Count_vowels_and_consonants.py

text = "Python"

vowels = "aeiou"

vowel_count = 0
consonant_count = 0

for char in text.lower():

    if char.isalpha():

        if char in vowels:
            vowel_count += 1

        else:
            consonant_count += 1

print("Vowels :", vowel_count)
print("Consonants :", consonant_count)