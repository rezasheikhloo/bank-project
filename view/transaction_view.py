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
    name_txt.focus_set()


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
    database.save(client.get(), operation.get(), quantity.get())
    msg.showinfo("Save", "transaction Saved Successfully")
    reset_form()


def edit_click():
    database.edit(id.get(), client.get(), operation.get(), quantity.get())
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
Label(win, text="client").place(x=20, y=60)
name = StringVar()
name_txt = Entry(win, textvariable=name)
name_txt.place(x=90, y=60)

# Brand
Label(win, text="operation").place(x=20, y=100)
transaction_type = StringVar()
Entry(win, textvariable=operation).place(x=90, y=100)

# Quantity
Label(win, text="Quantity").place(x=20, y=140)
quantity = IntVar()
Entry(win, textvariable=quantity).place(x=90, y=140)


total_var = StringVar()
Label(win, font=("Arial Black" , 14), textvariable=total_var).place(x=20, y=230)



table = ttk.Treeview(win, height=15, columns=(1, 2, 3, 4), show="headings")
table.heading(1, text="ID")
table.heading(2, text="client")
table.heading(3, text="operation")
table.heading(4, text="Quantity")

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
