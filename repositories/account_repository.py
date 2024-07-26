from models.account import Account

class AccountRepository:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account: Account):
        self.accounts[account.account_id] = account

    def get_account(self, account_id: int) -> Account:
        return self.accounts.get(account_id)

    def transfer_funds(self, from_account: Account, to_account: Account, amount: float):
        from_account.balance -= amount
        to_account.balance += amount
        from_account.transactions.append(f"Transferred {amount} to {to_account.account_id}")
        to_account.transactions.append(f"Received {amount} from {from_account.account_id}")

    def get_transactions(self, account_id: int):
        account = self.get_account(account_id)
        if account:
            return account.transactions
        return None

