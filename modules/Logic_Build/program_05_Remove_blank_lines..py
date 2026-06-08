# Remove blank lines.
with open("file.txt", "r") as f:
    lines = f.readlines()

with open("clean.txt", "w") as f:
    for line in lines:
        if line.strip() != "":
            f.write(line)

# — List filter
with open("file.txt", "r") as f:
    lines = f.read().splitlines()

clean = [l for l in lines if l.strip()]

print("\n".join(clean))