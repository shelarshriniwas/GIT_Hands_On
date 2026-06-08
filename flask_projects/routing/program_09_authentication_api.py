# program_09_authentication_api.py


from flask import Flask, request, jsonify

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "123"

@app.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == USERNAME and password == PASSWORD:

        return jsonify({
            "message":"Login Successful"
        })

    return jsonify({
        "message":"Invalid Credentials"
    })

if __name__ == "__main__":
    app.run(debug=True)