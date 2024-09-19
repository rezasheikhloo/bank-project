class Account:
	def __init__(self, id, name, account_type, account_number):
		self.id = id
		self.name = name
		self.account_type = account_type
		self.account_number = account_number

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
	def account_type(self):
		return self._account_type

	@account_type.setter
	def account_type(self, account_type):
		#todo : Add Validator
		self._account_type = account_type

	@property
	def account_number(self):
		return self._account_number

	@account_number.setter
	def account_number(self, account_number):
		#todo : Add Validator
		self._account_number = account_number

	def __repr__(self):
		return f"{self.__dict__}"
