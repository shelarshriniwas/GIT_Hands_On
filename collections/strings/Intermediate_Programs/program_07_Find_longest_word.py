# program_07_Find_longest_word.py

sentence = "I love Python programming"

words = sentence.split()

longest = max(words, key=len)

print(longest)


sentence = "I love Python programming"

words = sentence.split()

longest = ""

for word in words:

    if len(word) > len(longest):
        longest = word

print(longest)