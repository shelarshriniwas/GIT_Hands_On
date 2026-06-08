# program_09_navigation_bar.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <a href='/'>Home</a> |
    <a href='/about'>About</a> |
    <a href='/contact'>Contact</a>
    """

@app.route("/about")
def about():
    return "About Page"

@app.route("/contact")
def contact():
    return "Contact Page"

if __name__ == "__main__":
    app.run(debug=True)