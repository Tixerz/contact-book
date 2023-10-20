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


def add_contact_menu():
    root = tk.Tk()
    root.geometry("300x100")
    root.mainloop()

root =  tk.Tk()
root.geometry("800x500")
add_button = tk.Button(root , text= "Add" , command=add_contact_menu)
add_button.place(x=700 , y= 350)

entry = tk.Entry(root ,width=50)
entry.pack(padx= 10 , pady= 30)
search_button = tk.Button(root , text= "Search" )
search_button.place(x=600 , y=30)
root.mainloop()