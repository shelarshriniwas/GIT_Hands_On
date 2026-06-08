# Inventory management using Counter.
from collections import Counter

inventory = Counter()

inventory["Laptop"] += 5
inventory["Mouse"] += 10

print(inventory)

inventory["Laptop"] -= 2

print("Updated Inventory")
print(inventory)