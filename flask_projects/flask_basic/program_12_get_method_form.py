# program_12_get_method_form.py

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <form action="/result" method="get">
        Name:
        <input type="text" name="name">
        <input type="submit">
    </form>
    """

@app.route("/result")
def result():
    name = request.args.get("name")
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(debug=True)
