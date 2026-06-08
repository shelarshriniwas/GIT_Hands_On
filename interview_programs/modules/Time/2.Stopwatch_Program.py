'''
Program 2.Stopwatch_Program.py

Output:

Start
Stop
Elapsed Time = X sec
'''

import time

input("Press Enter To Start Stopwatch")

start = time.time()

input("Press Enter To Stop Stopwatch")

end = time.time()

total = end - start

print("Elapsed Time :", total, "seconds")