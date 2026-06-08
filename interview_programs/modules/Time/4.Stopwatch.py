'''
Input:
Start
Wait 5 Seconds
Stop

Output:

Elapsed Time = 5 Seconds
'''

import time

input("Press Enter To Start Stopwatch")

start = time.time()

input("Press Enter To Stop Stopwatch")

end = time.time()

total = end - start

print("Elapsed Time :", total, "seconds")