# program_01_Create_a_list_and_print_all_elements.py

n = int(input("Enter no of elements want to store in list : "))
l1 = []

for i in range(n):
    l1.append(int(input()))

print("All elemts of List : \n",l1)