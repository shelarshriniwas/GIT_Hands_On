# program_06_display_user_input.py

from flask import Flask

app = Flask(__name__)

@app.route("/user/<name>")
def user(name):
    return f"Welcome {name}"

if __name__ == "__main__":
    app.run(debug=True)