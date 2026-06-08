# program_01_simple_rest_api.py

from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "Simple REST API Working"

if __name__ == "__main__":
    app.run(debug=True)