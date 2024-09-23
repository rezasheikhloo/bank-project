from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
import database

def reset_form():
    id.set(0)
    creation_date.set("")
    status.set("")
    amount.set(0)

    total_var.set(f"Total : {database.total()}")
    refresh_table()
    creation_date_txt.focus_set()


def refresh_table():
    for item in table.get_children():
        table.delete(item)

    for transaction in database.find_all():
        table.insert("", END, values=transaction)


def select_transaction(event):
    transaction = table.item(table.focus())["values"]
    id.set(transaction[0])
    creation_date.set(transaction[1])
    status.set(transaction[2])
    amount.set(transaction[3])


def save_click():
    database.save(creation_date.get(), status.get(), amount.get())
    msg.showinfo("Save", "transaction Saved Successfully")
    reset_form()


def edit_click():
    database.edit(id.get(), creation_date.get(), status.get(), amount.get())
    msg.showinfo("Edit", "transaction Edited Successfully")
    reset_form()


def remove_click():
    if msg.askyesno("Remove", "Are You Sure Remove transaction ?"):
        database.remove(id.get())
        msg.showinfo("Remove", "transaction Removed Successfully")
        reset_form()

def close_win():
    if msg.askyesno("Remove", "Are You Sure Remove transaction ?"):
        exit()

win = Tk()
win.protocol("WM_DELETE_WINDOW", close_win)
win.geometry("630x370")
win.title("transaction Management")

# Id
Label(win, text="Id").place(x=20, y=20)
id = IntVar()
Entry(win, textvariable=id, state="readonly").place(x=90, y=20)

# Name
Label(win, text="creation_date").place(x=20, y=60)
creation_date = StringVar()
creation_date_txt = Entry(win, textvariable=creation_date)
creation_date_txt.place(x=90, y=60)

# Brand
Label(win, text="status").place(x=20, y=100)
status = StringVar()
Entry(win, textvariable=status).place(x=90, y=100)

# Quantity
Label(win, text="amount").place(x=20, y=140)
amount = IntVar()
Entry(win, textvariable=amount).place(x=90, y=140)


total_var = StringVar()
Label(win, font=("Arial Black", 14), textvariable=total_var).place(x=20, y=230)



table = ttk.Treeview(win, height=15, columns=(1, 2, 3, 4), show="headings")
table.heading(1, text="ID")
table.heading(2, text="creation-date")
table.heading(3, text="status")
table.heading(4, text="amount")

table.column(1, width=60)
table.column(2, width=80)
table.column(3, width=80)
table.column(4, width=60)


table.bind("<ButtonRelease-1>", select_transaction)
table.bind("<KeyRelease>", select_transaction)

table.place(x=250, y=20)

Button(win, text="Save", width=7, command=save_click).place(x=20, y=320)
Button(win, text="Edit", width=7, command=edit_click).place(x=90, y=320)
Button(win, text="Remove", width=7, command=remove_click).place(x=160, y=320)

reset_form()

win.mainloop()
