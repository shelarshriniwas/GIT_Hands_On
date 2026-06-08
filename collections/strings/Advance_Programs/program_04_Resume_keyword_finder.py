# program_04_Resume_keyword_finder.py

resume = "Python AWS Docker"

keywords = ["AWS", "Java", "Python"]

for word in keywords:

    if word in resume:
        print(word)