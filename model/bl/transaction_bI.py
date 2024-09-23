

class TransactionBl:
    @staticmethod
    def save(person):
        Transaction_da = TransactionDa()
        return Transaction_da.save(Transaction)