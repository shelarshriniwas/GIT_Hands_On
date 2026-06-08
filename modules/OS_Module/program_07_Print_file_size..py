# Print file size.
import os

file_name = input("Enter File Name : ")

size = os.path.getsize(file_name)

print("File Size :", size, "bytes")