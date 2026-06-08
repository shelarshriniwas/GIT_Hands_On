# program_15_registration_form.py

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def register():

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        return f"""
        Registration Successful<br>
        Name : {name}<br>
        Email : {email}
        """

    return """
    <form method="post">
        Name:
        <input type="text" name="name"><br><br>

        Email:
        <input type="email" name="email"><br><br>

        <input type="submit">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)