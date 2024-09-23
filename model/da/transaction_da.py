import mysql.connector

from transaction import Transaction


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
            "INSERT INTO transaction_tbl (username,password,id,creation_date,status,amount) VALUES (%s,%s,%s,%s,%s)",
            [transaction.username, transaction.password, transaction.id, transaction.creation_date, transaction.status,
             transaction.amount])
        self.disconnect(commit=True)

    def edit(self, transaction):
        self.connect()
        self.cursor.execute(
            "UPDATE transaction_tbl SET password=%s,id=%s,creation_date=%s,status=%s ,amount=%s WHERE username=%s",
            [transaction.password, transaction.id, transaction.creation_date, transaction.status, transaction.amount,
             transaction.username])
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
