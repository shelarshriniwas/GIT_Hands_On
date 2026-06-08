'''
Input
Function A
Function B
Output
Function A = 0.02 sec
Function B = 0.01 sec

'''
import time

def function_a():
    for _ in range(1000000):
        pass

start = time.perf_counter()
function_a()
end = time.perf_counter()

print("Execution Time =", round(end-start,4), "sec")