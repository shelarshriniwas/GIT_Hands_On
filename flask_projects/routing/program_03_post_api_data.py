# program_03_post_api_data.py

from flask import Flask, request, jsonify

app = Flask(__name__)

students = []

@app.route("/student", methods=["POST"])
def add_student():

    data = request.get_json()

    students.append(data)

    return jsonify({
        "message":"Student Added",
        "data":data
    })

if __name__ == "__main__":
    app.run(debug=True)