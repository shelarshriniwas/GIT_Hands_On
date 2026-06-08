# program_07_Difference_of_sets.py

n = int(input("no of elements want to add in set-1: "))
set1 = set()

for i in range(n):
    set1.add(int(input()))

print(set1)

n2 = int(input("no of elements want to add in set-2: "))
set2 = set()

for i in range(n):
    set2.add(int(input()))

print(set2)

print(set1.difference(set2))

print(set2.difference(set1))