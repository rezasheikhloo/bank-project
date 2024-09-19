from tools import validator
from tools.validator import Validator


class Transaction:
    def __init__(self, id, creation_date, status, amount):
        self.id = id
        self.creation_date = creation_date
        self.status = status
        self.amount = amount

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = validator.id_validator(id, 'invalid id')

    @property
    def creation_date(self):
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        self._creation_date = Validator.creation_date_validator(creation_date, "invalid name")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = Validator.status_validator(status, "invalid fstatus")

    @property
    def amount(self, amount):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = validator.amount_validator(amount, "invalid amount")