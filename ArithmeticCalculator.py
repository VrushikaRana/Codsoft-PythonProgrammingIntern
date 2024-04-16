# Making a GUI Calculator which performs "Arithmetic Operations" in Python language
import tkinter as tk

#for the input
calculation= ""

#for adding the desired digits
def add(symbol):
    global calculation
    calculation += str(symbol)
    result.delete(1.0,"end")
    result.insert(1.0,calculation)

#for performing the calculation
def evaluate():
    global calculation
    try:
        calculation=str(eval(calculation))
        result.delete(1.0,"end")
        result.insert(1.0,calculation)
    except:
        clear_field()
        result.insert(1.0,"Error")
        
#for clearing the previous contents
def clear_field():
    global calculation
    calculation = ""
    result.delete(1.0,"end")
#for the output interface like calculator in mobile
root=tk.Tk()
root.geometry("300x275")
root.title("GUI Arithmetic Calculator")
result=tk.Text(root,height=2,width=16,font=("Times News Roman",24))
result.grid(columnspan=5)

#for creating the columns and rows for inserting the operands
one=tk.Button(root,text="1",command=lambda: add(1),width=6,font=('Times News Roman',14))
one.grid(row=4,column=1)
two=tk.Button(root,text="2",command=lambda: add(2),width=6,font=('Times News Roman',14))
two.grid(row=4,column=2)
three=tk.Button(root,text="3",command=lambda: add(3),width=6,font=('Times News Roman',14))
three.grid(row=4,column=3)
four=tk.Button(root,text="4",command=lambda: add(4),width=6,font=('Times News Roman',14))
four.grid(row=3,column=1)
five=tk.Button(root,text="5",command=lambda: add(5),width=6,font=('Times News Roman',14))
five.grid(row=3,column=2)
six=tk.Button(root,text="6",command=lambda: add(6),width=6,font=('Times News Roman',14))
six.grid(row=3,column=3)
seven=tk.Button(root,text="7",command=lambda: add(7),width=6,font=('Times News Roman',14))
seven.grid(row=2,column=1)
eight=tk.Button(root,text="8",command=lambda: add(8),width=6,font=('Times News Roman',14))
eight.grid(row=2,column=2)
nine=tk.Button(root,text="9",command=lambda: add(9),width=6,font=('Times News Roman',14))
nine.grid(row=2,column=3)
zero=tk.Button(root,text="0",command=lambda: add(0),width=6,font=('Times News Roman',14))
zero.grid(row=5,column=3)

plus=tk.Button(root,text="+",command=lambda: add("+"),width=6,font=('Times News Roman',14))
plus.grid(row=4,column=4)
minus=tk.Button(root,text="-",command=lambda: add("-"),width=6,font=('Times News Roman',14))
minus.grid(row=3,column=4)
mul=tk.Button(root,text="*",command=lambda: add("*"),width=6,font=('Times News Roman',14))
mul.grid(row=2,column=4)
div=tk.Button(root,text="/",command=lambda: add("/"),width=6,font=('Times News Roman',14))
div.grid(row=1,column=4)
modulus=tk.Button(root,text="%",command=lambda: add("%"),width=6,font=('Times News Roman',14))
modulus.grid(row=1,column=3)
floor_divison=tk.Button(root,text="//",command=lambda: add("//"),width=6,font=('Times News Roman',14))
floor_divison.grid(row=1,column=2)


open=tk.Button(root,text="(",command=lambda: add("("),width=6,font=('Times News Roman',14))
open.grid(row=5,column=1)
close=tk.Button(root,text=")",command=lambda: add(")"),width=6,font=('Times News Roman',14))
close.grid(row=5,column=2)
equals=tk.Button(root,text="=",command=evaluate,width=6,font=('Times News Roman',14))
equals.grid(row=5,column=4)
clear=tk.Button(root,text="C",command=clear_field,width=6,font=('Times News Roman',14))
clear.grid(row=1,column=1)

root.mainloop() 
