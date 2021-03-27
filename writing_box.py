from tkinter import *
import pandas as p
# classes
def newwin():
    # new window
	screen = Tk()
	screen.geometry('250x150')
	screen.title('Entry...')
	screen.iconbitmap('empo.ico')


	head=Label(screen,text='Employes Entery',font ='timesnewroman 10 bold')
	head.grid(row=0,column=2)

	L1 = Label(screen,text='Name')
	L1.grid(row=1,column=1)
	E1 = Entry(screen,bd=2)
	E1.grid(row=1,column=2)

	L2 = Label(screen,text='Father name')
	L2.grid(row=3,column=1)
	E2 = Entry(screen,bd=2)
	E2.grid(row=3,column=2)

	L3 = Label(screen,text='Age')
	L3.grid(row=5,column=1)
	E3 = Entry(screen,bd=2)
	E3.grid(row=5,column=2)

	L4 = Label(screen,text='Contact')
	L4.grid(row=7,column=1)
	E4 = Entry(screen,bd=2)
	E4.grid(row=7,column=2)

	# functions
	def added():
		name = E1.get()
		fathername = E2.get()
		salary = E3.get()
		contact = E4.get()
		E1.delete(0,END)
		E2.delete(0,END)
		E3.delete(0,END)
		E4.delete(0,END)
		employe = {'Name': [str(name)],'Father name': [str(fathername)],'salary': [str(salary)],'contact no.': [str(contact)]}
		df = p.DataFrame(employe)
		df.to_csv('employes_data.csv', mode='a', header=False)
		mana = Toplevel(screen)
		mana.geometry('400x200')
		mana.iconbitmap('empo.ico')
		Label(mana, text ='employe added').grid(row=0,column=0)
		Label(mana,text=df).grid(row=1,column=0)
		mana.mainloop()
	submit =Button(screen,text='Add Employe',command = added)
	submit.grid(row=9,column=2)

	screen.mainloop()