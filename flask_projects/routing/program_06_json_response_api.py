# program_06_json_response_api.py

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/info")
def info():

    return jsonify({
        "name":"Shriniwas",
        "role":"AWS Cloud Engineer",
        "experience":"3 Years"
    })

if __name__ == "__main__":
    app.run(debug=True)