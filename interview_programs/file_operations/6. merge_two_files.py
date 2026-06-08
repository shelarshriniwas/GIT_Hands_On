files = ["file1.txt","file2.txt"]

with open("merged.txt","w") as out:
    for file in files:
        with open(file) as f:
            out.write(f.read())

print("merged.txt created")