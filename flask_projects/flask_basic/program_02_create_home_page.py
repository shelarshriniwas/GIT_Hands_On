# program_02_create_home_page.py

from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Flask Home!"

if __name__ == "__main__":
    app.run(debug=True)