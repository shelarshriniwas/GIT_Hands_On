# program_06_Delete_elements_using_pop().py
n = int(input("Enter no of elements want to store in list : "))
l1 = []

for i in range(n):
    l1.append(int(input()))

print(l1)

l1.pop() # if we provide any value in pop(value) it will remove from list index value liek pop(2) means elemen of index 2 will remove  

print(l1)
