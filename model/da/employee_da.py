import mysql.connector

from employee import Employee


class EmployeeDa:

    def connect(self):
        self.connection = mysql.connector.connect(host="localhost", user="root", password="Root123@", database="mft")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, employee):
        self.connect()
        self.cursor.execute("INSERT INTO employee_tbl (username,password,id,name,family,job_title) VALUES (%s,%s,%s,%s,%s)",
            [employee.username, employee.password, employee.id, employee.name, employee.family,
             employee.job_title])
        self.disconnect(commit=True)

    def edit(self, employee):
        self.connect()
        self.cursor.execute("UPDATE employee_tbl SET password=%s,id=%s,name=%s,family=%s ,job_title=%s WHERE username=%s",
            [employee.password, employee.id, employee.name, employee.family, employee.job_title,
             employee.username])
        self.disconnect(commit=True)

    def remove(self, id):
        self.connect()
        self.cursor.execute("delete from employee_tbl where id=%s", [id])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from employee_tbl ")
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        if employee_list:
            return employee_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute("select * from employee_tbl where id=%s", [id])
        employee = self.cursor.fetchone()
        self.disconnect()
        if employee:
            return Employee(*employee)
