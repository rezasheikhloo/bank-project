from controller.person_bl import PersonBl
from model.entity.client import Person
from tools.decorators import exception_handling


class PersonController:
    @staticmethod
    @exception_handling
    def save(name, family, status=True):
        person = Person(None, name, family, status)
        return True, PersonBl.save(person)