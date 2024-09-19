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
		#todo : Add Validator
		self._id = id

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		#todo : Add Validator
		self._name = name

	@property
	def family(self):
		return self._family

	@family.setter
	def family(self, family):
		#todo : Add Validator
		self._family = family

	@property
	def birth_date(self):
		return self._birth_date

	@birth_date.setter
	def birth_date(self, birth_date):
		#todo : Add Validator
		self._birth_date = birth_date

	def __repr__(self):
		return f"{self.__dict__}"
