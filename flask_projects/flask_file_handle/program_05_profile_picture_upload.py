# program_05_profile_picture_upload.py

from flask import Flask, request
import os

app = Flask(__name__)

PROFILE_FOLDER = "profile_pictures"
os.makedirs(PROFILE_FOLDER, exist_ok=True)

@app.route("/", methods=["GET","POST"])
def profile():

    if request.method == "POST":

        image = request.files["profile"]

        image.save(
            os.path.join(
                PROFILE_FOLDER,
                image.filename
            )
        )

        return "Profile Picture Uploaded"

    return """
    <h2>Profile Upload</h2>

    <form method="POST"
          enctype="multipart/form-data">

        <input type="file" name="profile">

        <input type="submit">

    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)