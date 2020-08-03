from tkinter import *
from backend import Database
 
database=Database("password_data.db")
 
class Window(object):
 
    def __init__(self,window):
 
        self.window = window
 
        self.window.wm_title("Password Manager")
 
        l1=Label(window,text="User")
        l1.grid(row=0,column=0)
 
        l2=Label(window,text="Password")
        l2.grid(row=0,column=2)
 
        l3=Label(window,text="Website")
        l3.grid(row=0,column=4)
        
        self.user_text=StringVar()
        self.e1=Entry(window,textvariable=self.user_text)
        self.e1.grid(row=0,column=1)
 
        self.password_text=StringVar()
        self.e2=Entry(window,textvariable=self.password_text)
        self.e2.grid(row=0,column=3)
 
        self.website_text=StringVar()
        self.e3=Entry(window,textvariable=self.website_text)
        self.e3.grid(row=0,column=5)

        self.list1=Listbox(window, height=7,width=75)
        self.list1.grid(row=2,column=0,rowspan=6,columnspan=4)
 
        sb1=Scrollbar(window)
        sb1.grid(row=2,column=4,rowspan=6)
 
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)
 
        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)
 
        b1=Button(window,text="View all", width=12,command=self.view_command)
        b1.grid(row=2,column=5)
 
        b2=Button(window,text="Search entry", width=12,command=self.search_command)
        b2.grid(row=3,column=5)
 
        b3=Button(window,text="Add entry", width=12,command=self.add_command)
        b3.grid(row=4,column=5)
 
        b4=Button(window,text="Update selected", width=12,command=self.update_command)
        b4.grid(row=5,column=5)
 
        b5=Button(window,text="Delete selected", width=12,command=self.delete_command)
        b5.grid(row=6,column=5)
 
        b6=Button(window,text="Close", width=12,command=window.destroy)
        b6.grid(row=7,column=5)
 
    def get_selected_row(self,event):
        index=self.list1.curselection()[0]
        self.selected_tuple=self.list1.get(index)
        self.e1.delete(0,END)
        self.e1.insert(END,self.selected_tuple[1])
        self.e2.delete(0,END)
        self.e2.insert(END,self.selected_tuple[2])
        self.e3.delete(0,END)
        self.e3.insert(END,self.selected_tuple[3])

    def view_command(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)
 
    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.user_text.get(),self.password_text.get(),self.website_text.get()):
            self.list1.insert(END,row)
 
    def add_command(self):
        database.insert(self.user_text.get(),self.password_text.get(),self.website_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.user_text.get(),self.password_text.get(),self.website_text.get()))
 
    def delete_command(self):
        database.delete(self.selected_tuple[0])
 
    def update_command(self):
        database.update(self.selected_tuple[0],self.user_text.get(),self.password_text.get(),self.website_text.get())
 
window=Tk()
Window(window)
window.mainloop()

