import datetime
from commponent import *
import tkinter.ttk as ttk
from controller.transaction_controller import TransactionController
from controller.account_controller import AccountController
from controller.client_controller import ClientController

class SignInView:
    def __init__(self):
        self.win = Tk()
        self.win.title("Sign In")
        self.win.resizable(False, False)
        self.win.geometry("400x400")

        self.name = EntryWithLabel(self.win, "Name : ", 10, 5, 140, "str")
        self.family = EntryWithLabel(self.win, "Family : ", 10, 45, 140, "str")
        self.username = EntryWithLabel(self.win, "username : ", 10, 85, 140, "str")
        self.password = EntryWithLabel(self.win, "Password : ", 10, 125, 140, "str")

        Label(self.win, text="Which One Are You : ").place(x=10, y=205)

        Button(self.win, text="Sign In", width=10, command=self.SignIn_click).place(x=195, y=350)

        self.win.mainloop()

    def SignIn_click(self):
        def Do_Button():
            for i in table.get_children():
                table.delete(i)

            TransactionController().save(self.status.get(), self.amount.get(), self.date_time.get(),self.source_account.get(), self.destination_account.get())
            for i in TransactionController.find_all():
                table.insert("", END, values=i)

            for i in table_person.get_children():
                table_person.delete(i)
            ClientController().save(self.name.get(), self.family.get(), self.username.get(), self.password.get())

            for i in ClientController().find_all():
                table_person.insert("", END, values=i)

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
                TransactionController().edit(self.id.get(), self.status.get(), self.amount.get(), self.date_time.get(),self.source_account.get(), self.destination_account.get())

                for i in TransactionController().find_all():
                    table.insert("", END, values=i)

            def Edit_Client():
                for i in table_person.get_children():
                    table_person.delete(i)

            ClientController().edit(self.id.get(), self.client_name.get(), self.client_family.get(),
                                    self.client_username.get(), self.client_password.get())
            for i in ClientController().find_all():
                table_person.insert("", END, values=i)

        def Edit_Account():
            for i in table_sec.get_children():
                table_sec.delete(i)
            AccountController().edit(self.id.get(), self.account_type.get(), self.account_number.get(), self.client.get())

            for i in AccountController().find_all():
                table_sec.insert("", END, values=i)

        def table_person_refresher():
            for i in table_person.get_children():
                table_person.delete(i)

            for i in ClientController.find_all():
                table_person.insert("", END, values=i)
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

        status, client = ClientController().save(self.name.get(), self.family.get(), self.username.get(), self.password.get())
        if status:
         print(status)
        self.win.destroy()
        self.window = Tk()
        self.window.title("transaction")
        self.window.geometry("1000x1000")

        self.client_name = EntryWithLabel(self.window, "Person Name : ", 10, 205, 120, "str")
        self.client_family = EntryWithLabel(self.window, "Person Family : ", 10, 245, 120, "str")
        self.client_username = EntryWithLabel(self.window, "Person username : ", 10, 285, 120, "str")
        self.client_password = EntryWithLabel(self.window, "Person password : ", 10, 325, 120, "str")


        table = ttk.Treeview(self.window, height=20, columns=(1, 2, 3, 4, 5, 6), show="headings")
        table_person = ttk.Treeview(self.window, height=28, columns=(1, 2, 3, 4, 5, 6), show="headings")



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