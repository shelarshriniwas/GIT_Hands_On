# program_07_notes_application.py

from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("notes.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS notes(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT,
content TEXT
)
""")

conn.commit()

@app.route("/")
def home():

    cur.execute("SELECT * FROM notes")
    notes = cur.fetchall()

    html = """
    <h2>Notes App</h2>

    <form method="post" action="/add">

    Title:
    <input name="title"><br><br>

    Content:
    <textarea name="content"></textarea><br><br>

    <input type="submit">

    </form><hr>
    """

    for note in notes:
        html += f"""
        <b>{note[1]}</b><br>
        {note[2]}<hr>
        """

    return html

@app.route("/add", methods=["POST"])
def add():

    cur.execute(
        "INSERT INTO notes(title,content) VALUES(?,?)",
        (
            request.form["title"],
            request.form["content"]
        )
    )

    conn.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)