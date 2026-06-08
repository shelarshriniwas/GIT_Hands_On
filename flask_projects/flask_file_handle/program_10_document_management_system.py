# program_10_document_management_system.py

from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)

DOC_FOLDER = "documents"

os.makedirs(DOC_FOLDER, exist_ok=True)

@app.route("/", methods=["GET","POST"])
def home():

    if request.method == "POST":

        file = request.files["document"]

        file.save(
            os.path.join(
                DOC_FOLDER,
                file.filename
            )
        )

    files = os.listdir(DOC_FOLDER)

    html = """
    <h2>Document Management System</h2>

    <form method="POST"
          enctype="multipart/form-data">

        <input type="file"
               name="document">

        <input type="submit"
               value="Upload">

    </form>

    <hr>
    """

    for file in files:

        html += f"""
        <a href='/download/{file}'>
            {file}
        </a><br>
        """

    return html

@app.route("/download/<filename>")
def download(filename):

    return send_from_directory(
        DOC_FOLDER,
        filename,
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)