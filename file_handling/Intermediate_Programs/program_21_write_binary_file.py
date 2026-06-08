# program_21_write_binary_file.py

data = b"Hello Python"

with open("binary.dat", "wb") as file:

    file.write(data)

print("Binary File Written")