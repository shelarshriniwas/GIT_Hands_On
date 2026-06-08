# program_02_Find_unique_words_in_sentence.py

sentence = input("Enter the sentence: ")

words = sentence.split()

unique_words = set(words)

print(unique_words)