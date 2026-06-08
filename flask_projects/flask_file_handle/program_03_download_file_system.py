# program_03_download_file_system.py

from flask import Flask, send_from_directory
import os

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():

    return """
    <h2>Download File</h2>

    <a href="/download/sample.txt">
        Download Sample File
    </a>
    """

@app.route("/download/<filename>")
def download(filename):

    return send_from_directory(
        DOWNLOAD_FOLDER,
        filename,
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)