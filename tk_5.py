import tkinter as tk
from tkinter import Menu
# !Menu-> it is a graphical element that gives a list of options to the user.

def show1():
    print("do something")

def show2():
    print('do some thing else')



root = tk.Tk()
root.geometry("500x500")
root.title("Menu")
mn=Menu(root)#create menu
root.config(menu=mn)


# *if we donot add teraoff=0 then there will be a dottet lines/minus in submenu section



# *Adding File Menu and SubMenus
fn=Menu(mn,tearoff=0,background="yellow") #tearoff prevent doted lines
mn.add_cascade(label="File", menu=fn) # add 
fn.add_command(label='do_something',command=show1,foreground="red")  
fn.add_command(label='do_something else',command=show2)  
fn.add_separator()#create line
fn.add_command(label="exit",command=root.quit)



# *Adding View Menu and SubMenus
gn=Menu(mn,tearoff=1,background="pink")
mn.add_cascade(label="View", menu=gn )#cascade means adding sub-menu
gn.add_command(label="zoom-in")
gn.add_command(label="zoom-out")
# no seperator used
gn.add_command(label="exit",command=root.quit)



# *Adding Help Menu and SubMenus
help_ = Menu(mn, tearoff=0)
mn.add_cascade(label='Help', menu=help_)
help_.add_command(label='Tk Help')
help_.add_command(label='Demo')

root.mainloop()


