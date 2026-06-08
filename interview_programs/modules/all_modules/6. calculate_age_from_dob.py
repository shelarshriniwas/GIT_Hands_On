from datetime import datetime

dob = "15-08-2000"

birth = datetime.strptime(dob,"%d-%m-%Y")

age = datetime.now().year - birth.year

print(age,"Years")