import pickle as pk
import tkinter as tk
import os

class contact():
    def __init__(self,name,number):
        self.name = name
        self.number = number

    def edit(self,new_name , new_number):
        self.new_name = new_name
        self.new_number = new_number

    def save(self):
        with open(f"/Contacts/{self.name}.con" , "wb") as file:
            pk.dump(contact(self.name , self.number) , file)

    def delete(self):
        os.remove(f"/Contacts/{self.name}.con")

storage = []
showed_list = ["rayan                    92347923749237492374349387"]

 #we r gonna save all the data here
#for item in os.listdir("/Contacts/"):
   # storage.append(pk.load(f"/Contacts/{item}"))
#showed_list = ["sex    92834"] #its what we are going to show in the main listbox



root =  tk.Tk()
root.geometry("800x500")

con_list = tk.Listbox(root, width=100 , height= 300)
con_list.place(x= 10 , y= 100)

def refresh():
    global root
    global con_list
    global showed_list
    con_list = tk.Listbox( root , width=100 , height= 300)
    for item in showed_list :
        con_list.insert('end' , item)
    con_list.place( x= 10 , y= 100)
refresh()

def add_contact_menu():
    
    root = tk.Tk()
    tk.Label(root,text="name:").place(x=10 , y =10)
    tk.Label(root,text="number:").place(x=10 , y= 40)
    name_entry = tk.Entry(root )
    name_entry.place(x=100 , y=15)
    root.geometry("300x100")
    root.mainloop()
    refresh()
add_button = tk.Button(root , text= "Add" , command=add_contact_menu)
add_button.place(x=700 , y= 350)


entry = tk.Entry(root ,width=50)
entry.pack(padx= 10 , pady= 30)

search_button = tk.Button(root , text= "Search" , width=5 , height=2 )
search_button.place(x=600 , y=30)


root.mainloop()