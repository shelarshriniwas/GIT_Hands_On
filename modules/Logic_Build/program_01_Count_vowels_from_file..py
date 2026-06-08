# Count vowels from file.
vowels = "aeiouAEIOU"

count = 0

with open("file.txt", "r") as f:
    for line in f:
        for char in line:
            if char in vowels:
                count += 1

print(count)