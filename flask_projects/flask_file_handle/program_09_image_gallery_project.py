# program_09_image_gallery_project.py

from flask import Flask
import os

app = Flask(__name__)

IMAGE_FOLDER = "gallery"

os.makedirs(IMAGE_FOLDER, exist_ok=True)

@app.route("/")
def gallery():

    images = os.listdir(IMAGE_FOLDER)

    html = "<h2>Image Gallery</h2>"

    for image in images:

        html += f"""
        <img src='/static/{image}'
             width='200'
             height='200'>
        """

    return html

if __name__ == "__main__":
    app.run(debug=True)