from tools import validator
from tools.validator import Validator


class Employee:
	def __init__(self, id, name, family, job_title):
		self.id = id
		self.name = name
		self.family = family
		self.job_title = job_title

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id =  validator.id_validator(id, 'invalid id')

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
	def job_title(self):
		return self._job_title

	@job_title.setter
	def job_title(self, job_title):
		self._job_title = Validator.job_title_validator(job_title, "invalid job_title")

	def __repr__(self):
		return f"{self.__dict__}"
