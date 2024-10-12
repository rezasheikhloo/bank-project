import re
from datetime import datetime


class Validator:
    @classmethod
    def id_validator(cls, id, message):
        if type(id) == int and id >= 0:
            return id
        else:
            raise ValueError(message)

    @classmethod
    def name_validator(cls, name, message):
        if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,30}$", name):
            return name
        else:
            raise ValueError(message)

    @classmethod
    def family_validator(cls, family, message):
        if isinstance(family, str) and re.match(r"^[a-zA-Z\s]{2,30}$", family):
            return family
        else:
            raise ValueError(message)

    @classmethod
    def username_validator(cls, username, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,30}$", username):
            return username
        else:
            raise ValueError(message)

    @classmethod
    def password_validator(cls, password, message):
        if re.match(r"^[\w@!#$%^&*\s]{2,16}$", password):
            return password
        else:
            raise ValueError(message)

    @classmethod
    def account_number_validator(cls, account_number, message):
        if re.match(r"^[0-9]{16}$", account_number):
            return account_number
        else:
            raise ValueError(message)

    @classmethod
    def amount_validator(cls, amount, message):
        if type(amount) == int and amount > 0:
            return amount
        else:
            raise ValueError(message)

    @classmethod
    def account_type_validator(cls, account_type, message):
        if re.match(r"^[a-zA-Z\s]{2,30}$", account_type):
            return account_type
        else:
            raise ValueError(message)

    @classmethod
    def status_validator(cls, status, message):
        if isinstance(status, str) and re.match(r"^[a-zA-Z\s]{2,30}$", status):
            return status
        else:
            raise ValueError(message)

    @classmethod
    def source_account_validator(cls,source_account, message):
        if isinstance(source_account, str) and re.match(r"^[a-zA-Z\s]{2,30}$", source_account):
            return source_account
        else:
            raise ValueError(message)

    @classmethod
    def destination_account_validator(cls, destination_account, message):
        if isinstance(destination_account, str) and re.match(r"^[a-zA-Z\s]{2,30}$", destination_account):
            return destination_account
        else:
            raise ValueError(message)

    @classmethod
    def date_time_validator(cls, date_time, message):
        if isinstance(date_time, datetime):
            return date_time
        elif isinstance(date_time, str):
            try:
                return datetime.strptime(date_time, '%Y-%m-%d %H:%M')
            except:
                raise ValueError(message)
        else:
            ValueError(message)