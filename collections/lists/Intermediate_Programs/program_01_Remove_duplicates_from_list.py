# program_01_Remove_duplicates_from_list.py

n = int(input("Enter the no of elements want to add in list: "))
l1 = []

for i in range(n):
    l1.append(int(input()))

print(l1)

print("Using set : ",list(set(l1)))

