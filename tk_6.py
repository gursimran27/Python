
#!Selection widgets->those widgets which provide a graphical display option to a user. it include
# 1)combobox->made of combo of enter-box
# 2)list box
# 3)radio button
# 4)checkbutton

def show():
    print(cb.get(),v.get())


from tkinter import*
from tkinter.ttk import Combobox

root=Tk()
root.geometry("500x500")



#*--------------combo-box--------------------
l1=Label(root,text="select your place:")
l1.pack()
cb=Combobox(root,values=["Punhab","haryana","UP","Jk","Bihar"])
cb.pack()



#*--------------list-box--------------------
l2=Label(root,text="select your Technology:")
l2.pack()
li=Listbox(root,selectmode=SINGLE)#selectmode=MULTIPLE
li.insert(1,"C")
li.insert(2,"C++")
li.insert(3,"JS")
li.insert(4,"Java")
li.insert(5,"Swift")
li.insert(6,"Python")
li.insert(7,"React")
li.pack()



#*--------------radio-button--------------------

l3=Label(root,text="select your gender:")
l3.pack()
v=IntVar()
v.set(2)#for default select
rbtn_male = Radiobutton ( root , text='Male', value=1,variable= v)
rbtn_male.pack()
rbtn_female =Radiobutton ( root,text ='Female',value=2,variable=v)
rbtn_female.pack()
rbtn_other =Radiobutton ( root,text ="Other",value=3,variable=v)
rbtn_other.pack()



#*--------------check-button--------------------

l4 = Label(root,text="role")
l4.pack()
c1 = Checkbutton(root,text="Student")
c1.pack()
c2 =Checkbutton(root,text="Teacher")
c2.pack()





btn=Button(root, text="submit",command=show,width=20)
btn.pack()

root.mainloop()