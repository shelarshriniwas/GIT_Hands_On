# program_08_attendance_management_system.py

from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("attendance.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS attendance(
id INTEGER PRIMARY KEY AUTOINCREMENT,
student TEXT,
status TEXT
)
""")
conn.commit()

@app.route("/")
def home():

    cur.execute("SELECT * FROM attendance")
    data = cur.fetchall()

    html = """
    <h2>Attendance System</h2>

    <form method="post" action="/mark">

    Student:
    <input name="student">

    Status:
    <select name="status">
        <option>Present</option>
        <option>Absent</option>
    </select>

    <input type="submit">

    </form><hr>
    """

    for row in data:
        html += f"{row}<br>"

    return html

@app.route("/mark", methods=["POST"])
def mark():

    cur.execute(
        "INSERT INTO attendance(student,status) VALUES(?,?)",
        (
            request.form["student"],
            request.form["status"]
        )
    )

    conn.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)