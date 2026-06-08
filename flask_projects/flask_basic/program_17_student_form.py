# program_17_student_form.py

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def student():

    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]

        return f"""
        Student Name : {name}<br>
        Course : {course}
        """

    return """
    <form method="post">
        Name:
        <input type="text" name="name"><br><br>

        Course:
        <input type="text" name="course"><br><br>

        <input type="submit">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)