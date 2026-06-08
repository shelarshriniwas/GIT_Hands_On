# program_09_Compress_string.py

text = "aaabbcccc"

result = ""

count = 1

for i in range(len(text) - 1):

    if text[i] == text[i + 1]:
        count += 1

    else:
        result += text[i] + str(count)
        count = 1

result += text[-1] + str(count)

print(result)

text = "aaabbcccc"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)