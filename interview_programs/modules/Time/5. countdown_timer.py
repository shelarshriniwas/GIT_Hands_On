'''
Input
10 Seconds
Output
10
9
8
...
0
'''

import time

for i in range(10, -1, -1):
    print(i)
    time.sleep(1)