# program_19_contact_form.py


from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        return f"""
        Name : {name}<br>
        Email : {email}<br>
        Message : {message}
        """

    return """
    <form method="post">

        Name:
        <input type="text" name="name"><br><br>

        Email:
        <input type="email" name="email"><br><br>

        Message:
        <textarea name="message"></textarea><br><br>

        <input type="submit">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)