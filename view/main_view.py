from commponent import *
import tkinter.ttk as ttk
from controller.transaction_controller import TransactionController
from controller.account_controller import AccountController
from controller.client_controller import ClientController
import datetime

class SignInView:
    def __init__(self):
        self.win = Tk()
        self.win.title("Sign In")
        self.win.resizable(False, False)
        self.win.geometry("400x250")

        self.name = EntryWithLabel(self.win, "Name : ", 10, 15, 140, "str")
        self.family = EntryWithLabel(self.win, "Family : ", 10, 55, 140, "str")
        self.username = EntryWithLabel(self.win, "username : ", 10, 95, 140, "str")
        self.password = EntryWithLabel(self.win, "Password : ", 10, 135, 140, "str")

        Button(self.win, text="Sign In", width=10, command=self.SignIn_click).place(x=165, y=200)

        self.win.mainloop()

    def SignIn_click(self):
        def save_Button():
            for i in table.get_children():
                table.delete(i)

            TransactionController().save(self.status.get(), self.amount.get(), self.date_time.get(),
                                         self.source_account.get(), self.destination_account.get())
            for i in TransactionController.find_all():
                table.insert("", END, values=i)

            for i in table_client.get_children():
                table_client.delete(i)
            ClientController().save(self.name.get(), self.family.get(), self.username.get(), self.password.get())

            for i in ClientController().find_all(self.name.get(), self.family.get(), self.username.get(), self.password.get()):
                table_client.insert("", END, values=i)

            for i in table_sec.get_children():
                table_sec.delete(i)
            AccountController().save(self.account_type.get(), self.account_number.get(), self.client.get())

            for i in AccountController().find_all():
                table_sec.insert("", END, values=i)

        def Remove_Button():
            for i in table.get_children():
                table.delete(i)
            TransactionController().delete(self.id.get())
            for i in TransactionController.find_all():
                table.insert("", END, values=i)

            for i in table_sec.get_children():
                table_sec.delete(i)
            AccountController().delete(self.id.get())

            for i in AccountController().find_all():
                table_sec.insert("", END, values=i)

        def Find_All_Button():
            for i in table.get_children():
                table.delete(i)

            for i in TransactionController().find_all():
                table.insert("", END, values=i)

        def Edit_Transaction():
            for i in table.get_children():
                table.delete(i)
            TransactionController().edit(self.id.get(), self.status.get(), self.amount.get(), self.date_time.get(),
                                         self.source_account.get(), self.destination_account.get())

            for i in TransactionController().find_all():
                table.insert("", END, values=i)

        def table_person_refresher():
            for i in table_client.get_children():
                table_client.delete(i)

            for i in ClientController.find_all():
                table_client.insert("", END, values=i)

        def table_sec_refresher():
            for i in table_sec.get_children():
                table_sec.delete(i)

            for i in AccountController().find_all():
                table_sec.insert("", END, values=i)

        def table_refresher_usuall():
            for i in table.get_children():
                table.delete(i)
            for i in TransactionController.find_all():
                table.insert("", END, values=i)

        status, client = ClientController().save(self.name.get(), self.family.get(), self.username.get(),
                                                 self.password.get())
        if status:
            print(status)
        self.win.destroy()
        self.window = Tk()
        self.window.title("transaction")
        self.window.geometry("900x700")

        self.id = EntryWithLabel(self.window, "Client Id : ", 10, 25, 120, "int")
        self.status = EntryWithLabel(self.window, "Transaction Status : ", 10, 65, 120, "str")
        self.amount = EntryWithLabel(self.window, "Transaction Amount : ", 10,105, 120, "float")
        self.date_time = EntryWithLabel(self.window, "Transaction DateTime : ", 10, 145, 120,"str")
        self.source_account = EntryWithLabel(self.window, "Source_account : ", 10, 185, 120, "str")
        self.destination_account = EntryWithLabel(self.window, "destination_account : ", 10, 225, 120, "str")
        self.client_name = EntryWithLabel(self.window, "Client Name : ", 10, 265, 120, "str")
        self.client_family = EntryWithLabel(self.window, "Client Family : ", 10, 305, 120, "str")
        self.client_username = EntryWithLabel(self.window, "Client Username : ", 10, 345, 120, "str")
        self.client_password = EntryWithLabel(self.window, "Client Password : ", 10, 385, 120, "str")
        self.account_type = EntryWithLabel(self.window, "Account Type : ", 10, 425, 120, "str")
        self.account_number = EntryWithLabel(self.window, "Account_number : ", 10, 465, 120, "int")

        Button(self.window, text="Save", command=save_Button).place(x=10, y=500)

        Button(self.window, text="Remove", command=Remove_Button).place(x=60, y=500)

        Button(self.window, text="Find All Transaction", command=Find_All_Button).place(x=110, y=550)

        Button(self.window, text="Edit Transaction", command=Edit_Transaction).place(x=10, y=550)


        table = ttk.Treeview(self.window, height=25, columns=(1, 2, 3, 4, 5, 6), show="headings")
        table.heading(1, text="Id")
        table.heading(2, text="Name")
        table.heading(3, text="Family")
        table.heading(4, text="Status")
        table.heading(5, text="Amount")
        table.heading(6, text="Account Number")

        table.column(1, width=70)
        table.column(2, width=80)
        table.column(3, width=80)
        table.column(4, width=80)
        table.column(5, width=90)
        table.column(6, width=80)

        table.place(x=265, y=25)

        table_refresher_usuall()

        table_client = ttk.Treeview(self.window, height=28, columns=(1, 2, 3, 4, 5, 6), show="headings")

        table_sec = ttk.Treeview(self.window, height=28, columns=(1, 2, 3, 4, 5, 6), show="headings")
        table_sec.heading(1, text="Id")
        table_sec.heading(2, text="Person Name")
        table_sec.heading(3, text="Book Name")
        table_sec.heading(4, text="Borrow Date Time")
        table_sec.heading(5, text="Return Date Time")
        table_sec.heading(6, text="Amount")

        table_sec.column(1, width=70)
        table_sec.column(2, width=100)
        table_sec.column(3, width=100)
        table_sec.column(4, width=100)
        table_sec.column(5, width=100)
        table_sec.column(6, width=80)

        table_sec.place(x=1350, y=5)


sgn = SignInView()
