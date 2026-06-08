# program_04_put_api_data.py

from flask import Flask, request, jsonify

app = Flask(__name__)

student = {
    "id":1,
    "name":"Amit"
}

@app.route("/student", methods=["PUT"])
def update_student():

    data = request.get_json()

    student["name"] = data["name"]

    return jsonify(student)

if __name__ == "__main__":
    app.run(debug=True)