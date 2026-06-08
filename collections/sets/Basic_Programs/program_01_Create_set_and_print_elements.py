# program_01_Create_set_and_print_elements.py

n = int(input("no of elements want to add in set: "))
set1 = set()

for i in range(n):
    set1.add(int(input()))

print(set1)