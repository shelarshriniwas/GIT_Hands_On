# Decrypt text file.
with open("encrypted.txt", "r") as f:
    text = f.read()

decrypted = ""

for c in text:
    decrypted += chr(ord(c) - 1)

print(decrypted)