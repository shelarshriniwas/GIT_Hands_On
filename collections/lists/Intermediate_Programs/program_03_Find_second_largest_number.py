# program_03_Find_second_largest_number.py

n = int(input("Enter the no of elements want to add in list: "))
l1 = []

for i in range(n):
    l1.append(int(input()))

print(l1)

largest = second_large = l1[0]

for i in l1:
    if i > largest:
        second_large = largest
        largest = i
    elif i > second_large and i != largest:
        second_large = i

print("second_large: ",second_large)    
l1.sort()
print("After sort: ",l1)
print("Second large using slice: ",l1[-2])