# program_02_add_record.py

from flask import Flask, request

import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("crud.db", check_same_thread=False)
cur = conn.cursor()

@app.route("/", methods=["GET","POST"])
def add():

    if request.method == "POST":

        name = request.form["name"]

        cur.execute(
            "INSERT INTO students(name) VALUES(?)",
            (name,)
        )

        conn.commit()

        return "Record Added"

    return """
    <form method="post">
        Name:
        <input name="name">
        <input type="submit">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)