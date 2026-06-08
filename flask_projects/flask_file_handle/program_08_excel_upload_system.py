# program_08_excel_upload_system.py

from flask import Flask, request
import os

app = Flask(__name__)

EXCEL_FOLDER = "excel_files"
os.makedirs(EXCEL_FOLDER, exist_ok=True)

@app.route("/", methods=["GET","POST"])
def upload_excel():

    if request.method == "POST":

        file = request.files["excel"]

        if file.filename.endswith((".xlsx",".xls")):

            file.save(
                os.path.join(
                    EXCEL_FOLDER,
                    file.filename
                )
            )

            return "Excel Uploaded"

        return "Only Excel Files Allowed"

    return """
    <h2>Excel Upload System</h2>

    <form method="POST"
          enctype="multipart/form-data">

        <input type="file" name="excel">

        <input type="submit">

    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
