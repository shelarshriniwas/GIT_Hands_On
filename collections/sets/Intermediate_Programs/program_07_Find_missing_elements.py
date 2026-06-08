# program_07_Find_missing_elements.py

full_list = [1, 2, 3, 4, 5]

current_list = [1, 2, 5]

missing = []

for item in full_list:
    if item not in current_list:
        missing.append(item)

print(missing)