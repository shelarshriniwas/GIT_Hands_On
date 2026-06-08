# program_01_online_banking_system.py

from flask import Flask, request, redirect, render_template_string
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("bank.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS accounts(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
balance REAL
)
""")
conn.commit()

html = """
<h2>Online Banking System</h2>

<form method="post" action="/create">
Name:
<input type="text" name="name">
Balance:
<input type="number" name="balance">
<input type="submit" value="Create Account">
</form>

<hr>

{% for acc in accounts %}
ID: {{acc[0]}} |
{{acc[1]}} |
Balance: ₹{{acc[2]}}
<br>
{% endfor %}
"""

@app.route("/")
def home():
    cur.execute("SELECT * FROM accounts")
    accounts = cur.fetchall()
    return render_template_string(html, accounts=accounts)

@app.route("/create", methods=["POST"])
def create():
    name = request.form["name"]
    balance = request.form["balance"]

    cur.execute(
        "INSERT INTO accounts(name,balance) VALUES(?,?)",
        (name,balance)
    )
    conn.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)