# program_04_resume_upload_project.py

from flask import Flask, request
import os

app = Flask(__name__)

RESUME_FOLDER = "resumes"
os.makedirs(RESUME_FOLDER, exist_ok=True)

@app.route("/", methods=["GET","POST"])
def resume_upload():

    if request.method == "POST":

        resume = request.files["resume"]

        resume.save(
            os.path.join(
                RESUME_FOLDER,
                resume.filename
            )
        )

        return "Resume Uploaded Successfully"

    return """
    <h2>Resume Upload Portal</h2>

    <form method="POST"
          enctype="multipart/form-data">

        Name:
        <input type="text" name="name"><br><br>

        Resume:
        <input type="file" name="resume"><br><br>

        <input type="submit">

    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)