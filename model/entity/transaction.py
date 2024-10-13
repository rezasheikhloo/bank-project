from tools.validator import Validator

class Transaction:
    def __init__(self, id,  status, amount, date_time, source_account, destination_account):
        self.id = id
        self.status = status
        self.amount = amount
        self.datetime = date_time
        self.source_account = source_account
        self.destination_account = destination_account

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = Validator.id_validator(id, "Invalid Id")


    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = Validator.status_validator(status, "Invalid Status")

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = Validator.amount_validator(amount, "Invalid Amount")

    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        self._date_time = Validator.date_time_validator(date_time, "Invalid datetime")

    @property
    def source_account(self):
        return self._source_account

    @source_account.setter
    def source_account(self, source_account):
        self._source_account = source_account

    @property
    def destination_account(self):
        return self._destination_account

    @destination_account.setter
    def destination_account(self, destination_account):
        self._destination_account = destination_account