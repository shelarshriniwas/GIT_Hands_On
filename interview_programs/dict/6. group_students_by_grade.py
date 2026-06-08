'''
Input:

{
 'Ram':'A',
 'Shyam':'B',
 'Mohan':'A',
 'Ravi':'B'
}

Output:

{
 'A':['Ram','Mohan'],
 'B':['Shyam','Ravi']
}

'''

from collections import defaultdict

students = {
 'Ram':'A',
 'Shyam':'B',
 'Mohan':'A',
 'Ravi':'B'
}

result = defaultdict(list)

for name, grade in students.items():
    result[grade].append(name)

print(dict(result))