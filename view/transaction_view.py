from tkinter import *
from tkinter import ttk


win = Tk()

table = ttk.Treeview(win, columns=(1, 2, 3, 4, 5, 6), show="headings")
table.column(1, width=50)
table.column(2, width=80)
table.column(3, width=110)
table.column(4, width=140)
table.column(5, width=170)
table.column(6, width=200)

table.heading(1, text="Id")
table.heading(2, text="Status")
table.heading(3, text="Amount")
table.heading(4, text="Datetime")
table.heading(5, text="Source_account")
table.heading(6, text="Destination_account")



win.mainloop()