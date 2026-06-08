# program_10_bootstrap_flask_page.py



from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body class='container mt-5'>
        <h1 class='text-primary'>Bootstrap Flask Page</h1>
        <button class='btn btn-success'>Click</button>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)