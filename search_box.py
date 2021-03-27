from tkinter import *
import pandas as p
def newwin():
    window=Tk()
    window.title('search Engine ....')
    window.resizable(width=False,height=False)
    window.geometry('400x200')
    window.iconbitmap('empo.ico')

    def searching():
        employer = search1.get()
        search1.delete(0,END)
        employes = p.read_csv('employes_data.csv')
        mana = Toplevel(window)
        mana.geometry('400x200')
        mana.iconbitmap('empo.ico')
        la = Label(mana,text=employes.loc[employes['Name']==employer]).pack()
        mana.mainloop()

    head=Label(window,text='Search Employee',font='timesnewroman 18 bold')
    head.grid(row=0,column=0)

    search1=Entry(window)
    search1.grid(row=2,column=0,pady=30,padx=20)

    btn=Button(window,text='Search',command=searching)
    btn.grid(row=2,column=1)


    window.mainloop()
