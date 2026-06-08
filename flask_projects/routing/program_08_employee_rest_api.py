# program_08_employee_rest_api.py

from flask import Flask, jsonify, request

app = Flask(__name__)

employees = []

@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)

@app.route("/employees", methods=["POST"])
def add_employee():

    emp = request.get_json()

    employees.append(emp)

    return jsonify({
        "message":"Employee Added"
    })

@app.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):

    for emp in employees:

        if emp["id"] == id:

            emp["name"] = request.json["name"]

            return jsonify(emp)

    return jsonify({
        "message":"Not Found"
    })

if __name__ == "__main__":
    app.run(debug=True)