from tkinter import*
# !linking windows

root = Tk()
root.geometry("400x400")
root.title("linking tabs")

def tab1():
    def tab2():
        lab1.destroy()
        btn1.destroy()
        lab2 = Label(root,text="Second Window",bg="blue",font=("Time_New_Roman",24))
        lab2.pack()    
        def back():
            lab2.destroy()
            btn2.destroy()
            tab1()
        btn2= Button(root,text="Back",bg="red",command=back,width=10)
        btn2.pack(side=BOTTOM)


    lab1 = Label(root, text="Parent Window",bg="blue", font=("Time_New_Roman",24))
    lab1.pack()
    btn1= Button(root,text="Next",bg="red",command=tab2,width=10)
    btn1.pack(side=BOTTOM)


tab1()

root.mainloop()