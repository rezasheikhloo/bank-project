import re
from datetime import datetime,date


class Validator:
    @classmethod
    def id_validator(cls, id, message):
        if re.match(r"^[0-9]{1,10}$", id):
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
        if re.match(r"^[0-9]{16}$", amount):
            return amount
        else:
            raise ValueError(message)

    @classmethod
    def account_type_validator(cls, account_type, message):
        if re.match(r"^[a-zA-Z\s]{2,30}$", account_type):
            return account_type
        else:
            raise ValueError(message)