'''
Input
1 2 3 4 5 6
Output
Even: 2 4 6
Odd: 1 3 5
'''

l1 = [1,2,3,4,5,6]

even = [x for x in l1 if x%2==0]

odd = [x for x in l1 if x%2 != 0]

print("Even : ",even)
print("Odd : ",odd)