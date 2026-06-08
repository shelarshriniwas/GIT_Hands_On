# program_07_Reverse_a_list.py
n = int(input("Enter no of elements want to store in list : "))
l1 = []

for i in range(n):
    l1.append(int(input()))

print(l1)
l1.reverse()
print(l1)

print(l1[::-1])