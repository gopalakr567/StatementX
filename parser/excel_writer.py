from openpyxl import Workbook
from openpyxl.styles import Alignment

def write_excel(transactions, filename):

    wb = Workbook()
    ws = wb.active
    ws.title = "Transactions"

    ws.append([
        "S.No",
        "Date",
        "Heading",
        "Narration",
        "Withdrawal",
        "Deposit",
        "Balance"
    ])

    for t in transactions:
        ws.append([
            t["sno"],
            t["date"],
            t["heading"],
            t["narration"],
            t["withdrawal"],
            t["deposit"],
            t["balance"]
        ])

    ws.column_dimensions["A"].width = 8
    ws.column_dimensions["B"].width = 14
    ws.column_dimensions["C"].width = 25
    ws.column_dimensions["D"].width = 80
    ws.column_dimensions["E"].width = 15
    ws.column_dimensions["F"].width = 15
    ws.column_dimensions["G"].width = 15

    wb.save(filename)