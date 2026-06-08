# program_05_Remove_elements_using_remove().py
n = int(input("Enter no of elements want to store in list : "))
l1 = []

for i in range(n):
    l1.append(int(input()))

print(l1)

r = int(input("Enter nu which is want to remove form list"))

l1.remove(r)

print("After remove element: ",l1)