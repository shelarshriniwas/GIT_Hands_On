# program_09_library_management.py

from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("library.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS books(
id INTEGER PRIMARY KEY AUTOINCREMENT,
book_name TEXT,
author TEXT
)
""")

conn.commit()

@app.route("/")
def home():

    cur.execute("SELECT * FROM books")
    books = cur.fetchall()

    html = """
    <h2>Library Management</h2>

    <form method="post" action="/add">

    Book Name:
    <input name="book_name">

    Author:
    <input name="author">

    <input type="submit">

    </form><hr>
    """

    for book in books:
        html += f"{book}<br>"

    return html

@app.route("/add", methods=["POST"])
def add():

    cur.execute(
        """
        INSERT INTO books
        (book_name,author)
        VALUES(?,?)
        """,
        (
            request.form["book_name"],
            request.form["author"]
        )
    )

    conn.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)