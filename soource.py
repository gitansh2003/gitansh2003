import tkinter as tk
from tkinter import *
def clear_all() :
 
    # whole content of entry boxes is deleted
    ic_field.delete(0, END)  
    bkg_field.delete(0, END)
    eff_field.delete(0, END)
    kr_field.delete(0, END)
   
    # set focus on the principal_field entry box 
    ic_field.focus_set()
def kr():
    ic=float(ic_field.get())
    bkg=float(bkg_field.get())
    eff=float(eff_field.get())
    kr=((ic-bkg)*1.65)/(3600*2.9*3.7*eff)
    kr_field.insert(100,kr)
if __name__ == "__main__" :
    
    root=tk.Tk()
    root.configure(background = 'light green')
   
    # Set the configuration of GUI window
    root.geometry("%dx%d" % (450, 300))
    # set the name of tkinter GUI window
    root.title("Krypton Calculator")
    root.resizable(height=0, width=0)
    l1=Label(root,text="Integrated Counts",fg="black",bg="grey")
    l2=Label(root,text="Background Counts",fg="black",bg="grey")
    l3=Label(root,text="Efficiency (in %)",fg="black",bg="grey")
    l4=Label(root,text="Krypton Activity",fg="black",bg="grey")
    l1.grid(row=1,column=0,padx=20,pady=10)
    l2.grid(row=2,column=0,padx=20,pady=10)
    l3.grid(row=3,column=0,padx=20,pady=10)
    l4.grid(row=4,column=0,padx=20,pady=10)
    ic_field=Entry(root)
    bkg_field=Entry(root)
    eff_field=Entry(root)
    kr_field=Entry(root)
ic_field.grid(row = 1, column = 1, padx = 10, pady = 10)
bkg_field.grid(row = 2, column = 1, padx = 10, pady = 10)
eff_field.grid(row = 3, column = 1, padx = 10, pady = 10) 
kr_field.grid(row = 4, column = 1, padx = 10, pady = 10)
b1 = Button(root, text = "Submit", bg = "red",fg = "black", command = kr)
b2 = Button(root, text = "Clear", bg = "red", fg = "black", command = clear_all)
b1.grid(row = 5, column = 1, pady = 10)
b2.grid(row = 6, column = 1, pady = 10)
root.resizable(False, False)
root.mainloop()