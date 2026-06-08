# program_04_Sort_dictionary_by_values.py

data = {
    "Rahul": 85,
    "Amit": 95,
    "Sneha": 75
}

sorted_data = dict(
    sorted(data.items(), key=lambda item: item[1])
)

print(sorted_data)