

print("First make sure file 1 and file 2 is created")

with open("file.txt","r") as f1:
    data = f1.read()

print("Total Characters: ",len(data))



