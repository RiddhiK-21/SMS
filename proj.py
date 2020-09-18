from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import socket
import requests
import bs4
import array
import textwrap

con=None
try:
	con=connect("proj.db")
	print("connected")
	cursor=con.cursor()
	sql="create table Student(rno int primary key,name text,marks int)"
	cursor.execute(sql)     
	print("table created")
except Exception as e:
	print("creation issue",e)
finally:
	if con is not None:
		con.close()
		print("disconnected")



def f1():
	adst.deiconify()
	root.withdraw()
	entrno.delete(0,END)
	entname.delete(0,END)
	entmks.delete(0,END)
def f2():
	root.deiconify()
	adst.withdraw()
def f4():
	root.deiconify()
	vist.withdraw()
def f3():
	stdata.delete(1.0,END)
	vist.deiconify()
	root.withdraw()
	con=None
	try:
		con=connect("proj.db")
		print("connected")
		cursor=con.cursor()
		sql="select * from Student order by rno asc"
		cursor.execute(sql)
		data=cursor.fetchall()   
		info=""
		for d in data:
			info=info+"rno: "+str(d[0])+" name: "+str(d[1])+"  marks: "+str(d[2])+"\n"
		stdata.insert(INSERT,info)
	except Exception as e:
		print("select issue",e)
		
	finally:
		if con is not None:
			con.close()
			print("disconnected")
def f5():
	try:
		con=connect("proj.db")
		print("connected")
		if entrno.index("end")==0:
			showwarning("issue","rno Empty")
		elif int(entrno.get())<0:
			showwarning("issue","Negative rno")
		else:
			rno=int(entrno.get())
			name=entname.get()
			if len(name)==0:
				showwarning("issue","Name is Empty")
			elif len(name)<2:
				showwarning("issue","Less no of characters")
			elif name.isalpha()==False:
				showwarning("issue","Inappropriate name")
			else:
				if entmks.index("end")==0:
					showwarning("issue","Marks are Empty")
				elif (int(entmks.get())<0 or int(entmks.get())>100):
					showwarning("issue","Enter marks between 0 to 100")
				
				else:
					marks=int(entmks.get())
					args=(rno,name,marks)
					cursor=con.cursor()
					sql="insert into Student values('%d','%s','%d')"
					cursor.execute(sql % args)     
					con.commit()
					showinfo("success","record added")
	except Exception as e:
		showerror("failure",str(e))
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("disconnected")
def f6():
	upst.deiconify()
	root.withdraw()
	entrno1.delete(0,END)
	entname1.delete(0,END)
	entmks1.delete(0,END)
def f7():
	delst.deiconify()
	root.withdraw()
	entrno2.delete(0,END)
def f8():
	root.withdraw()
	con=None
	try:
		con=connect("proj.db")
		print("connected")
		cursor=con.cursor()
		sql="select * from Student order by marks desc"
		cursor.execute(sql)
		data=cursor.fetchall()  
		name1=[]
		marks1=[]
		for d in data:
			name1.append(str(d[1]))
			marks1.append(int(d[2]))
		n2=name1[0:5]
		m2=marks1[0:5]
		x=np.arange(len(n2))
		plt.bar(x,m2,width=0.25)
		plt.xticks(x,n2)
		plt.title("Marks of all students")
		plt.xlabel("Names")
		plt.ylabel("Marks")
		plt.show()

	except Exception as e:
		showerror("chart issue",e)
		
	finally:
		if con is not None:
			con.close()
			print("disconnected")
	root.deiconify()
	
def f9():
	con=None
	try:
		con=connect("proj.db")
		print("connected")
		
		if entrno1.index("end")==0:
			showwarning("issue","rno Empty")
		elif int(entrno1.get())<0:
			showwarning("issue","Negative rno")
		else:
			rno=int(entrno1.get())
			name=entname1.get()
			if len(name)==0:
				showwarning("issue"," name Empty")
			elif len(name)<2:
				showwarning("issue","Less no of characters")
			elif name.isalpha()==False:
				showwarning("issue","Inappropriate name")
			else:
				if entmks1.index("end")==0:
					showwarning("issue","Marks are Empty")
				elif (int(entmks1.get())<0 or int(entmks1.get())>100):
					showwarning("issue","Enter marks between 0 to 100")
				
				else:
					marks=int(entmks1.get())
					args=(name,marks,rno)
					cursor=con.cursor()
					sql="update Student set name='%s',marks='%d' where rno='%d'"
					cursor.execute(sql % args)
					if cursor.rowcount>=1:	
						con.commit()
						showinfo("success","Record updated")
					else:
						showwarning("Warning","rno does not exists")
	except Exception as e:
		showerror("update issue",e)
		con.rollback()
	
	finally:
		if con is not None:
			con.close()
			print("disconnected")
def f10():
	upst.withdraw()
	root.deiconify()
def f11():
	try:
		con=connect("proj.db")
		print("connected")
		if entrno2.index("end")==0:
			showwarning("issue","rno is Empty")
		elif int(entrno2.get())<0:
			showwarning("issue","Negative rno")
		else:
			rno=int(entrno2.get())
			args=(rno)
			cursor=con.cursor()
			sql="delete from Student where rno='%d'"
			cursor.execute(sql % args)
			if cursor.rowcount>=1:
				con.commit()
				showinfo("success","record deleted")
			else:
				showerror("issue","rno does not exists")

	except Exception as e:
		showerror("update issue",e)
		con.rollback()
	
	finally:
		if con is not None:
			con.close()
			print("disconnected")
def f12():
	delst.withdraw()
	root.deiconify()


#root window
root=Tk()
root.title("SMS")
root.geometry("500x500+400+50")
root.configure(background="pale green")
btnadd=Button(root,text="ADD",font=("arial",18,"bold"),width=10,command=f1)
btnview=Button(root,text="VIEW",font=("arial",18,"bold"),width=10,command=f3)
btnup=Button(root,text="UPDATE",font=("arial",18,"bold"),width=10,command=f6)
btndel=Button(root,text="DELETE",font=("arial",18,"bold"),width=10,command=f7)
btnch=Button(root,text="CHARTS",font=("arial",18,"bold"),width=10,command=f8)

socket.create_connection( ("www.google.com", 80))
a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"	
a2 = "&q=" + "mumbai"
a3 = "&appid=c6e315d09197cec231495138183954bd"
api_address =  a1 + a2  + a3 		
res = requests.get(api_address)
print(res)
data=res.json()
temp=str(data['main']['temp'])
t=""
t="Location : Mumbai   Temp : "+temp

socket.create_connection(("www.google.com",80))
print("CONNECTED...!!")
res=requests.get("https://www.brainyquote.com/quote_of_the_day")
print(res)
soup=bs4.BeautifulSoup(res.text,"lxml")
data=soup.find("img",{"class":"p-qotd"})
quote=data['alt']
q=""
q="QOTD : "+quote


lbl1=Label(root,text=t,font=("calibri",16,"bold italic"))
lbl2=Label(root,text=q,wraplength=400,font=("calibri",16,"bold italic"))

btnadd.pack(pady=5)
btnview.pack(pady=5)
btnup.pack(pady=5)
btndel.pack(pady=5)
btnch.pack(pady=5)
lbl1.pack(pady=20)
lbl2.pack(pady=5)

#add student
adst=Toplevel(root)
adst.title("Add student")
adst.geometry("500x400+400+200")
adst.configure(background="cyan")
adst.withdraw()
lblrno=Label(adst,text="Enter rno",font=("arial",18,"bold"))
entrno=Entry(adst,bd=5,font=("arial",18,"bold"))
lblname=Label(adst,text="Enter name",font=("arial",18,"bold"))
entname=Entry(adst,bd=5,font=("arial",18,"bold"))
lblmks=Label(adst,text="Enter marks",font=("arial",18,"bold"))
entmks=Entry(adst,bd=5,font=("arial",18,"bold"))
btnsave=Button(adst,text="Save",font=("arial",18,"bold"),command=f5)
btnback=Button(adst,text="Back",font=("arial",18,"bold"),command=f2)
lblrno.pack(pady=5)
entrno.pack(pady=5)
lblname.pack(pady=5)
entname.pack(pady=5)
lblmks.pack(pady=5)
entmks.pack(pady=5)
btnsave.pack(pady=5)
btnback.pack(pady=5)

#view student
vist=Toplevel(root)
vist.title("View student")
vist.geometry("500x400+400+200")
vist.configure(background="pink")
vist.withdraw()
stdata=ScrolledText(vist,width=40,height=20)
btnvback=Button(vist,text="Back",font=("arial",18,"bold"),command=f4)
stdata.pack(pady=10)
btnvback.pack(pady=10)

#update student
upst=Toplevel(root)
upst.title("Update student")
upst.geometry("500x400+400+200")
upst.configure(background="khaki1")
upst.withdraw()
lblrno1=Label(upst,text="Enter rno",font=("arial",18,"bold"))
entrno1=Entry(upst,bd=5,font=("arial",18,"bold"))
lblname1=Label(upst,text="Enter name",font=("arial",18,"bold"))
entname1=Entry(upst,bd=5,font=("arial",18,"bold"))
lblmks1=Label(upst,text="Enter marks",font=("arial",18,"bold"))
entmks1=Entry(upst,bd=5,font=("arial",18,"bold"))
btnsave1=Button(upst,text="Save",font=("arial",18,"bold"),command=f9)
btnback1=Button(upst,text="Back",font=("arial",18,"bold"),command=f10)
lblrno1.pack(pady=5)
entrno1.pack(pady=5)
lblname1.pack(pady=5)
entname1.pack(pady=5)
lblmks1.pack(pady=5)
entmks1.pack(pady=5)
btnsave1.pack(pady=5)
btnback1.pack(pady=5)

#delete student
delst=Toplevel(root)
delst.title("Delete student")
delst.geometry("500x400+400+200")
delst.configure(background="plum1")
delst.withdraw()
lblrno2=Label(delst,text="Enter rno",font=("arial",18,"bold"))
entrno2=Entry(delst,bd=5,font=("arial",18,"bold"))
btnsave2=Button(delst,text="Delete",font=("arial",18,"bold"),command=f11)
btnback2=Button(delst,text="Back",font=("arial",18,"bold"),command=f12)
lblrno2.pack(pady=5)
entrno2.pack(pady=5)
btnsave2.pack(pady=5)
btnback2.pack(pady=5)



root.mainloop()