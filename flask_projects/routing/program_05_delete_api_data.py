# program_05_delete_api_data.py

from flask import Flask, jsonify

app = Flask(__name__)

students = [
    {"id":1,"name":"Amit"},
    {"id":2,"name":"Rahul"}
]

@app.route("/student/<int:id>", methods=["DELETE"])
def delete_student(id):

    global students

    students = [
        s for s in students
        if s["id"] != id
    ]

    return jsonify({
        "message":"Deleted Successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)