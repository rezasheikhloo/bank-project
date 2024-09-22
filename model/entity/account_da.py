import mysql.connector

from account import Account


class AccountDa:

    def connect(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", password="Root123@", database="mft")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, account):
        self.connect()
        self.cursor.execute("INSERT INTO account_tbl (username,password,id,name,account_type,account_number) VALUES (%s,%s,%s,%s,%s)",
            [account.username, account.password, account.id, account.name, account.account_type, account.account_number])
        self.disconnect(commit=True)

    def edit(self, account):
        self.connect()
        self.cursor.execute("UPDATE account_tbl SET password=%s,id=%s,name=%s,account_type=%s ,account_number=%s WHERE username=%s",
            [account.password, account.id, account.name, account.account_type, account.account_number, account.username])
        self.disconnect(commit=True)

    def remove(self, id):
        self.connect()
        self.cursor.execute("delete from account_tbl where id=%s", [id])
        self.disconnect(commit=True)

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
