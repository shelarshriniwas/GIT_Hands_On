# program_09_cloud_file_storage.py

from flask import Flask, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET","POST"])
def upload():

    if request.method == "POST":

        file = request.files["file"]

        file.save(
            os.path.join(
                UPLOAD_FOLDER,
                file.filename
            )
        )

        return "File Uploaded Successfully"

    return """
    <h2>Cloud File Storage</h2>

    <form method="post"
          enctype="multipart/form-data">

    <input type="file" name="file">

    <input type="submit">

    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)