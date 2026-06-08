# Find palindrome words.
with open("file.txt", "r") as f:
    words = f.read().split()

palindromes = [w for w in words if w == w[::-1]]

print(palindromes)