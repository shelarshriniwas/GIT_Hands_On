# program_07_Replace_substring.py

text = "I love Java"

result = text.replace("Java", "Python")

print(result)

# Logic 2
text2 = "I love Java"

words2 = text2.split()

for i in range(len(words2)):

    if words2[i] == "Java":
        words2[i] = "Python"

result2 = " ".join(words2)

print(result2)