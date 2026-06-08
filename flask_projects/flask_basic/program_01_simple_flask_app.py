# program_01_simple_flask_app.py

from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask!"

if __name__ == "__main__":
    app.run(debug=True)