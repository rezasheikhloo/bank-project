import mysql.connector

from model.entity.person import Person

class PersonDa:

    def connect(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", password="Root123@", database="mft")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()

    def save(self, Person):
        self.connect()
        from model.entity import person
        self.cursor.execute("INSERT INTO person_tbl (id,name,family) VALUES (%s,%s,%s)",
            [person.id, person.name, person.family])
        self.disconnect(commit=True)

    def edit(self, account):
        self.connect()
        self.cursor.execute("UPDATE account_tbl SET id=%s,client=%s,account_type=%s ,account_number=%s WHERE id=%s",
            [person.id, person.name, person.family])
        self.disconnect(commit=True)

    def remove(self, id):
        self.connect()
        self.cursor.execute("delete from person_tbl where id=%s", [id])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from person_tbl ")
        account_list = [Person(*person) for person in self.cursor.fetchall()]
        self.disconnect()
        if account_list:
            return account_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from person_tbl where id=%s", [id])
        account = self.cursor.fetchone()
        self.disconnect()
        if account:
            return Person(*person)
