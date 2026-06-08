# program_09_Phonebook_application.py

phonebook = {
    "Rahul": 9876543210,
    "Amit": 9876501234
}

search = "Rahul"

if search in phonebook:
    print(phonebook[search])

else:
    print("Contact Not Found")