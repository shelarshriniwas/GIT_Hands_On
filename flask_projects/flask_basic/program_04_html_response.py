# program_04_html_response.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Flask HTML Response</h1>
    <h2>Welcome User</h2>
    """

if __name__ == "__main__":
    app.run(debug=True)