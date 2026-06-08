# Remove extra spaces.
with open("file.txt", "r") as f:
    text = f.read()

clean = " ".join(text.split())

print(clean)