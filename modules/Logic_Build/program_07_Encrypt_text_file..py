# Encrypt text file.
with open("file.txt", "r") as f:
    text = f.read()

encrypted = ""

for c in text:
    encrypted += chr(ord(c) + 1)

with open("encrypted.txt", "w") as f:
    f.write(encrypted)

print("Encrypted")