# program_09_Perform_list_comprehension_examples.py

n = int(input("Enter the no of elements want to add in list: "))
l1 = []

for i in range(n):
    l1.append(int(input()))

print(l1)

even = [i for i in l1 if i%2==0]
print(even)
