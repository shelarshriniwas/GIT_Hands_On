# Count duplicate words.
with open("file.txt", "r") as f:
    words = f.read().split()

freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

for k, v in freq.items():
    if v > 1:
        print(k, v)

# Using Set

with open("file.txt", "r") as f:
    words = f.read().split()

duplicates = set([w for w in words if words.count(w) > 1])

print(duplicates)