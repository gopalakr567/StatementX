def get_column(word):
    x = word["x0"]

    if x < 70:
        return "sno"

    elif x < 140:
        return "date"

    elif x < 320:
        return "remarks"

    elif x < 420:
        return "withdrawal"

    elif x < 520:
        return "deposit"

    else:
        return "balance"