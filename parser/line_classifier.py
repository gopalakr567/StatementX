import re

transaction_pattern = re.compile(
    r"^\d+\s+\d{2}\.\d{2}\.\d{4}\s+[\d,]+\.\d{2}\s+[\d,]+\.\d{2}$"
)

def classify(line):
    if transaction_pattern.match(line):
        return "TRANSACTION"

    prefixes = (
        "UPI/",
        "MMT/",
        "INF/",
        "ATD/",
        "BIL/",
        "ACH/",
        "NEFT/",
        "RTGS/",
        "IMPS/",
        "POS/",
        "NACH/",
    )

    if line.startswith(prefixes):
        return "NARRATION"

    return "HEADING"