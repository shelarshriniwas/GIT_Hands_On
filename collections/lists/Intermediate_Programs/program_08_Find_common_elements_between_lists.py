# program_08_Find_common_elements_between_lists.py

n = int(input("Enter the no of elements want to add in list-1: "))
l1 = []
l2 =[]


for i in range(n):
    l1.append(int(input()))

n2 = int(input("Enter the no of elements want to add in list-2: "))
for i in range(n2):
    l2.append(int(input()))

print(l1)
print(l2)

print("Using set : ",list(set(l1) and set(l2)))