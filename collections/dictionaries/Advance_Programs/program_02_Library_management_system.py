# program_02_Library_management_system.py

library = {
    "Python": 5,
    "AWS": 3,
    "Docker": 2
}

book = "Python"

if library[book] > 0:

    library[book] -= 1

    print("Book Issued")

else:
    print("Book Not Available")

print(library)