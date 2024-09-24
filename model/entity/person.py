from tools.validator import Validator


class Person:
    def __init__(self, id, name, family):
        self.id = id
        self.name = name
        self.family = family

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = Validator.id_validator(id, "Invalid Id")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = Validator.name_validator(name, "Invalid Name")

    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, family):
        self._family = Validator.family_validator(family, "Invalid Family")
