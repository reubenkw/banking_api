class Account:
    def __init__(self, account_id: int, balance: float):
        self.account_id = account_id
        self.balance = balance
        self.transactions = []

