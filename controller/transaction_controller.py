from tools.decorators import exception_handling
from model.entity.transaction import Transaction

class TransactionController:
    @staticmethod
    @exception_handling
    def save(status, amount, date_time, source_account, destination_account):
        transaction = Transaction(0, status, amount, date_time, source_account, destination_account)
        Transaction.save(transaction)
        return True, f"Transaction Saved {transaction}"

    @staticmethod
    @exception_handling
    def edit(status, amount, date_time, source_account, destination_account):
        transaction = Transaction(0, status, amount, date_time, source_account, destination_account)
        Transaction.edit(transaction)
        return True, f"Transaction edited {transaction}"

    @staticmethod
    @exception_handling
    def remove(status, amount, date_time, source_account, destination_account):
        transaction = Transaction(0, status, amount, date_time, source_account, destination_account)
        Transaction.remove(transaction)
        return True, f"Transaction removed {transaction}"

    @staticmethod
    @exception_handling
    def find_all(cls):
        pass