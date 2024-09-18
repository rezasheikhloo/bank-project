from tkinter import *
from tkinter import ttk
from view.component import Table

person_list = [(1, "ali", "alipour", 20),
               (2, "reza", "rezaii", 24)]


class PersonView:
    def __init__(self):
        win = Tk()
        win.geometry("300x300")

        self.person_table = Table(win, ["Id", "Name", "Family", "Age"], [50,80,80,50],20,20, self.person_table_click)

        self.person_table.set_data(person_list)

        win.mainloop()

    def person_table_click(row):
        print(row)

    


