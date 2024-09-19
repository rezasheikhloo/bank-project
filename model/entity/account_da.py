import mysql.connector

from account import Account

class AccountDa:

	def connect(self):
		self.connection = mysql.connector.connect(host="localhost", user="root", password="root123", database="mft")
		self.cursor = self.connection.cursor()

	def disconnect(self, commit=False):
		if commit:
			self.connection.commit()
		self.cursor.close()
		self.connection.close()

	def save(self, account):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("insert into account_tbl () values ()",[])
		self.disconnect(commit = True)

	def edit(self, account):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("update account_tbl set    where id=%s",[])
		self.disconnect(commit = True)

	def remove(self, id):
		self.connect()
		self.cursor.execute("delete from account_tbl where id=%s",[id])
		self.disconnect(commit = True)

	def find_all(self):
		self.connect()
		self.cursor.execute("select * from account_tbl ")
		account_list = [Account(*account) for account in self.cursor.fetchall()]
		self.disconnect()
		if account_list:
			return account_list

	def find_by_id(self, id):
		self.connect()
		self.cursor.execute("select * from account_tbl where id=%s", [id])
		account = self.cursor.fetchone()
		self.disconnect()
		if account:
			return Account(*account)

