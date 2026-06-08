# program_08_dynamic_webpage.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("dynamic.html", name="Shriniwas")

if __name__ == "__main__":
    app.run(debug=True)

# <h1>Welcome {{ name }}</h1>  code in dynamic.html    