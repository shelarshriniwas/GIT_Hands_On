# program_02_Merge_two_lists.py

n = int(input("Enter the no of elements want to add in list-1: "))
l1 = []
l2 = []

for i in range(n):
    l1.append(int(input()))

n1 = int(input("Enter the no of elements want to add in list-2: "))
for i in range(n1):
    l2.append(int(input()))

print("List-1 : ",l1)
print("List-2 : ",l2)

print(l1+l2)
