from tkinter import *
import search_box as sb
import writing_box as wb
def Main():
	# making window
	mainwindow = Tk()
	menubar = Menu(mainwindow)
	mainwindow.iconbitmap('empo.ico')
	mainwindow.geometry('300x300')
	mainwindow.config(bg='purple')
	mainwindow.title('employes data')
	# declearing some functions
	def employeadd():
		wb.newwin()
	def employesearch():
		sb.newwin()
	#making help button on menu
	fuckedupmenu = Menu(menubar,tearoff =0)
	fuckedupmenu.add_command(label='how can we help?',command = employesearch)
	menubar.add_cascade(label='help',menu=fuckedupmenu)
	menubar.add_cascade(label='about us')
	#image
	photo = PhotoImage(file = 'logo.png')
	label = Label(image = photo,bg='purple').place(relx=0.28,rely=0.05)
	#buttons
	b1 = Button(text = 'add employes',fg = 'black',bg ='white',font='Ariel 12 bold',command=employeadd)
	b2 = Button(text = 'search employes',fg = 'black',bg ='white',font='Ariel 12 bold',command=employesearch)
	b1.place(relx=0.35,rely=0.7)
	b2.place(relx=0.35,rely=0.9)
	#windows main loop
	mainwindow.config(menu=menubar)
	mainwindow.mainloop()
Main()
