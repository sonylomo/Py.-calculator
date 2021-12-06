import time
import datetime
from tkinter import*
import phoneback

def selected_row(event):
    global selected_tuple
    index=lstList1.curselection()[0]

    selected_tuple=lstList1.get(index)
    print(index)
    name_txt.delete(0,END)
    name_txt.insert(END,selected_tuple[1])

    num_txt.delete(0,END)
    num_txt.insert(END,selected_tuple[2])

    email_txt.delete(0,END)
    email_txt.insert(END,selected_tuple[3])

    smedia_txt.delete(0,END)
    smedia_txt.insert(END,selected_tuple[4])

def viewbtn():
    lstList1.delete(0,END)
    for x in phoneback.viewing():
        lstList1.insert(END,x)()
#for x in phonebackend.viewing():
def searchbtn():
    lstList1.delete(0,END)
    #for row in (http://localhost:8888/notebooks/phonelistings.ipynb.search(name_txt.get(),num_txt.get(),email_txt.get(),smedia_txt.get())):
    for row in phoneback.search(name_txt.get(),num_txt.get(),email_txt.get(),smedia_txt.get()):
        lstList1.insert(END,row)
#for row in phonebackend.search(name_txt.get(),num_txt.get(),email_txt.get(),smedia_txt.get()):
def insertbtn():
	phoneback.insert(name_txt.get(),num_txt.get(),email_txt.get(),smedia_txt.get())
	lstList1.delete(0,END)
	lstList1.insert(END,(name_txt.get(),num_txt.get(),email_txt.get(),smedia_txt.get()))
#phonebackend.insert(name_txt.get(),num_txt.get(),email_txt.get(),smedia_txt.get())
def deletecom():
    phoneback.deleting(selected_tuple[0])
#phonebackend.delete(selected_tuple[0])

app=Tk()
app.title('Phone Book')
time1=''
#f2=Frame(app,width=300,height=320,bd=8,bg="powder blue")
#f2.grid(column=1,row=8)

mainframe=Frame(app).grid(row=0,column=0,columnspan=4)
app.geometry('650x600')
app.configure(bg='powder blue')

txt=StringVar()
txt2=StringVar()
txt3=StringVar()
txt4=StringVar()
#todays_date=StringVar()
#todays_time=StringVar()

name_txt=Entry(app, textvariable=txt)
name_txt.grid(column=1, row=1,columnspan=2, rowspan=1)
num_txt=Entry(app, textvariable=txt2)
num_txt.grid(column=1, row=2, columnspan=2, rowspan=1)
email_txt=Entry(app,textvariable=txt3)
email_txt.grid(column=7,row=1)
smedia_txt=Entry(app,textvariable=txt4)
smedia_txt.grid(column=7,row=2)

scrollbar1 = Scrollbar(app, orient=VERTICAL)
lstList1 = Listbox(app, exportselection=0, yscrollcommand=scrollbar1.set)
lstList1.bind('<<ListboxSelect>>',selected_row)
scrollbar1.config(command=lstList1.yview)
scrollbar1.grid(row=3, column=6, rowspan=5, sticky='nes')
lstList1.grid(row=3, column=0, rowspan=5, columnspan=6, sticky='nsew')


namelabel=Label(app,text='NAME:',bg='powder blue',font=('comic sans ms',15,'bold'))
namelabel.grid(column=0,row=1)
numlabel=Label(app,text='PHONE NO:',bg='powder blue',font=('comic sans ms',15,'bold'))
numlabel.grid(column=0,row=2)
emaillabel=Label(app,text='EMAIL:',bg='powder blue',font=('comic sans ms',15,'bold'))
emaillabel.grid(column=5,row=1)
smedialabel=Label(app,text='MEDIA \n HANDLE:',bg='powder blue',font=('comic sans ms',12,'bold'))
smedialabel.grid(column=5,row=2)
titlelabel=Label(app,font=('times new roman',25,'bold'),text='PHONELIST',bg='powder blue',fg='white')
titlelabel.grid(column=1,row=0)

#todays_date.set(time.strftime("%d/%m/%Y"))
date=time.strftime("%d/%m/%Y")
datelabel=Label(app,font=('times new roman',15,'bold'),bg='powder blue',text=date).grid(column=7,row=0)

#datelabel.config()

#clock = Label(app, font=('times', 20, 'bold'), bg='green')
#clock.grid(column=1,row=8)

#time2 = time.strftime('%H:%M:%S')
#if time2 != time1:
       # time1 = time2
       # clock.config(text=time2)

btn_create=Button(app,text='ADD CONTACT',width=12,command=insertbtn,bg='blue',font='ebrima').grid(column=7,row=3)
#btn_update=Button(app,text='CHANGE',width=12,bg='blue',font='ebrima').grid(column=7,row=4)
btn_view=Button(app,text='VIEW ALL',width=12,command=viewbtn ,bg='blue',font='ebrima').grid(column=7,row=5)
btn_delete=Button(app,text='DELETE',width=12,command=deletecom,bg='blue',font='ebrima').grid(column=7,row=6)
btn_search=Button(app,text='SEARCH',width=12,command=searchbtn,bg='blue',font='ebrima').grid(column=7,row=4)


app.mainloop()
