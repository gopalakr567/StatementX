from parser.pdf_reader import read_pdf_words
from parser.row_builder import build_transactions
from parser.excel_writer import write_excel

def extract_statement(pdf_path, excel_path):
    rows = read_pdf_words(pdf_path)

    transactions = build_transactions(rows)

    print(f"Transactions Found: {len(transactions)}")

    if transactions:
        print("First :", transactions[0]["sno"], transactions[0]["date"])
        print("Last  :", transactions[-1]["sno"], transactions[-1]["date"])

    write_excel(transactions, excel_path)

    return len(transactions)


if __name__ == "__main__":
    count = extract_statement(
        "sample/statement.pdf",
        "output/transactions.xlsx"
    )

    print("Excel file created successfully.")