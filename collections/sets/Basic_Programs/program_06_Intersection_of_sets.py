# program_06_Intersection_of_sets.py

n = int(input("no of elements want to add in set-1: "))
set1 = set()

for i in range(n):
    set1.add(int(input()))

print(set1)

set2 = {6,7}

set1.update(set2)

print(set1)