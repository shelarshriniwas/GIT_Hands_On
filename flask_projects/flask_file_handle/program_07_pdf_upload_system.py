# program_07_pdf_upload_system.py

from flask import Flask, request
import os

app = Flask(__name__)

PDF_FOLDER = "pdfs"
os.makedirs(PDF_FOLDER, exist_ok=True)

@app.route("/", methods=["GET","POST"])
def upload_pdf():

    if request.method == "POST":

        pdf = request.files["pdf"]

        if pdf.filename.endswith(".pdf"):

            pdf.save(
                os.path.join(
                    PDF_FOLDER,
                    pdf.filename
                )
            )

            return "PDF Uploaded"

        return "Only PDF Allowed"

    return """
    <h2>PDF Upload System</h2>

    <form method="POST"
          enctype="multipart/form-data">

        <input type="file" name="pdf">

        <input type="submit">

    </form>
    """

if __name__ == "__main__":
    app.run(debug=True)