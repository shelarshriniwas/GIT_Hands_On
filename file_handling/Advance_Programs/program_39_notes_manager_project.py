# program_39_notes_manager_project.py

note = input("Enter Note : ")

with open("notes.txt", "a") as file:

    file.write(note + "\n")

print("Note Added")