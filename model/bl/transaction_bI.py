from model.da.transaction_da import TransactionDa

class TransactionBl:
    @staticmethod
    def save(transaction):
        transaction_da = TransactionDa()
        return transaction_da.save(transaction)

    @staticmethod
    def edit(transaction):
        transaction_da = TransactionDa()
        return transaction_da.edit(transaction)

    @staticmethod
    def remove(transaction):
        transaction_da = TransactionDa()
        return transaction_da.remove(transaction)

    @staticmethod
    def find_all(transaction):
        transaction_da = TransactionDa()
        return transaction_da.find_all(transaction)