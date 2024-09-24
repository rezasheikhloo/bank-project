from model.da.transaction_da import TransactionDa
from model.entity import transaction


class TransactionBl:
    @staticmethod
    def save(person):
        Transaction_da = TransactionDa()
        return Transaction_da.save(transaction)