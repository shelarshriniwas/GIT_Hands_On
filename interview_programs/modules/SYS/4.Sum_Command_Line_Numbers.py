'''
Input:

python add.py 10 20 30

Output:

60 
'''

# add.py

import sys

total = 0

for i in sys.argv[1:]:
    total += int(i)

print(total)

# Logic - 2 
'''
import sys
numbers = list(map(int, sys.argv[1:]))
print(sum(numbers))
'''