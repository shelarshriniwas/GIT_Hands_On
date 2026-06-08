# program_05_chat_application.py


from flask import Flask, request, redirect

app = Flask(__name__)

messages = []

@app.route("/")
def home():

    html = "<h2>Chat Application</h2>"

    for msg in messages:
        html += f"<p>{msg}</p>"

    html += """
    <form method='post' action='/send'>
    <input type='text' name='msg'>
    <input type='submit'>
    </form>
    """

    return html

@app.route("/send", methods=["POST"])
def send():

    messages.append(request.form["msg"])

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)