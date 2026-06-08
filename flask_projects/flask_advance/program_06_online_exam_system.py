# program_06_online_exam_system.py

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def exam():

    if request.method == "POST":

        score = 0

        if request.form["q1"] == "Python":
            score += 1

        if request.form["q2"] == "Flask":
            score += 1

        return f"Score = {score}/2"

    return """
    <h2>Online Exam</h2>

    <form method="post">

    Q1: Which language are we using?
    <input type="text" name="q1"><br><br>

    Q2: Flask is?
    <input type="text" name="q2"><br><br>

    <input type="submit">

    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)