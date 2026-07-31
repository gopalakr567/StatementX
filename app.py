from flask import Flask, render_template, request, send_file  # type: ignore[import]
import os

from main import extract_statement

# correct module name usage
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/extract", methods=["POST"])
def extract():

    pdf = request.files["pdf"]

    pdf_path = os.path.join(UPLOAD_FOLDER, pdf.filename)
    pdf.save(pdf_path)

    excel_path = os.path.join(OUTPUT_FOLDER, "transactions.xlsx")

    extract_statement(pdf_path, excel_path)

    return send_file(
        excel_path,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)