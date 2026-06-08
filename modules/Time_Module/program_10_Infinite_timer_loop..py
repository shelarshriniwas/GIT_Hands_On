# Infinite timer loop.
import time

counter = 1

while True:

    print("Timer :", counter)

    time.sleep(1)

    counter += 1