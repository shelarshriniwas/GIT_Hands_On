# program_04_JSON-like_nested_dictionary_handling.py

response = {
    "status": "success",

    "data": {
        "user": {
            "name": "Rahul",
            "email": "rahul@gmail.com"
        }
    }
}

print(response["data"]["user"]["name"])