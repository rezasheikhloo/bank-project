from model.bl.account_bl import AccountBl
from model.entity.account import Account
from tools.decorators import exception_handling

class AccountController:
    @staticmethod
    @exception_handling
    def save(id, account_type, account_number, client):
        account = Account(0, account_type, account_number, client)
        AccountBl.save(account)
        return True, f"Account Saved {account}"

    @staticmethod
    @exception_handling
    def edit(id, account_type, account_number, client):
        account = Account(0, account_type, account_number, client)
        AccountBl.edit(account)
        return True, f"Account Saved {account}"

    @staticmethod
    @exception_handling
    def remove(id, account_type, account_number, client):
        account = Account(0, account_type, account_number, client)
        AccountBl.remove(account)
        return True, f"Account Saved {account}"

    @staticmethod
    @exception_handling
    def find_all(id, account_type, account_number, client):
        account = Account(0, account_type, account_number, client)
        AccountBl.find_all(account)
        return True, f"Account find_all {account}"