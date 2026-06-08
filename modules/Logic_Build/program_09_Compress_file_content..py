# Compress file content.
with open("file.txt", "r") as f:
    text = f.read()

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

  # Logic-2
with open("file.txt", "r") as f:
    words = f.read().split()

freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print(freq)