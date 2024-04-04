from tkinter import*
from tkinter import messagebox
import random

#! message-box Widget=> it is used to dispaly message-box in the python application.
# syntax-> import message-box
# messagebox.function_name(title,message)
# it is of 7 types of function_name
#1) showinfo(): Show some relevant information to the user.
#2)showwarning(): Display the warning to the user.
#3) showerror(): Display the error message to the user.
#4)askquestion(): Ask question and user has to answered in yes or no.
#5)askokcancel(): Confirm the user’s action regarding some application activity.
#6) askyesno(): User can answer in yes or no for some action.
#7)askretrycancel(): Ask the user about doing a particular task again or not.

root = Tk()
root.geometry("600x600")
root.title("messagebox")




l1=Label(root,text="message-box",font="50")
l1.pack()

def showinfo():
    messagebox.showinfo("showinfo","Information")

def showwarning():
    messagebox.showwarning("showwarning", "Warning")
    
def showerror():
    messagebox.showerror("showerror", "Error")
    
def askquestion():
    a=messagebox.askquestion("askquestion", "do you like this")
    if(a=="yes"):
        messagebox.showinfo("askquestion", "you choose yes")
    else:
        messagebox.showinfo("askquestion", "you choose NO")
   
def askokcancel():
    a= messagebox.askokcancel("askokcancel", "Want to exit?")
    if a>0:
       root.destroy()
    else:
       pass
    
def askyesno():
    a=messagebox.askyesno("askyesno", "Want to continue")
    if a>0:
       pass
    else:
       root.destroy()
    
def askretrycancel():
   a= messagebox.askretrycancel("askretrycancel", "Try again?") 
   if a>0:
       pass
   else:
       root.destroy()





def randomNumber():
    list1 = [1, 2, 3, 4, 5, 6, 7]
    rd = random.choice(list1)
    print(rd)
    return rd






def test():
    rd = randomNumber() 
    print(f"rd={rd}")
    if rd==1:
        showinfo()
    elif rd==2:
        showwarning()
    elif rd==3:
        showerror()
    elif rd==4:
        askquestion()
    elif rd==5:
        askokcancel()
    elif rd==6:
        askyesno()
    elif rd==7:
        askretrycancel()


# btn = Button(root,text="showinfo",font="20",bg="aqua",fg="red",bd=9,command=showinfo)
# btn.pack()

# btn = Button(root,text="showwarning",font="20",bg="aqua",fg="red",bd=9,command=showwarning)
# btn.pack(side=LEFT)

# btn = Button(root,text="showerror",font="20",bg="aqua",fg="red",bd=9,command=showerror)
# btn.pack(side=RIGHT)

# btn = Button(root,text="askquestion",font="20",bg="aqua",fg="red",bd=9,command=askquestion)
# btn.pack(side=BOTTOM)

# btn = Button(root,text="askokcancel",font="20",bg="aqua",fg="red",bd=9,command=askokcancel)
# btn.pack()

# btn = Button(root,text="askyesno",font="20",bg="aqua",fg="red",bd=9,command=askyesno)
# btn.pack()

# btn = Button(root,text="askretrycancel",font="10",bg="aqua",fg="red",bd=9,command=askretrycancel)
# btn.pack()



btn = Button(root,text="Button",font="20",bg="aqua",fg="red",bd=9,command=test)
btn.pack()



root.mainloop()