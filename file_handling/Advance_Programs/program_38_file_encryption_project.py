# program_38_file_encryption_project.py

with open("data.txt", "r") as file:

    data = file.read()

encrypted = ""

for char in data:
    encrypted += chr(ord(char) + 5)

with open("encrypted.txt", "w") as file:

    file.write(encrypted)

print("Encrypted Successfully")