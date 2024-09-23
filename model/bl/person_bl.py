from tools.person_da import PersonDa


class PersonBl:
    @staticmethod
    def save(person):
        person_da = PersonDa()
        return person_da.save(person)