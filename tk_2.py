# step 1->import tkinter
from tkinter import*


# gemeotry method is use to place widgets on window screen
# gemeotry method-> 3 types
# 1)Pack()->use to display widgets on windows side eg-> side=LEFT/RIGHT/TOP/BOTTOM
# 2)grid()->use to represent widget on tabular form/grid(row and column) structure eg=>label.grid(row=0,column=1)
# 3)place()->use to represent widgets on the basis of x and y axis. here we use x and y

# widget-> is a graphical element that a user can interact with like label,button and these are stored in tcl/tk

# !login form
root = Tk()
root.geometry("500x500")
root.configure(bg="brown")
root.title("Login Page")

def show(): # to switch btw windows
    root1 = Tk()
    root1.title("submit")
    root1.geometry("400x400")
    lab = Label(root1,text="submmitted successfully")
    lab.grid()

l = Label(root , text="Login Form",)
l.pack()

lab1 = Label(root , text="username:" , fg="red")
lab1.place(x=150 , y=50)
e1 = Entry(root , bg="grey")
e1.place(x=220,y=50)


lab2 = Label(root , text="password:" , fg="red")
lab2.place(x=150 , y=100)
e2 = Entry(root , bg="grey")
e2.place(x=220,y=100)


lab3 = Label(root , text="email:" , fg="red")
lab3.place(x=150 , y=150)
e3 = Entry(root , bg="grey")
e3.place(x=220,y=150)


lab3 = Label(root , text="phone number:" , fg="red")
lab3.place(x=150 , y=200)
e3 = Entry(root , bg="grey")
e3.place(x=250,y=200)


btn1 = Button(root , text="Submit" ,fg="green" , command=show)
btn1.place(y=270 , x=200)

btn2 = Button(root , text="Reset" , fg="green")
btn2.place(y=270 , x=300)


root.mainloop()



# ! syllabus
# Label
# Button
# entry box
# geometry method
# Canvas
# selection widgets
# frames
# scrollbar
# Menu
# qr code Generator
# image display or use as a background
# data base connectivity


# mysql->download communnity server->400mb->setup