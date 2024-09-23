from tools.validator import Validator


class Account:
    def __init__(self, id, account_type, account_number, client):
        self.id = id
        self.account_type = account_type
        self.account_number = account_number
        self.client = client

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = Validator.id_validator(id, 'invalid id')

    @property
    def account_type(self):
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        self._account_type = Validator.account_type_validator(account_type, "Invalid Account Type")

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        self._account_number = Validator.account_number_validator(account_number, "invalid number")

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, client):
        self._client = client

    def __repr__(self):
        return f"{self.__dict__}"
