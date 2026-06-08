# program_02_get_api_data.py

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/students", methods=["GET"])
def get_students():

    students = [
        {"id":1,"name":"Amit"},
        {"id":2,"name":"Rahul"},
        {"id":3,"name":"Priya"}
    ]

    return jsonify(students)

if __name__ == "__main__":
    app.run(debug=True)