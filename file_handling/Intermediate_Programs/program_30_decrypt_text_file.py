# program_30_decrypt_text_file.py

file_name = input("Enter Encrypted File Name : ")

with open(file_name, "r") as file:

    data = file.read()

decrypted = ""

for char in data:
    decrypted += chr(ord(char) - 3)

with open("decrypted.txt", "w") as file:

    file.write(decrypted)

print("File Decrypted")