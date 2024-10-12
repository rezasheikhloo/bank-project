from model.entity.account import Account
from tools.decorators import exception_handling
class AccountController:
    @staticmethod
    @exception_handling
    def save(id, account_type, account_number, client):
        account = Account(0, account_type, account_number, client)
        Account.save(account)
        return True, f"Account Saved {account}"

    @staticmethod
    @exception_handling
    def edit(id, account_type, account_number, client):
        account = Account(0, account_type, account_number, client)
        Account.edit(account)
        return True, f"Account Saved {account}"

    @staticmethod
    @exception_handling
    def remove(id, account_type, account_number, client):
        account = Account(0, account_type, account_number, client)
        Account.remove(account)
        return True, f"Account Saved {account}"

    @staticmethod
    @exception_handling
    def find_all(cls):
        pass

    def delete(self, param):
        pass