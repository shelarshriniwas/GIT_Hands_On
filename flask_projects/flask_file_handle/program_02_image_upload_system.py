# program_02_image_upload_system.py

from flask import Flask, request
import os

app = Flask(__name__)

IMAGE_FOLDER = "images"
os.makedirs(IMAGE_FOLDER, exist_ok=True)

@app.route("/", methods=["GET","POST"])
def upload():

    if request.method == "POST":

        image = request.files["image"]

        image.save(
            os.path.join(
                IMAGE_FOLDER,
                image.filename
            )
        )

        return "Image Uploaded Successfully"

    return """
    <h2>Image Upload System</h2>

    <form method="POST"
          enctype="multipart/form-data">

        <input type="file" name="image">
        <input type="submit">

    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)