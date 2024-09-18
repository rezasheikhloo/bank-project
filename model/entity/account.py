from model.entity.client import Client
from tools import validator
from tools.validator import Validator


class Account:
    def __init__(self, id, name,account_type, account_number):
        self.id = id
        self.name = name
        self.account_type = account_type
        self.account_number = account_number


    @property
    def id(self):
        return self._id


    @id.setter
    def id(self, id):
        self._id = validator.id_validator(id, 'invalid id')


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name):
        self._name = Validator.name_validator(name, "invalid name")


    @property
    def account_type(self):
        return self._account_type


    @account_type.setter
    def account_type(self, account_type):
        self._account_type = Validator.family_validator(account_type, "invalid account_type")


    @property
    def account_number(self):
        return self._account_number


    @account_number.setter
    def account_number(self, account_number):
        self._account_number = Validator.account_number_validator(account_number, "invalid number")
