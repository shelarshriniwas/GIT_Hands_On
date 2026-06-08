# program_04_edit_record.py

from flask import Flask, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("crud.db", check_same_thread=False)
cur = conn.cursor()

@app.route("/", methods=["GET","POST"])
def update():

    if request.method == "POST":

        id = request.form["id"]
        name = request.form["name"]

        cur.execute(
            "UPDATE students SET name=? WHERE id=?",
            (name,id)
        )

        conn.commit()

        return "Record Updated"

    return """
    <form method="post">
        ID:
        <input name="id"><br><br>

        Name:
        <input name="name"><br><br>

        <input type="submit">
    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)