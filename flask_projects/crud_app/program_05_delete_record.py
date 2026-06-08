# program_05_delete_record.py

from flask import Flask, request
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("crud.db", check_same_thread=False)
cur = conn.cursor()

@app.route("/", methods=["GET","POST"])
def delete():

    if request.method == "POST":

        id = request.form["id"]

        cur.execute(
            "DELETE FROM students WHERE id=?",
            (id,)
        )

        conn.commit()

        return "Record Deleted"

    return """
    <form method="post">

        Student ID:
        <input name="id">

        <input type="submit"
               value="Delete">

    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)