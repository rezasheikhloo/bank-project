import mysql.connector
from model.entity.transaction import Transaction

class TransactionDa:

    def connect(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", password="Root123@", database="mft")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, transaction):
        self.connect()
        self.cursor.execute(
           "INSERT INTO transaction_tbl (id,status,amount,date_time,source_account,destination_account) VALUES (%s,%s,%s,%s,%s,%s)",
            [transaction.id, transaction.status, transaction.amount, transaction.date_time, transaction.source_account,
             transaction.destination_account])
        self.disconnect(commit=True)

    def edit(self, transaction):
        self.connect()
        self.cursor.execute(
            "UPDATE transaction_tbl SET id=%s,status=%s,amount=%s,date_time=%s,source_account=%s ,destination_account=%s WHERE id=%s",
            [transaction.id, transaction.date_time, transaction.status, transaction.amount, transaction.source_account,
             transaction.destination_account])
        self.disconnect(commit=True)

    def remove(self, id):
        self.connect()
        self.cursor.execute("delete from transaction_tbl where id=%s", [id])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from transaction_tbl ")
        transaction_list = [Transaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        if transaction_list:
            return transaction_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from transaction_tbl where id=%s", [id])
        transaction = self.cursor.fetchone()
        self.disconnect()
        if transaction:
            return Transaction(*transaction)
