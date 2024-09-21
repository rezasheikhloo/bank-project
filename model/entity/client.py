from tools import validator
from tools.validator import Validator


class Client:
	def __init__(self, id, name, family, birth_date):
		self.id = id
		self.name = name
		self.family = family
		self.birth_date = birth_date

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = validator.id_validator(id, 'invalid id')

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = Validator.name_validator(name, "invalid name")

	@property
	def family(self):
		return self._family

	@family.setter
	def family(self, family):
		self._family = Validator.family_validator(family, "invalid family")

	@property
	def birth_date(self):
		return self._birth_date

	@birth_date.setter
	def birth_date(self, birth_date):
		self._birth_date = validator.birth_date_validator(birth_date, "invalid birth_date")

	def __repr__(self):
		return f"{self.__dict__}"
