from controller.person_da import TransactionDa
from model.entity.client import Transaction



class TransactionBl:
    @staticmethod
    def save(person):
        Transaction_da = TransactionDa()
        return Transaction_da.save(Transaction)