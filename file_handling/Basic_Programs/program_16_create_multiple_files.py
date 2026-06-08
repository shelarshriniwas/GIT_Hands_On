# program_16_create_multiple_files.py

total = int(input("How Many Files : "))

for i in range(1, total + 1):

    file_name = input("Enter File Name : ")

    with open(file_name, "w") as file:
        file.write("File Created")

print("Files Created Successfully")