from tkinter import *
def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)
def buttonPushed():
    txt=t.get()
    label.config(text="text in the box is "+txt)
def resetPushed():
    t.delete(0,END)
root = Tk()
var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1,command=sel)
R1.pack( anchor = W )
R2 = Radiobutton(root, text="Option 2", variable=var, value=2,command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Option 3", variable=var, value=3,command=sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()
w = Label(root, text="hello good morning")
w.pack()

b = Button(root, text="click me",command=buttonPushed)
b.pack()

b1 = Button(root, text="reset me",command=resetPushed)
b1.pack()
t = Entry()
t.pack()

root.mainloop()

