# program_34_password_manager.py

website = input("Enter Website : ")
password = input("Enter Password : ")

with open("passwords.txt", "a") as file:

    file.write(website + " : " + password + "\n")

print("Password Saved")