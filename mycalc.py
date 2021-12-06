import math
from tkinter import*
window=Tk()
window.title('My Calculator')
val=StringVar()
value=''

def press(num):
    global value
    value=value+str(num)
    val.set(value)

def clear():
    global value
    value=''
    val.set(value)

def equal():
    global value
    total=str(eval(value))
    val.set(total)

def sine():
    global value
    y=math.sin(str(val))
    val.set(y)

e1=Entry(window,textvariable=val).grid(column=0,row=1)
sine=Button(window,text='sin',command=sine).grid(column=4,row=3)
delete=Button(window,text='clear',command=clear).grid(column=0,row=5)
plus=Button(window,text='+',command=lambda:press('+')).grid(column=3,row=5)
minus=Button(window,text='-',command=lambda:press('-')).grid(column=3,row=4)
prod=Button(window,text='x',command=lambda:press('*')).grid(column=3,row=3)
anw=Button(window,text='=',command=equal).grid(column=2,row=5)
b=Button(window,text='.',command=lambda:press('.')).grid(column=3,row=2)
b0=Button(window,text='0',command=lambda:press(0)).grid(column=1,row=5)
b1=Button(window,text='1',command=lambda:press(1)).grid(column=0,row=4)
b2=Button(window,text='2',command=lambda:press(2)).grid(column=1,row=4)
b3=Button(window,text='3',command=lambda:press(3)).grid(column=2,row=4)
b4=Button(window,text='4',command=lambda:press(4)).grid(column=0,row=3)
b5=Button(window,text='5',command=lambda:press(5)).grid(column=1,row=3)
b6=Button(window,text='6',command=lambda:press(6)).grid(column=2,row=3)
b7=Button(window,text='7',command=lambda:press(7)).grid(column=0,row=2)
b8=Button(window,text='8',command=lambda:press(8)).grid(column=1,row=2)
b9=Button(window,text='9',command=lambda:press(9)).grid(column=2,row=2)
#txt=Text(window,height=2,width=5).grid(column=2,row=1)
window.mainloop()