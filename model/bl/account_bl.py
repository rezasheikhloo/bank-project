from model.da.account_da import AccountDa

class AccountBl:
    @staticmethod
    def save(account):
        account_da = AccountDa
        return account_da.save(account)

    @staticmethod
    def edit(account):
        account_da = AccountDa
        return account_da.edit(account)

    @staticmethod
    def remove(account):
        account_da = AccountDa
        return account_da.remove(account)

    @staticmethod
    def find_all(account):
        account_da = AccountDa
        return account_da.find_all(account)

    @staticmethod
    def delete(account):
        account_da = AccountDa
        return account_da.delete(account)