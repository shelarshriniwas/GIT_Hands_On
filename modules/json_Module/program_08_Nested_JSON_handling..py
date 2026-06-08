import json

students = {
    "101": {
        "name": "Shri",
        "marks": 90
    },
    "102": {
        "name": "Ram",
        "marks": 85
    }
}

with open("nested.json", "w") as file:

    json.dump(students, file, indent=4)

print("Nested JSON Created")