import os
import shutil
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


def open_directory():
    dir_path = filedialog.askdirectory(initialdir=cur_path.get())
    if dir_path:
        display_directory(dir_path)


def display_directory(path):
    if os.path.exists(path):
        cur_path.set(path)
        files_list.delete(0, END)
        for entry in os.listdir(path):
            files_list.insert(END, entry)


def on_double_click(event):
    selected = files_list.curselection()
    if selected:
        item = files_list.get(selected[0])
        item_path = os.path.join(cur_path.get(), item)
        if os.path.isdir(item_path):
            display_directory(item_path)


root = Tk()
root.title("File Browser")

cur_path = StringVar()
cur_path.set(os.path.expanduser("~"))

toolbar = Frame(root)
toolbar.pack(side=TOP, fill=X)

open_button = Button(toolbar, text="Open", command=open_directory)
open_button.pack(side=LEFT, padx=2, pady=2)

path_label = Label(toolbar, textvariable=cur_path, anchor="w")
path_label.pack(side=LEFT, fill=X, padx=2, pady=2)

files_list = Listbox(root)
files_list.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar = Scrollbar(root, orient=VERTICAL, command=files_list.yview)
scrollbar.pack(side=LEFT, fill=Y)

files_list.config(yscrollcommand=scrollbar.set)

files_list.bind('<Double-Button-1>', on_double_click)

display_directory(cur_path.get())

root.mainloop()
