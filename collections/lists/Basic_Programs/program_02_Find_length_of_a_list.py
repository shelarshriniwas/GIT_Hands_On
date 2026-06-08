# program_02_Find_length_of_a_list.py

n = int(input("Enter no of elements want to store in list : "))
l1 = []

for i in range(n):
    l1.append(int(input()))

print("Length of list using len() : ",len(l1))

count = 0
for i in l1:
    count +=1

print("Length of list using loop : ",count)
