# program_10_Remove_duplicates_from_list_using_set.py


n = int(input("no of elements want to add in List-1: "))
l1 = []

for i in range(n):
    l1.append(int(input()))

print(l1)

seen =list(set(l1))
print(seen)