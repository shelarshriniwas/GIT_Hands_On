# Queue using deque.
from collections import deque

queue = deque()

queue.append(100)
queue.append(200)
queue.append(300)

print("Queue :", queue)

removed = queue.popleft()

print("Removed :", removed)

print("Updated Queue :", queue)