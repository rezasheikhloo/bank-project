from model.bl.transaction_bI import TransactionBl
from tools.decorators import exception_handling
from model.entity.transaction import Transaction

class TransactionController:
    @staticmethod
    @exception_handling
    def save(status, amount, date_time, source_account, destination_account):
        transaction = Transaction(0, status, amount, date_time, source_account, destination_account)
        TransactionBl.save(transaction)
        return True, f"Transaction Saved {transaction}"

    @staticmethod
    @exception_handling
    def edit(status, amount, date_time, source_account, destination_account):
        transaction = Transaction(0, status, amount, date_time, source_account, destination_account)
        TransactionBl.edit(transaction)
        return True, f"Transaction edited {transaction}"

    @staticmethod
    @exception_handling
    def remove(status, amount, date_time, source_account, destination_account):
        transaction = Transaction(0, status, amount, date_time, source_account, destination_account)
        TransactionBl.remove(transaction)
        return True, f"Transaction removed {transaction}"

    @staticmethod
    @exception_handling
    def find_all(status, amount, date_time, source_account, destination_account):
        transaction = Transaction(0, status, amount, date_time, source_account, destination_account)
        TransactionBl.find_all(transaction)
        return True, f"Transaction find_all {transaction}"

    def delete(self, param, param1, param2, param3, param4, param5):
        pass