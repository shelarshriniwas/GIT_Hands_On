# program_07_student_rest_api.py

from flask import Flask, jsonify, request

app = Flask(__name__)

students = []

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/students", methods=["POST"])
def add_student():

    data = request.get_json()

    students.append(data)

    return jsonify({
        "message":"Student Added"
    })

@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):

    global students

    students = [
        s for s in students
        if s["id"] != id
    ]

    return jsonify({
        "message":"Deleted"
    })

if __name__ == "__main__":
    app.run(debug=True)