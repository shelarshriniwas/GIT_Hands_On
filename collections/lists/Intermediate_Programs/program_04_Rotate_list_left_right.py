# program_04_Rotate_list_left_right.py

n = int(input("Enter no of elements want to add in list: "))
numbers = []

for i in range(n):
    numbers.append(int(input()))

r = int(input("enter rotate amount between 1-3 for left and -value for right: "))

result = numbers[r:] + numbers[:r]

print(" Rotated List :", result)