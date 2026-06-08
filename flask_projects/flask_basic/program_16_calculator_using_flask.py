# program_16_calculator_using_flask.py

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def calculator():

    if request.method == "POST":

        num1 = int(request.form["num1"])
        num2 = int(request.form["num2"])

        result = num1 + num2

        return f"Result = {result}"

    return """
    <form method="post">
        Number 1:
        <input type="number" name="num1"><br><br>

        Number 2:
        <input type="number" name="num2"><br><br>

        <input type="submit" value="Add">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)