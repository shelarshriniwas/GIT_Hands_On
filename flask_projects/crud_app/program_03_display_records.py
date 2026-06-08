# program_03_display_records.py

from flask import Flask
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("crud.db", check_same_thread=False)
cur = conn.cursor()

@app.route("/")
def display():

    cur.execute(
        "SELECT * FROM students"
    )

    rows = cur.fetchall()

    html = "<h2>Student Records</h2>"

    for row in rows:
        html += f"{row}<br>"

    return html

if __name__ == "__main__":
    app.run(debug=True)