# program_03_Sort_dictionary_by_keys.py

data = {
    "b": 20,
    "a": 10,
    "c": 30
}

sorted_data = dict(sorted(data.items()))

print(sorted_data)