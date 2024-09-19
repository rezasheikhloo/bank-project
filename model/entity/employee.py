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
	def job_title(self):
		return self._job_title

	@job_title.setter
	def job_title(self, job_title):
		#todo : Add Validator
		self._job_title = job_title

	def __repr__(self):
		return f"{self.__dict__}"
