# program_18_feedback_form.py

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def feedback():

    if request.method == "POST":
        feedback = request.form["feedback"]

        return f"Feedback Received:<br>{feedback}"

    return """
    <form method="post">
        Feedback:<br>
        <textarea name="feedback"></textarea><br><br>

        <input type="submit">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)