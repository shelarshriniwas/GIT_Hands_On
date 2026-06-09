
print("First make sure file 1 and file 2 is created")

with open("file.txt","r") as f1:
    data = f1.read()


with open("file2.txt","w") as f2:
    f2.write(data)