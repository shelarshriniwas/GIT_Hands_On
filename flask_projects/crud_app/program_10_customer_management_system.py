# program_10_customer_management_system.py

from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect(
    "customer.db",
    check_same_thread=False
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS customers(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
email TEXT,
mobile TEXT
)
""")

conn.commit()

@app.route("/")
def home():

    cur.execute(
        "SELECT * FROM customers"
    )

    customers = cur.fetchall()

    html = """
    <h2>Customer Management System</h2>

    <form method="post" action="/add">

    Name:
    <input name="name"><br><br>

    Email:
    <input name="email"><br><br>

    Mobile:
    <input name="mobile"><br><br>

    <input type="submit">

    </form><hr>
    """

    for customer in customers:

        html += f"""
        ID:{customer[0]}
        |
        {customer[1]}
        |
        {customer[2]}
        |
        {customer[3]}
        <br>
        """

    return html

@app.route("/add", methods=["POST"])
def add():

    cur.execute(
        """
        INSERT INTO customers
        (name,email,mobile)
        VALUES(?,?,?)
        """,
        (
            request.form["name"],
            request.form["email"],
            request.form["mobile"]
        )
    )

    conn.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)