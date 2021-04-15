from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("600x600")
Label(root , text="Country you wanna travel?").pack()
country = ["Australia" , "USA" , "Japan" , "England" , "Italy"]
var = StringVar()
new_var = var.set("nowhere")

def travel():
    tmsg.showinfo("Lets travel" , f"We are booking your flight to {var.get()}\n Wish you a happy Journey :)")

for x in range(5):
    Radiobutton(root , text = country[x] , variable=var,value=country[x]).pack()

Button(root , text="Let's travel" , command = travel).pack()
root.mainloop()