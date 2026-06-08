# Compare two files.
with open("file1.txt", "r") as f1:
    data1 = f1.read()

with open("file2.txt", "r") as f2:
    data2 = f2.read()

if data1 == data2:
    print("Files are same")
else:
    print("Files are different")