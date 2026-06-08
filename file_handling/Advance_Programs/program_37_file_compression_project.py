# program_37_file_compression_project.py

with open("data.txt", "r") as file:

    data = file.read()

compressed = data.replace(" ", "")

with open("compressed.txt", "w") as file:

    file.write(compressed)

print("File Compressed")