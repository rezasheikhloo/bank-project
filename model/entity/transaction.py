class Transaction:
	def __init__(self, id, creation_date, status, amount):
		self.id = id
		self.creation_date = creation_date
		self.status = status
		self.amount = amount

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		#todo : Add Validator
		self._id = id

	@property
	def creation_date(self):
		return self._creation_date

	@creation_date.setter
	def creation_date(self, creation_date):
		#todo : Add Validator
		self._creation_date = creation_date

	@property
	def status(self):
		return self._status

	@status.setter
	def status(self, status):
		#todo : Add Validator
		self._status = status

	@property
	def amount(self):
		return self._amount

	@amount.setter
	def amount(self, amount):
		#todo : Add Validator
		self._amount = amount

	def __repr__(self):
		return f"{self.__dict__}"
