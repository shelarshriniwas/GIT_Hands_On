# program_08_Count_words_in_sentence.py

sentence = "Python AWS Docker"

count = 1

for char in sentence:

    if char == " ":
        count += 1

print(count)