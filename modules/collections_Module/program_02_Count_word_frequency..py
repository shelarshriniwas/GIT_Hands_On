# Count word frequency.
from collections import Counter

sentence = input("Enter Sentence : ")

words = sentence.split()

frequency = Counter(words)

print(frequency)