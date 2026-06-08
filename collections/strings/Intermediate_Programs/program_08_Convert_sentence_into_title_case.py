# program_08_Convert_sentence_into_title_case.py

sentence = "python aws docker"

print(sentence.title())

sentence = "python aws docker"

words = sentence.split()

result = []

for word in words:
    result.append(word.capitalize())

print(" ".join(result))