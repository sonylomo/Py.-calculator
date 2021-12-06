from tkinter import*
import phonebackend

app=Tk()
app.title('My Phone Book')
mainframe=Frame(app).grid()

def selected_row(event):
	global selected_tuple
	index=lstList1.curselection()[0]

	selected_tuple=lstList1.get(index)
	print(index)
	name_txt.delete(0,END)
	name_txt.insert(END,selected_tuple[1])
	num_txt.delete(0, END)
	num_txt.insert(END, selected_tuple[2])

def viewbtn():
	lstList1.delete(0,END)
	for x in phonebackend.viewing():
		lstList1.insert(END,x)

def searchbtn():
	lstList1.delete(0,END)
	for row in phonebackend.search(name_txt.get(),num_txt.get()):
		lstList1.insert(END,row)

def insertbtn():
	phonebackend.insert(name_txt.get(),num_txt.get())
	lstList1.delete(0,END)
	lstList1.insert(END,(name_txt.get(),num_txt.get()))

def deletecom():
	phonebackend.delete(selected_tuple[0])


txt=StringVar()
txt2=StringVar()
name_txt=Entry(app, textvariable=txt)
name_txt.grid(column=1, row=1,columnspan=2, rowspan=1)
num_txt=Entry(app, textvariable=txt2)
num_txt.grid(column=1, row=2, columnspan=2, rowspan=1)

scrollbar1 = Scrollbar(app, orient=VERTICAL)
lstList1 = Listbox(app, exportselection=0, yscrollcommand=scrollbar1.set)
lstList1.bind('<<ListboxSelect>>',selected_row)
scrollbar1.config(command=lstList1.yview)
scrollbar1.grid(row=3, column=5, rowspan=5, sticky='nes')
lstList1.grid(row=3, column=0, rowspan=5, columnspan=3, sticky='nsew')

namelabel=Label(app,text='NAME:')
namelabel.grid(column=0,row=1)
numlabel=Label(app,text='PHONE NO.:')
numlabel.grid(column=0,row=2)

btn_create=Button(app,text='NEW CONTACT',width=12,command=insertbtn).grid(column=6,row=3)
btn_update=Button(app,text='UPDATE',width=12).grid(column=6,row=4)
btn_view=Button(app,text='VIEW ALL',width=12,command=viewbtn).grid(column=6,row=5)
btn_delete=Button(app,text='DELETE',width=12,command=deletecom).grid(column=6,row=6)
btn_search=Button(app,text='SEARCH',width=12,command=searchbtn).grid(column=6,row=7)


app.mainloop()