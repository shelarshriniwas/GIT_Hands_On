# program_05_Compare_two_sets.py

n = int(input("Enter the no of elements want to add in set1 : "))
n2 = int(input("Enter the no of elements want to add in set2 : "))

set1 = set()
set2 = set()

for i in range(n):
    set1.add(int(input()))

print("Set-1 : ",set1)

for i in range(n2):
    set2.add(int(input()))

print("Set-2 : ",set2)

print(set1 == set2)