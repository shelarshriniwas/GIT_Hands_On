import os

# Take folder path from user
base_path = input("Enter folder path where files should be created: ")

# Create folder if it does not exist
os.makedirs(base_path, exist_ok=True)

# Read input lines from file.txt
with open("f.txt", "r") as f:
    lines = f.readlines()

# Process each line
for i, line in enumerate(lines, start=1):

    line = line.strip()

    if not line:
        continue

    # Replace spaces with underscore
    file_name_part = line.replace(" ", "_")

    # Final file name
    file_name = f"program_{i:02d}_{file_name_part}py"

    # Full path
    full_path = os.path.join(base_path, file_name)

    # Create file
    with open(full_path, "w") as f:
        f.write(f"#{file_name}")

    print("Created:", full_path)