from tkinter import ttk
from tkinter import *
from controller.transaction_controller import TransactionController
from commponent import *

win = Tk()
win.geometry("700x500")
class TransactionView:
    def __init__(self, window, title, width):
        self.table = ttk.Treeview(window, columns=(1, 2, 3, 4, 5, 6), show="headings")
        self.table.column(1, width=50)
        self.table.column(2, width=80)
        self.table.column(3, width=110)
        self.table.column(4, width=140)
        self.table.column(5, width=170)
        self.table.column(6, width=200)

        self.table.heading(1, text="Id")
        self.table.heading(2, text="Status")
        self.table.heading(3, text="Amount")
        self.table.heading(4, text="Datetime")
        self.table.heading(5, text="Source Account")
        self.table.heading(6, text="Destination Account")

win.mainloop()