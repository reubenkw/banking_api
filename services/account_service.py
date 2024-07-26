from repositories.account_repository import AccountRepository
from models.account import Account
from dtos.account_dto import CreateAccountDTO, TransferFundsDTO

class AccountService:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def create_account(self, account_data: CreateAccountDTO):
        account = Account(account_data.account_id, account_data.initial_balance)
        self.account_repository.create_account(account)

    def transfer_funds(self, transfer_data: TransferFundsDTO):
        from_account = self.account_repository.get_account(transfer_data.from_account_id)
        to_account = self.account_repository.get_account(transfer_data.to_account_id)
        if not from_account or not to_account:
            raise ValueError("Invalid account IDs")
        if from_account.balance < transfer_data.amount:
            raise ValueError("Insufficient funds")
        self.account_repository.transfer_funds(from_account, to_account, transfer_data.amount)

    def get_transactions(self, account_id: int):
        return self.account_repository.get_transactions(account_id)

