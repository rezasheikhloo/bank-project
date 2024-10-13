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
        self.win.geometry("400x250")

        self.name = EntryWithLabel(self.win, "Name : ", 10, 15, 140, "str")
        self.family = EntryWithLabel(self.win, "Family : ", 10, 55, 140, "str")
        self.username = EntryWithLabel(self.win, "username : ", 10, 95, 140, "str")
        self.password = EntryWithLabel(self.win, "Password : ", 10, 135, 140, "str")

        Button(self.win, text="Log In", width=10, command=self.SignIn_click).place(x=165, y=200)

        self.win.mainloop()

    def SignIn_click(self):
        def save_Button():
            for i in table.get_children():
                table.delete(i)

            TransactionController().save(self.status.get(), self.amount.get(), self.date_time.get(),
                                         self.source_account.get(), self.destination_account.get())
            for i in TransactionController.find_all():
                table.insert("", END, values=i)

            for i in table.get_children():
                table.delete(i)
            ClientController().save(self.name.get(), self.family.get(), self.username.get(), self.password.get())

            for i in ClientController().find_all(self.name.get(), self.family.get(), self.username.get(),
                                                 self.password.get()):
                table.insert("", END, values=i)

            for i in table.get_children():
                table.delete(i)
            AccountController().save(self.id.get(), self.account_type.get(), self.account_number.get(),
                                     self.name.get())

            for i in AccountController().find_all():
                table.insert("", END, values=i)

        def Remove_Button():
            for i in table.get_children():
                table.delete(i)
            TransactionController().delete(self.id.get(), self.status.get(), self.amount.get(), self.date_time.get(),
                                           self.source_account.get(), self.destination_account.get())
            for i in TransactionController.find_all():
                table.insert("", END, values=i)

            for i in table.get_children():
                table.delete(i)
            AccountController().remove(self.id.get(), self.account_type.get(), self.account_number.get(),
                                       self.name.get())

            for i in AccountController().find_all():
                table.insert("", END, values=i)

        def Find_All_Button():
            for i in table.get_children():
                table.delete(i)

            for i in TransactionController().find_all():
                table.insert("", END, values=i)

        def Edit_Button():
            for i in table.get_children():
                table.delete(i)
            TransactionController().edit(self.id.get(), self.status.get(), self.amount.get(), self.date_time.get(),
                                         self.source_account.get(), self.destination_account.get())

            for i in TransactionController().find_all():
                table.insert("", END, values=i)

            for i in table.get_children():
                table.delete(i)
            ClientController().edit(self.name.get(), self.family.get(), self.username.get(), self.password.get())

            for i in ClientController().find_all(self.name.get(), self.family.get(), self.username.get(),
                                                 self.password.get()):
                table.insert("", END, values=i)

            for i in table.get_children():
                table.delete(i)
            AccountController().edit(self.id.get(), self.account_type.get(), self.account_number.get(),
                                     self.name.get())

            for i in AccountController().find_all():
                table.insert("", END, values=i)
        def table_transaction_refresher():
            for i in table.get_children():
                table.delete(i)

            for i in ClientController.find_all(self.name.get(), self.family.get(), self.username.get(),
                                               self.password.get()):
                table.insert("", END, values=i)


        status, client = ClientController().save(self.name.get(), self.family.get(), self.username.get(),
                                                 self.password.get())
        if status:
            print(status)
        self.win.destroy()
        self.window = Tk()
        self.window.title("transaction")
        self.window.geometry("1070x650")

        self.id = EntryWithLabel(self.window, "Client Id : ", 10, 25, 120, "int")
        self.status = EntryWithLabel(self.window, "Transaction Status : ", 10, 65, 120, "str")
        self.amount = EntryWithLabel(self.window, "Transaction Amount : ", 10,105, 120, "float")
        self.date_time = EntryWithLabel(self.window, "Transaction DateTime : ", 10, 145, 120,"str")
        self.source_account = EntryWithLabel(self.window, "Source Account : ", 10, 185, 120, "str")
        self.destination_account = EntryWithLabel(self.window, "Destination Account : ", 10, 225, 120, "str")
        self.name = EntryWithLabel(self.window, "Client Name : ", 10, 265, 120, "str")
        self.family = EntryWithLabel(self.window, "Client Family : ", 10, 305, 120, "str")
        self.username = EntryWithLabel(self.window, "Client Username : ", 10, 345, 120, "str")
        self.password = EntryWithLabel(self.window, "Client Password : ", 10, 385, 120, "str")
        self.account_type = EntryWithLabel(self.window, "Account Type : ", 10, 425, 120, "str")
        self.account_number = EntryWithLabel(self.window, "Account Number : ", 10, 465, 120, "int")

        Button(self.window, text="Save", command=save_Button).place(x=10, y=530)

        Button(self.window, text="Remove", command=Remove_Button).place(x=60, y=530)

        Button(self.window, text="Find All", command=Find_All_Button).place(x=180, y=530)

        Button(self.window, text="Edit ", command=Edit_Button).place(x=130, y=530)

        table = ttk.Treeview(self.window, height=25, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), show="headings")

        table.heading(1, text="Id")
        table.heading(2, text="Status")
        table.heading(3, text="Amount")
        table.heading(4, text="Datetime")
        table.heading(5, text="Source")
        table.heading(6, text="Destination")
        table.heading(7, text="Name")
        table.heading(8, text="family")
        table.heading(9, text="Account type")
        table.heading(10, text="Account No")

        table.column(1, width=50)
        table.column(2, width=80)
        table.column(3, width=80)
        table.column(4, width=80)
        table.column(5, width=90)
        table.column(6, width=80)
        table.column(7, width=70)
        table.column(8, width=70)
        table.column(9, width=110)
        table.column(10, width=80)

        table.place(x=265, y=25)

        table_transaction_refresher()


sgn = SignInView()
