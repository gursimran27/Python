# canvas->use to create a complex layout/structure
from tkinter import*

root = Tk()
root.geometry("700x700")
root.title("Canvas")


# !first create canvas
# ct = Canvas(root , bg="aqua" , height=400 , width=400 )
# ct.pack()

# # now in that canvas we can create diff shapes
# # syntax->ct.create_....(x0,y0,x1,y1,options)
# ct.create_arc( 350 , 350 , 250 ,250, fill="green" , extent=300)

# ct.create_line(30 , 200 , 100 , 100 , fill="purple")

# ct.create_oval(50 , 250 , 150 , 400 , fill="pink")

# ct.create_arc(20, 50, 190, 240, start=0, extent=110, fill="red")

# ct.create_rectangle(200 , 10 , 350 , 100,fill="blue")





# ! image display using pillow library using canvas
# # first pip install pillow
# from PIL import Image,ImageTk #PIL->python image library
# img = ImageTk.PhotoImage(Image.open("./OIP.jpg"))
# ct.create_image(0,0,image=img)






# # ! to display multiline text
# def func():
#     rt=tx.get("1.0","end-1c")#get method is used to retrieve the content of the text widget,1.0->first charater,end-1c last charater
#     print("text sunmitted successfully->" , rt)

# lb = Label(root, text="multiline text")
# lb.pack()
# tx = Text(root)
# tx.pack()
# btn = Button(root , text="submit",fg="purple",command=func)
# btn.pack()






# ! to display multiline text using scrollbar
from tkinter import scrolledtext

def func():
    rt=tx.get("1.0","end-1c")#get method is used to retrieve the content of the text widget
    print("text sunmitted successfully->" , rt)

lb = Label(root, text="multiline text")
lb.pack()
tx = scrolledtext.ScrolledText(root,wrap=WORD,width=40,height=10)
tx.pack()
btn = Button(root , text="submit",fg="purple",command=func)
btn.pack()

root.mainloop()