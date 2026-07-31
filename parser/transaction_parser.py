from parser.transaction import Transaction
from parser.line_classifier import classify

def parse_transactions(lines):

    transactions = []

    current = None

    for line in lines:

        line_type = classify(line)

        if line_type == "TRANSACTION":

            if current:
                transactions.append(current)

            current = Transaction()
            current.transaction = line

        elif current:

            if line_type == "NARRATION":
                current.narration += " " + line

            else:
                current.heading += " " + line

    if current:
        transactions.append(current)

    return transactions