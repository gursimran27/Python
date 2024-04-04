# import *->mean all
from tkinter import*

# create a window obj
root = Tk()

# add widgets
root.geometry("500x300")
root.title("tetsting tkinter")
root.configure(bg="brown")

label = Label(root , text="firstName" , bg="aqua")
label.pack(side="left") # it is a gemetric method

btn = Button(root , text="submit" , fg="blue" , bg="orange")
btn.pack(side="bottom")


# call main loop
root.mainloop()