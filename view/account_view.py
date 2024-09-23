from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import database

def reset_form():
    id.set(0)
    name.set("")
    account_type.set("")
    account_number.set(0)

    total_var.set(f"Total : {database.total()}")
    refresh_table()
    name_txt.focus_set()


def refresh_table():
    for item in table.get_children():
        table.delete(item)

    for account in database.find_all():
        table.insert("", END, values=account)


def select_account(event):
    account = table.item(table.focus())["values"]
    id.set(account[0])
    name.set(account[1])
    account_type.set(account[2])
    account_number.set(account[3])


def save_click():
    database.save(name.get(), account_type.get(), account_number.get())
    msg.showinfo("Save", "account Saved Successfully")
    reset_form()


def edit_click():
    database.edit(id.get(), name.get(), account_type.get(), account_number.get())
    msg.showinfo("Edit", "transaction Edited Successfully")
    reset_form()


def remove_click():
    if msg.askyesno("Remove", "Are You Sure Remove transaction ?"):
        database.remove(id.get())
        msg.showinfo("Remove", "transaction Removed Successfully")
        reset_form()

def close_win():
    if msg.askyesno("Remove", "Are You Sure Remove account ?"):
        exit()

win = Tk()
win.protocol("WM_DELETE_WINDOW", close_win)
win.geometry("630x370")
win.title("account Management")

# Id
Label(win, text="Id").place(x=20, y=20)
id = IntVar()
Entry(win, textvariable=id, state="readonly").place(x=90, y=20)

# Name
Label(win, text="creation_date").place(x=20, y=60)
name = StringVar()
name_txt = Entry(win, textvariable=name)
name_txt.place(x=90, y=60)

# Brand
Label(win, text="status").place(x=20, y=100)
account_type = StringVar()
Entry(win, textvariable=account_type).place(x=90, y=100)

# Quantity
Label(win, text="amount").place(x=20, y=140)
account_number = IntVar()
Entry(win, textvariable=account_number).place(x=90, y=140)


total_var = StringVar()
Label(win, font=("Arial Black", 14), textvariable=total_var).place(x=20, y=230)



table = ttk.Treeview(win, height=15, columns=(1, 2, 3, 4), show="headings")
table.heading(1, text="ID")
table.heading(2, text="name")
table.heading(3, text="account_type")
table.heading(4, text="account_number")

table.column(1, width=60)
table.column(2, width=80)
table.column(3, width=80)
table.column(4, width=60)


table.bind("<ButtonRelease-1>", select_account)
table.bind("<KeyRelease>", select_account)

table.place(x=250, y=20)

Button(win, text="Save", width=7, command=save_click).place(x=20, y=320)
Button(win, text="Edit", width=7, command=edit_click).place(x=90, y=320)
Button(win, text="Remove", width=7, command=remove_click).place(x=160, y=320)

reset_form()

win.mainloop()


def transactionView():
    pass