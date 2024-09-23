from model.entity.person import Person
from tools.validator import Validator


class Client(Person):
    def __init__(self, id, name, family, account_number):
        super().__init__(id, name, family)
        self.account_number = account_number

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        self._account_number = Validator.account_number_validator(account_number, "invalid number")
