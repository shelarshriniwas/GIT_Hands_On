# program_03_Remove_elements_using_remove().py

n = int(input("no of elements want to add in set: "))
set1 = set()

for i in range(n):
    set1.add(int(input()))

print(set1)

n1 = int(input("elements want to remove from set: "))
set1.remove(n1)

print(set1)