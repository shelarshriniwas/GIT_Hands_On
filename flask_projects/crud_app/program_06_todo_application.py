# program_06_todo_application.py

from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("todo.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS todo(
id INTEGER PRIMARY KEY AUTOINCREMENT,
task TEXT
)
""")

conn.commit()

@app.route("/")
def home():

    cur.execute(
        "SELECT * FROM todo"
    )

    tasks = cur.fetchall()

    html = """
    <h2>Todo Application</h2>

    <form method="post" action="/add">

    Task:
    <input name="task">

    <input type="submit">

    </form><hr>
    """

    for task in tasks:
        html += f"{task}<br>"

    return html

@app.route("/add", methods=["POST"])
def add():

    task = request.form["task"]

    cur.execute(
        "INSERT INTO todo(task) VALUES(?)",
        (task,)
    )

    conn.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)