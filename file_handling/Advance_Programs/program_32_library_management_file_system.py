# program_32_library_management_file_system.py

with open("library.txt", "a") as file:

    book = input("Enter Book Name : ")

    file.write(book + "\n")

print("Book Added")