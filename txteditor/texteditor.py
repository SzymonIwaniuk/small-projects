import sys
from tkinter import *
import tkinter.filedialog

root = Tk()

root.title("Text Editor")
text = Text(root, undo=True)
text.grid()

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = tkinter.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if savelocation:
        with open(savelocation, "w+") as file1:
            file1.write(t)
        print("File saved successfully.")
    else:
        print("Save operation canceled.")

button=Button(root, text="Save", command=saveas)
button.grid()

def FontHelvetica():
    global text
    text.config(font="Helvetica")

def FontCourier():
    global text
    text.config(font="Courier")

def FontArial():
    global text
    text.config(font="Arial")


font = Menubutton(root, text="Font")
font.grid()
font.menu=Menu(font,tearoff=0)
font["menu"] = font.menu
helvetica = IntVar()
arial = IntVar()
courier=IntVar()

font.menu.add_checkbutton(label="Courier", variable=courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=helvetica, command=FontHelvetica)
font.menu.add_checkbutton(label="Arial", variable=arial, command=FontArial)


def undo_action():
    text.edit_undo()

def redo_action():
    text.edit_redo()

undo_button = Button(root, text="Undo", command=undo_action)
redo_button = Button(root, text="Redo", command=redo_action)
undo_button.grid(row=2, column=1)
redo_button.grid(row=1, column=1)

root.mainloop()