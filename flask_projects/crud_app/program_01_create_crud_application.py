# program_01_create_crud_application.py

from flask import Flask
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("crud.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT
)
""")

conn.commit()

@app.route("/")
def home():
    return "CRUD Application Created Successfully"

if __name__ == "__main__":
    app.run(debug=True)