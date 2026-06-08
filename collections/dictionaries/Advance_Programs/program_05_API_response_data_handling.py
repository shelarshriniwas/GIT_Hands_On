# program_05_API_response_data_handling.py

api_response = {
    "id": 101,
    "name": "Rahul",
    "skills": ["Python", "AWS", "Docker"]
}

print(api_response["name"])

for skill in api_response["skills"]:
    print(skill)