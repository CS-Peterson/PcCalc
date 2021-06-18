from tkinter import *


def solve(event):
    global value
    text = event.widget.cget("text")
    if text == "C":
        enter.set("")
    elif text == "=":
        if enter.get().isdigit():
            value = int(enter.get())
        else:
            value = eval(enter.get())
            enter.set(value)
            entered.update()
    else:
        enter.set(enter.get() + text)
        entered.update()
    
    


root = Tk()

root.geometry("300x600")
root.maxsize(300, 600)
root.minsize(300, 600)
root.title("Calculator")
# root.wm_iconbitmap("F:\PROGRAMMING\PYTHON\PROJECTS\GUI Calculator\Icon.ico")


view = Frame(root)
view.pack()


enter = StringVar()
entered = Entry(view, textvariable=enter, bg="light blue", fg="red",
                borderwidth=6, relief=FLAT, font="calibiri 40 bold")
entered.pack()

keys = Frame(root)
keys.pack()

b1 = Button(keys, text="=", bg="orange", width=12, height=2,
            borderwidth=4, relief=SUNKEN, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)

b1 = Button(keys, text="C", bg="orange", width=12, height=2,
            borderwidth=4, relief=SUNKEN, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)


keys = Frame(root)
keys.pack()

b1 = Button(keys, text="9", bg="light blue", width=6, height=2,
            borderwidth=4, relief=GROOVE, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)

b1 = Button(keys, text="8", bg="light blue", width=6, height=2,
            borderwidth=4, relief=GROOVE, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)

b1 = Button(keys, text="7", bg="light blue", width=6, height=2,
            borderwidth=4, relief=GROOVE, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)

keys1 = Frame(root)
keys1.pack()

b1 = Button(keys1, text="6", bg="light blue", width=6, height=2,
            borderwidth=4, relief=GROOVE, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)

b1 = Button(keys1, text="5", bg="light blue", width=6, height=2,
            borderwidth=4, relief=GROOVE, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)

b1 = Button(keys1, text="4", bg="light blue", width=6, height=2,
            borderwidth=4, relief=GROOVE, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)

keys2 = Frame(root)
keys2.pack()

b1 = Button(keys2, text="3", bg="light blue", width=6, height=2,
            borderwidth=4, relief=GROOVE, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)

b1 = Button(keys2, text="2", bg="light blue", width=6, height=2,
            borderwidth=4, relief=GROOVE, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)

b1 = Button(keys2, text="1", bg="light blue", width=6, height=2,
            borderwidth=4, relief=GROOVE, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)

keys2 = Frame(root)
keys2.pack()

b1 = Button(keys2, text="-", bg="orange", width=6, height=2,
            borderwidth=4, relief=SUNKEN, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)

b1 = Button(keys2, text="0", bg="light blue", width=6, height=2,
            borderwidth=4, relief=GROOVE, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)

b1 = Button(keys2, text="+", bg="orange", width=6, height=2,
            borderwidth=4, relief=SUNKEN, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)

keys2 = Frame(root)
keys2.pack()

b1 = Button(keys2, text="*", bg="orange", width=6, height=2,
            borderwidth=4, relief=SUNKEN, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)

b1 = Button(keys2, text="/", bg="orange", width=6, height=2,
            borderwidth=4, relief=SUNKEN, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)

b1 = Button(keys2, text=".", bg="orange", width=6, height=2,
            borderwidth=4, relief=SUNKEN, padx=10, pady=10, font="mangal 9 bold")
b1.pack(side=LEFT, padx=4, pady=4, fill=X)
b1.bind("<Button-1>", solve)


root.mainloop()
