# program_29_encrypt_text_file.py

file_name = input("Enter File Name : ")

with open(file_name, "r") as file:

    data = file.read()

encrypted = ""

for char in data:
    encrypted += chr(ord(char) + 3)

with open("encrypted.txt", "w") as file:

    file.write(encrypted)

print("File Encrypted")