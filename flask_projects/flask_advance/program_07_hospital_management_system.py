# program_07_hospital_management_system.py

from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("hospital.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS patients(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
disease TEXT
)
""")
conn.commit()

@app.route("/")
def home():

    cur.execute("SELECT * FROM patients")
    data = cur.fetchall()

    html = """
    <h2>Hospital Management</h2>

    <form method="post" action="/add">
    Name:
    <input name="name">

    Disease:
    <input name="disease">

    <input type="submit">
    </form>

    <hr>
    """

    for row in data:
        html += f"{row}<br>"

    return html

@app.route("/add", methods=["POST"])
def add():

    name = request.form["name"]
    disease = request.form["disease"]

    cur.execute(
        "INSERT INTO patients(name,disease) VALUES(?,?)",
        (name,disease)
    )

    conn.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)