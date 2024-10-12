from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from controller.transaction_controller import TransactionController
import datetime as dt

# class TransactionView:
#     def __init__(self, window, title, width, x, y):
#         self.table = ttk.Treeview(window, columns=(1, 2, 3, 4, 5, 6), show="headings")
#         self.table.column(1, width=50)
#         self.table.column(2, width=80)
#         self.table.column(3, width=110)
#         self.table.column(4, width=140)
#         self.table.column(5, width=170)
#         self.table.column(6, width=200)
#
#         self.table.heading(1, text="Id")
#         self.table.heading(2, text="Status")
#         self.table.heading(3, text="Amount")
#         self.table.heading(4, text="Datetime")
#         self.table.heading(5, text="Source Account")
#         self.table.heading(6, text="Destination Account")

def reset_form():
    id.set(0)
    status.set("")
    amount.set(0)
    date_time.set("")
    source_account.set("")
    destination_account.set("")


 def fill_datetime():
    now = datetime.now()
    datetime.set(now.strftime("%d/%m/%Y/%T"))
def refresh_table():
    for item in table.get_children():
        table.delete(item)

    for transaction in TransactionController.find_all():
        table.insert("", END, values=transaction)


def select_transaction(event):
    transaction = table.item(table.focus())["values"]
    id.set(transaction[0])
    status.set(transaction[1])
    amount.set(transaction[2])
    date_time.set(transaction[3])
    source_account.set(transaction[4])
    destination_account.set(transaction[5])

def save_click():
    TransactionController.save(status.get(),
                               amount.get(),
                               source_account.get(),
                               destination_account.get())
    msg.showinfo("Save", "Transaction Saved Successfully")
    reset_form()
def save_info():
    datetime_info = datetime.get()
    print(datetime_info)
    file = open("test.csv", "a")
    file.write(datetime_info)
    file.write(",")
    file.close()
    print(datetime_info)
    datetime.delete(0, END)

def edit_click():
    TransactionController.edit(status.get(),
                               amount.get(),
                               date_time.get(),
                               source_account.get(),
                               destination_account.get())
    msg.showinfo("Edit", "transaction Edited Successfully")
    reset_form()


def remove_click():
    if msg.askyesno("Remove", "Are You Sure Remove Transaction ?"):
        TransactionController.remove(id.get())
        msg.showinfo("Remove", "transaction Removed Successfully")
        reset_form()

def close_win():
    if msg.askyesno("Remove", "Are You Sure Remove Transaction ?"):
        exit()

win = Tk()
win.protocol("WM_DELETE_WINDOW", close_win)
win.geometry("800x400")
win.title("transaction Management")

# Id
Label(win, text="Id").place(x=20, y=20)
id = IntVar()
Entry(win, textvariable=id, state="readonly").place(x=140, y=20)

# status
Label(win, text="status").place(x=20, y=60)
status = StringVar()
name_txt = Entry(win, textvariable=status)
name_txt.place(x=140, y=60)

# amount
Label(win, text="amount").place(x=20, y=100)
amount = DoubleVar()
Entry(win, textvariable=amount).place(x=140, y=100)

# datetime
Label(win, text="datetime").place(x=20, y=140)
date_time = StringVar
Entry(win, textvariable=datetime).place(x=140, y=140)

# source_account
Label(win, text="source_account").place(x=20, y=180)
source_account = StringVar()
Entry(win, textvariable=source_account).place(x=140, y=180)

# destination_account
Label(win,text="destination_account").place(x=20, y=220)
destination_account = StringVar()
Entry(win, textvariable=destination_account).place(x=140, y=220)

table = ttk.Treeview(win, height=15, columns=(1, 2, 3, 4, 5, 6), show="headings")
table.heading(1, text="ID")
table.heading(2, text="Status")
table.heading(3, text="Amount")
table.heading(4, text="Datetime")
table.heading(5, text="Source_Account")
table.heading(6, text="Destination_Account")

table.column(1, width=40)
table.column(2, width=60)
table.column(3, width=80)
table.column(4, width=60)
table.column(5, width=115)
table.column(6, width=130)

table.bind("<ButtonRelease-1>", select_transaction)
table.bind("<KeyRelease>", select_transaction)

table.place(x=290, y=20)

Button(win, text="Save", width=7, command=save_click).place(x=20, y=320)
Button(win, text="Edit", width=7, command=edit_click).place(x=90, y=320)
Button(win, text="Remove", width=7, command=remove_click).place(x=160, y=320)
# datetime_button = Button(win, text="Fill DateTime", width=30, height=2, command=fill_datetime, bg="grey")
# datetime_button.place(x=15, y=260)
win.mainloop()