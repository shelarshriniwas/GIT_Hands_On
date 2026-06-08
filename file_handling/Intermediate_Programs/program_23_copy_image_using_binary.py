# program_23_copy_image_using_binary.py

with open("image.jpg", "rb") as file:

    data = file.read()

with open("copy_image.jpg", "wb") as file:

    file.write(data)

print("Image Copied")