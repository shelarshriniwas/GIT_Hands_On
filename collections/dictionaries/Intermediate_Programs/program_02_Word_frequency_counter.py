# program_02_Word_frequency_counter.py

text = "python aws python docker aws"

words = text.split()

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] += 1

    else:
        frequency[word] = 1

print(frequency)

