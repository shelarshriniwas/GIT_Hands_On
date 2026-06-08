n = int(input("Enter no of elements want to store in list : "))
l1 = []

for i in range(n):
    l1.append(int(input()))


min = l1[0]
max = l1[0]

print(l1)

for i in l1:
    if i > max:
        max = i
    if i < min:
        min = i

print("Max: ",max)
print("Min: ",min)