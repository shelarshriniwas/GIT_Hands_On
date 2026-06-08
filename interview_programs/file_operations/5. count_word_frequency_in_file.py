freq = {}

with open("sample.txt") as file:
    for word in file.read().split():
        freq[word] = freq.get(word, 0) + 1

print(freq)
