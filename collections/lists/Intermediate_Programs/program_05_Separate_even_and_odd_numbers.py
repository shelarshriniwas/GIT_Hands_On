# program_05_Separate_even_and_odd_numbers.py

n = int(input("Enter the no of elements want to add in list: "))
l1 = []
l2 = []
for i in range(n):
    l1.append(int(input()))

print(l1)

even = [i for i in l1 if i%2 == 0]
print(even)

odd = [i for i in l1 if i%2 != 0]
print(odd)