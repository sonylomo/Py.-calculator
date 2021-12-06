from tkinter import*
import backend

def get_selected_row(event):
	global selected_tuple
	index=lst1.curselection()[0]

	selected_tuple=lst1.get(index)
	print(index)
	e1.delete(0,END)
	e1.insert(END,selected_tuple[1])

	e2.delete(0,END)
	e2.insert(END,selected_tuple[2])

	e3.delete(0,END)
	e3.insert(END,selected_tuple[3])

	e4.delete(0,END)
	e4.insert(END,selected_tuple[4])

def viewbtn():
	lst1.delete(0,END)
	for x in backend.view():
		lst1.insert(END,x)

def searchbtn():
	lst1.delete(0,END)
	for row in backend.search(Tval.get(),Authval.get(),Yval.get(),isbnval.get()):
		lst1.insert(END,row)

def insertbtn():
	backend.insert(Tval.get(),Authval.get(),Yval.get(),isbnval.get())
	lst1.delete(0,END)
	lst1.insert(END,(Tval.get(),Authval.get(),Yval.get(),isbnval.get()))

def deletecomd():
	backend.delete(selected_tuple[0])

window=Tk()

l1=Label(window,text='Title')
l1.grid(row=0,column=0)

l2=Label(window,text='Author')
l2.grid(row=0,column=2)

l3=Label(window,text='Year')
l3.grid(row=1,column=0)

l4=Label(window,text='ISBN')
l4.grid(row=1,column=2)

Tval=StringVar()
e1=Entry(window,textvariable=Tval)
e1.grid(row=0,column=1)

Authval=StringVar()
e2=Entry(window,textvariable=Authval)
e2.grid(row=0,column=3)

Yval=StringVar()
e3=Entry(window,textvariable=Yval)
e3.grid(row=1,column=1)

isbnval=StringVar()
e4=Entry(window,textvariable=isbnval)
e4.grid(row=1,column=3)

lst1=Listbox(window,height=8,width=25)
lst1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=4,column=2)

lst1.configure(yscrollcommand=sb1.set)
sb1.configure(command=lst1.yview)

lst1.bind("<<ListboxSelect>>",get_selected_row)

btn1=Button(window,text='view all',width=13,command=viewbtn)
btn1.grid(row=2,column=3)

btn2=Button(window,text="Search entry", width=13, command=searchbtn)
btn2.grid(row=3,column=3)

btn3=Button(window,text='Add Entry',width=13,command=insertbtn)
btn3.grid(row=4,column=3)

btn4=Button(window,text='Update',width=13)
btn4.grid(row=5,column=3)

btn5=Button(window,text='Delete',width=13,command=deletecomd)
btn5.grid(row=6,column=3)

btn6=Button(window,text='Close',width=13)
btn6.grid(row=7,column=3)

window.mainloop()
