import re

date_pattern = re.compile(r"\d{2}\.\d{2}\.\d{4}")

def is_transaction(row):
    return (
        len(row) >= 4
        and row[0]["text"].isdigit()
        and date_pattern.fullmatch(row[1]["text"])
    )


def build_transactions(rows):

    transactions = []
    current = None
    pending_heading = ""

    # Text snippets to ignore in rows (page headers/footers etc.)
    IGNORE_TEXT = [
    "Dial your Bank",
    "Never share your OTP",
    "Transaction Remarks",
    "Date Amount",
    "Cheque Number",
    "www.icici.bank.in",
    "Page",
]

    for i, row in enumerate(rows):

        text = " ".join(word["text"] for word in row)
        # Ignore page headers and footers
        if any(x.lower() in text.lower() for x in IGNORE_TEXT):
            continue

        amounts = []
        for word in row:
            # Ignore S.No and Date columns
            if word["x0"] < 300:
                continue

            if word["text"].replace(".", "", 1).isdigit():
                amounts.append({
                    "value": word["text"],
                    "x": word["x0"]
                })

        if (
            any("." in word["text"] for word in row)
            and any(word["text"].isdigit() for word in row)
            and not is_transaction(row)
        ):
            print("NOT A TRANSACTION:", text)

        if is_transaction(row):
            # print(text)
            # print(amounts)
            # print("-" * 60)

            if current:
                transactions.append(current)

            withdrawal = ""
            deposit = ""
            balance = ""

            for amt in amounts:
                x = amt["x"]

                if x >= 525:
                    balance = amt["value"]
                elif x >= 470:
                    deposit = amt["value"]
                else:
                    withdrawal = amt["value"]

            current = {
                "sno": row[0]["text"],
                "date": row[1]["text"],
                "withdrawal": withdrawal,
                "deposit": deposit,
                "balance": balance,
                "heading": pending_heading,
                "narration": ""
            }

            pending_heading = ""

        else:

            if current is None:
                pending_heading = text
                continue

            first = row[0]["text"]

            # Look ahead to the next row
            next_is_transaction = False

            if i + 1 < len(rows):
                next_is_transaction = is_transaction(rows[i + 1])

            # If next row is a transaction, this row is the heading
            if (
                next_is_transaction
                and not first.startswith((
                    "UPI/",
                    "MMT/",
                    "INF/",
                    "ATD/",
                    "ACH/",
                    "RTGS/",
                    "NEFT/",
                    "POS/",
                    "NACH/"
                ))
            ):
                pending_heading = text
            else:
                if (
                    "transaction" in text.lower()
                    and "withdrawal" in text.lower()
                    and "deposit" in text.lower()
                ):
                    continue

                ignore = [
                    "Please call from your registered mobile number",
                    "Never share your OTP",
                    "Transaction Withdrawal Deposit Balance",
                    "Withdrawal Deposit Balance",
                    "S.No",
                    "Cheque Number",
                    "Transaction Remarks",
                    "Date Amount",
                    "www.icici.bank.in"
                ]

                if any(x.lower() in text.lower() for x in ignore):
                    print("IGNORED:", text)
                    continue

                if current["narration"]:
                    current["narration"] += " " + text
                else:
                    current["narration"] = text
    # Add the last transaction
    if current:
        transactions.append(current)

    return transactions