# program_10_Pair of elements_of_target

n = int(input("Enter the no of elements want to add in list: "))
l1 = []
target = int(input("Enter target: "))
for i in range(n):
    l1.append(int(input()))

print(l1)

for i in l1:
    for j in range(i+1,len(l1)):
        if l1[i] + l1[j] == target:
            print(l1[i], l1[j])



