# Extract numbers from file.
import re

with open("file.txt", "r") as f:
    text = f.read()

nums = re.findall(r"\d+", text)

print(nums)