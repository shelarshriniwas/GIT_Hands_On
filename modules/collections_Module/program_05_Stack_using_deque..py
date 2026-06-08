# Stack using deque.
from collections import deque

stack = deque()

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack :", stack)

removed = stack.pop()

print("Removed :", removed)

print("Updated Stack :", stack)