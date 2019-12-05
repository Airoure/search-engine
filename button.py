from tkinter import *

top = Tk()


def helloCallBack():
    tkMessageBox.showinfo("Hello Python", "Hello Runoob")


B = Button(top, text="搜素", command=helloCallBack)

B.pack()
top.mainloop()