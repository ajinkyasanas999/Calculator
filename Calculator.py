from tkinter import *

root = Tk()


def btn(numbers):
     global operator
     operator = operator + str(numbers)
     textvalue.set(operator)

def clear():
     global operator
     operator = ""
     textvalue.set("")
def equal():
     global operator
     sumup=str(eval(operator))
     textvalue.set(sumup)
     operator = ""

operator = ""
textvalue = StringVar()
textenter=Entry(root,textvariable=textvalue, justify="right", insertwidth=4, bd=8).grid(columnspan=4)

b9 = Button(root, text="9", padx=8, bd=5, command=lambda:btn(9)).grid(row=1, column=0)
b8 = Button(root, text="8", padx=8, bd=5, command=lambda:btn(8)).grid(row=1, column=1)
b7 = Button(root, text="7", padx=8, bd=5, command=lambda:btn(7)).grid(row=1, column=2)
b6 = Button(root, text="6", padx=8, bd=5, command=lambda:btn(6)).grid(row=2, column=0)
b5 = Button(root, text="5", padx=8, bd=5, command=lambda:btn(5)).grid(row=2, column=1)
b4 = Button(root, text="4", padx=8, bd=5, command=lambda:btn(4)).grid(row=2, column=2)
b1 = Button(root, text="1", padx=8, bd=5, command=lambda:btn(1)).grid(row=3, column=0)
b2 = Button(root, text="2", padx=8, bd=5, command=lambda:btn(2)).grid(row=3, column=1)
b3 = Button(root, text="3", padx=8, bd=5, command=lambda:btn(3)).grid(row=3, column=2)
bd = Button(root, text="/", padx=8, bd=5, command=lambda:btn("/")).grid(row=4, column=0)
b0 = Button(root, text="0", padx=8, bd=5, command=lambda:btn(0)).grid(row=4, column=1)
bm = Button(root, text="x", padx=8, bd=5, command=lambda:btn("*")).grid(row=4, column=2)
bs = Button(root, text="-", padx=8, bd=5, command=lambda:btn("-")).grid(row=5, column=0)
ba = Button(root, text="+", padx=8, bd=5, command=lambda:btn("+")).grid(row=5, column=1)
be = Button(root, text="=", padx=8, bd=5, command=equal).grid(row=6, column=1)
bc = Button(root, text="C", padx=8, bd=5, command=clear).grid(row=5, column=2)

root.mainloop()
