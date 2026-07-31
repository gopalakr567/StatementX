import pdfplumber
from collections import defaultdict

def read_pdf_words(pdf_path):
    rows = defaultdict(list)

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            words = page.extract_words()

            for word in words:
                y = round(word["top"], 1)
                rows[(page.page_number, y)].append(word)

    result = []

    for key in sorted(rows.keys()):
        row = sorted(rows[key], key=lambda w: w["x0"])
        result.append(row)

    return result