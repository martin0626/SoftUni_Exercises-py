from tkinter import *
from tkcalendar import DateEntry


tk = Tk()
def clear_view ():
    for button in tk.grid_slaves():
        button.destroy()

def tasks_view ():
    clear_view ()
    Label(tk, text='Enter your task name:').grid(row=0, column=0, padx=20, pady=20)
    name = Entry(tk).grid(row=0, column=1)
    Label(tk, text='Due date:').grid(row=1, column=0, padx=20, pady=20)
    date = DateEntry(tk).grid(row=1, column=0)


def start_view():
    Button(tk, text="List Tasks", bg='blue', fg='white').grid(row=0, column=0, padx=200, pady=200)
    Button(tk, text='Create new task', bg='green', fg='white', command=lambda:tasks_view()).grid(row=0, column=1, padx=100, pady=200)

start_view()
tk.geometry("900x700")
tk.mainloop()



