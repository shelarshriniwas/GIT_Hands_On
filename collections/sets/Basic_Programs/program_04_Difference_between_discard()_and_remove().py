# program_04_Difference_between_discard()_and_remove().py

n = int(input("no of elements want to add in set: "))
set1 = set()

for i in range(n):
    set1.add(int(input()))

print(set1)

n1 = int(input("elements want to remove from set: "))
set1.remove(n1)
print(set1)

n2 = int(input("elements want to discard from set: "))
set1.discard(n2)
print(set1)

