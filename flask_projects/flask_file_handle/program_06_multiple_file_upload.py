# program_06_multiple_file_upload.py

from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "multiple_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET","POST"])
def upload():

    if request.method == "POST":

        files = request.files.getlist("files")

        for file in files:

            file.save(
                os.path.join(
                    UPLOAD_FOLDER,
                    file.filename
                )
            )

        return "Multiple Files Uploaded"

    return """
    <h2>Multiple File Upload</h2>

    <form method="POST"
          enctype="multipart/form-data">

        <input type="file"
               name="files"
               multiple>

        <input type="submit">

    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)