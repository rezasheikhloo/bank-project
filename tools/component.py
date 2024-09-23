from tkinter import *
from tkinter import ttk as ttk


class Table:
    def __init__(self, window, titles, widths, x, y,clicker_function):
        self.clicker_function = clicker_function
        self.table = ttk.Treeview(window, columns=titles, show="headings")

        for idx, name in enumerate(titles):
            self.table.heading(name, text=name)
            self.table.column(name, width=widths[idx])

        self.table.bind("<ButtonRelease-1>", self.table_click)
        self.table.place(x=x, y=y)

    def table_click(self, event):
        return self.clicker_function(tuple(self.table.item(self.table.focus())["values"]))

    def clear_table(self):
        for item in self.table.get_children():
            self.table.delete(item)

    def set_data(self, data_list):
        self.clear_table()
        if data_list:
            for data in data_list:
                self.table.insert("", END, values=data)
