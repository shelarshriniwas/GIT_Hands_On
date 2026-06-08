# program_14_login_form.py

from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "123":
            return "Login Successful"
        else:
            return "Invalid Login"

    return """
    <form method="post">
        Username:
        <input type="text" name="username"><br><br>

        Password:
        <input type="password" name="password"><br><br>

        <input type="submit" value="Login">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)