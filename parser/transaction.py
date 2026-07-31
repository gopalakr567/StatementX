class Transaction:

    def __init__(self):
        self.heading = ""
        self.transaction = ""
        self.narration = ""

    def __str__(self):
        return (
            f"Heading: {self.heading}\n"
            f"Transaction: {self.transaction}\n"
            f"Narration: {self.narration}\n"
        )