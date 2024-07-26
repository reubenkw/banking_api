from pydantic import BaseModel, Field

class CreateAccountDTO(BaseModel):
    account_id: int = Field(..., example=1)
    initial_balance: float = Field(..., example=100.0)

class TransferFundsDTO(BaseModel):
    from_account_id: int = Field(..., example=1)
    to_account_id: int = Field(..., example=2)
    amount: float = Field(..., example=50.0)

