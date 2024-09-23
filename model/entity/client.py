from model.entity.person import Person


class Client(Person):
    def __init__(self, id, name, family):
        super().__init__(id, name, family)


    def __repr__(self):
        return f"{self.__dict__}"
