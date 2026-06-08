n = int(input("Enter no of elements want to store in list : "))
l1 = []

for i in range(n):
    l1.append(int(input()))

print(l1)

l1.sort()

print("After sort: ",l1)
