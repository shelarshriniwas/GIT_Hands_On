n = int(input("Enter no of elements want to store in list : "))
l1 = []

for i in range(n):
    l1.append(int(input()))

n1 = int(input("Enter the number want to cal total: "))

print(l1.count(n1))