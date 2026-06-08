# Most common word finder.
from collections import Counter

sentence = input("Enter Sentence : ")

words = sentence.split()

frequency = Counter(words)

common = frequency.most_common(1)

print("Most Common Word :", common)