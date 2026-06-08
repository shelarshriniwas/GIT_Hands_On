# program_22_replace_word_in_file.py

path2 = r"C:\Users\Shriniwas\VS_Codes\Python_Projects\file_handling\file2.txt"

old_word = input("Enter Old Word : ")
new_word = input("Enter New Word : ")

with open(path2, "r") as file:
    data = file.read()

data = data.replace(old_word, new_word)

with open(path2, "w") as file:
    file.write(data)

print("Word Replaced Successfully")