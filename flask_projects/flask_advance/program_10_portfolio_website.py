# program_10_portfolio_website.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    return """
    <html>

    <head>
        <title>Portfolio</title>
    </head>

    <body>

    <h1>Shriniwas</h1>

    <h2>AWS Cloud Engineer</h2>

    <h3>Skills</h3>

    <ul>
        <li>AWS</li>
        <li>Terraform</li>
        <li>Docker</li>
        <li>Kubernetes</li>
        <li>Python</li>
    </ul>

    <h3>Projects</h3>

    <ul>
        <li>Online Banking System</li>
        <li>E-Commerce Website</li>
        <li>Hospital Management System</li>
    </ul>

    <h3>Contact</h3>

    <p>Email: example@gmail.com</p>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)