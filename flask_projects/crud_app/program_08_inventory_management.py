# program_08_inventory_management.py

from flask import Flask, request, redirect
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("inventory.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
price REAL,
quantity INTEGER
)
""")

conn.commit()

@app.route("/")
def home():

    cur.execute("SELECT * FROM products")
    products = cur.fetchall()

    html = """
    <h2>Inventory Management</h2>

    <form method="post" action="/add">

    Name:
    <input name="name">

    Price:
    <input name="price">

    Quantity:
    <input name="quantity">

    <input type="submit">

    </form><hr>
    """

    for p in products:
        html += f"{p}<br>"

    return html

@app.route("/add", methods=["POST"])
def add():

    cur.execute(
        """
        INSERT INTO products
        (name,price,quantity)
        VALUES(?,?,?)
        """,
        (
            request.form["name"],
            request.form["price"],
            request.form["quantity"]
        )
    )

    conn.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)