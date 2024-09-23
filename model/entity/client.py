from model.entity.person import Person
from tools.validator import Validator


class Client(Person):
    def __init__(self, id, name, family, username, password):
        super().__init__(id, name, family)
        self.username = username
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = Validator.username_validator(username, "Invalid User name")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = Validator.password_validator(password, "Invalid Password")

    def __repr__(self):
        return f"{self.__dict__}"
