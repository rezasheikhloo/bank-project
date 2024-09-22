import mysql.connector

from client import Client

class ClientDa:

	def connect(self):
		self.connection = mysql.connector.connect(host="localhost", user="root", password="Root123@", database="mft")
		self.cursor = self.connection.cursor()

	def disconnect(self, commit=False):
		if commit:
			self.connection.commit()
		self.cursor.close()
		self.connection.close()

	def save(self, client):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("insert into client_tbl () values ()",[])
		self.disconnect(commit = True)

	def edit(self, client):
		self.connect()
		#todo : complete sql command and parameters
		self.cursor.execute("update client_tbl set    where id=%s",[])
		self.disconnect(commit = True)

	def remove(self, id):
		self.connect()
		self.cursor.execute("delete from client_tbl where id=%s",[id])
		self.disconnect(commit = True)

	def find_all(self):
		self.connect()
		self.cursor.execute("select * from client_tbl ")
		client_list = [Client(*client) for client in self.cursor.fetchall()]
		self.disconnect()
		if client_list:
			return client_list

	def find_by_id(self, id):
		self.connect()
		self.cursor.execute("select * from client_tbl where id=%s", [id])
		client = self.cursor.fetchone()
		self.disconnect()
		if client:
			return Client(*client)

