from model.entity.transaction import Transaction
from tools.decorators import exception_handling


class TransactionController:
    @staticmethod
    @exception_handling
    def save( status, amount, datetime, source_account, destination_account):
        transaction = Transaction(0, status, amount, datetime, source_account, destination_account)
        Transaction.save(transaction)
        return True, f"Transaction Saved {transaction}"
