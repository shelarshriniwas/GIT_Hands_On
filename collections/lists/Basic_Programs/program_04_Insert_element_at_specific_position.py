# program_04_Insert_element_at_specific_position.py
n = int(input("Enter no of elements want to store in list : "))
l1 = []

for i in range(n):
    l1.append(int(input()))

print(l1)

print("Enter the index and num want to add in list")
ele = int(input("Element : "))
index = int(input("Index: "))

l1.insert(index,ele)
print("After adding element using insert l1",l1)