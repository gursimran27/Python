# a = 10
# _a = 30
# print(_a)

# name = 'rajiv kumar'
# print(name)

# age =4
# Age =9
# print(age)
# print(Age)


# a=('guri','rajiv')
# print(a)
# list = list(a)
# print(list)


# ! LIST
# a=['guri','rajiv','guri']
# a.append('aman')
# print(a)

# a.insert(1,2)
# print(a)
 
# b=['ani','the']
# a.extend(b)
# print(a)

# a.pop(3)
# print(a)

# a.remove('the')
# print(a)

# print(b)
# b.clear()
# print(b)

# del a[1]
# print(a)


# a.sort()
# print(a)

# a.sort(reverse=True)
# print(a)

# print(len(a))

# a = list(('hlo','hola'))
# print(type(a))

# a.reverse()
# print(a)


# print(a.count('guri'))


# !TUPLE
# a= tuple(('hello','world','bye'))
# print(a)

# li = list(a)
# li.append('amandeep')
# a= tuple(li)
# print(a)


# print(10+5)


# !SETS ->unordred ,no duplicate
# a={2,1,3,8,1}
# print(a)

# print(a)

# b={11,2,'hi'}


# b.add('23')
# print(b)

# b.discard('hi')
# print(b)


# a.update(b)
# print(a)


# print(a)
# a.clear()
# print(a)

# a.pop()
# a.pop()
# a.pop()
# print(a)


# print(a.union(b))


# print(a.difference(b))


# print(a.intersection(b))



# !dictionary
# a= {
#     "firstName" : "Gursimran",
#     'lastName' :"Singh",
#     "rollno" : 2124129
# }
# print(a)

# # using constructor
# b =dict(name = "JohnDoe", age = 36, country = "Norway")

# *methods
# print(a.keys())


# print(a.values())


# print(a["rollno"])


# print(b.get("age"))
# b["age"] = 21 #keyValue pair
# print(b.get("age"))


# a["collage"] = "ikgptu" #keyValue pair
# print(a)


# i = a.items() #item method will return a list of tuple of its key-Value pair
# print(i)


# print(b.update({"age" : 2}))
# print(b)


# print(b.pop("age"))
# print(b)


# a["hi"] = 10
# print(a)
# a.popitem() #iw
# print(a)


# del a
# print(a)
# del a["rollno"]
# print(a)



# c = a.copy()
# print('c=>',c)


# newDic = dict.fromkeys(["name" , "last"] , True) #fromkeys method is used to create a new dictinory, it is having 2 arguments i.e specified keys and value same for all keys ....if no key is defined them it is none
# newDic = dict.fromkeys(range(1,10) , True)
# print(newDic)

# ! conditions
# a=20
# b= int(input("enter a number"))
# if b>a:
#     print("your number is greater than our num")
# else:
#     print("your number is smaller than our number")



# if b%2 == 0 :
#     print("your number is even")
# elif b%2 != 0:
#     print("thats an odd number")



# c= int(input("enter second number"))
# d= int(input("enter third number"))

# if( b > c and b > d):
#     print(b , "is greater")
# elif( c > b and c > d):
#     print(c, "is greater")
# else:
#     print(d, "is greater")


# if ( b>=90):
#     print("You get A grade")
# elif( b>=70 and b<90):
#     print("You get B grade")
# elif( b>=35 and b<70):
#     print("You get C grade")
# else:
#     print("Sorry, You failed")




# prime number without for loop in python?
# a= int(input("enter a number"))
# i = True
# if( a==1 or a==2 ):
#     print("not a prime number")
# else:
#     for x in range(2,a):
#         if a%x == 0:
#             print("not a prime number")
#             i = False
#             break
        
# if i == True:
#     print("prime number")



# to print range of prime num



# !loops->repitation of statement
# while loops -> executes until the condition is true
# for loop
# for x in range(1,11):
#     print(5*x)

# for x in range(55,5,-5):
#     print(x)

# for x in range(5,51,5):
#     print(x)

# for x in range(11,111,11):
#     print(x)


# num=int(input("Enter the number"))
# for i in range(1,11):
#     print(num,'x',i,'=',num*i)
    
# def printTable(i):
#     print(num,'x',i,'=',num*i)
    
# i =1
# while i<=10:
#     printTable(i)
#     i+=1
    


    
# i=0
# for x in range(1,num+1):
#     i+=x
# print(i)



#!star
# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end="")
#     print(" ")


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print(" ")


# square
# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print(" ")




# rectangle
# for i in range(2):
#     for j in range(5):
#         print("*",end=" ")
#     print(" ")





# !math modules
# import math


# a=(1,2,-1,5)
# print(min(a))
# print(max(a))
# b=2.7
# print(math.ceil(b))
# print(math.floor(b))
# print(math.sqrt(100))
# print(math.isqrt(100))
# print(math.pow(2,3))
# print(math.log10(100))
# print(max(2,-2))



# !test

# a = int(input("enter a number"))
# b = int(input("enter a number"))
# c = int(input("enter a number"))
# d = int(input("enter a number"))

# li = (a,b,c,d)
# print(max(li))



# 2
# a = int(input("enter a number"))
# b = int(input("enter a number"))
# c = int(input("enter a number"))

# average = ((a+b+c)/3)

# print('u got=',average,"%")
# if(average>=40):
#     print('Congrats, for ur success')
# else:
#     print('!SORRY, try again')


# 4
# a=["ram","sham","kaka","guri","Rajiv"]
# b = (input('enter a name'))

# i=True
# for x in a: # we can also use if(b in a)
#     if(b.lower()==x.lower()):
#         print('yes your name is included in list')
#         i=False
#         break


# if i==True:
#     print("your name is not in list")







# !functions
# it is a block of code which is given a name and by using its name can be called multiple times 

# syntax
# def funcName ():
#     body

# calling
# function()


# def func():
#     print('hi')

# func()

# parameters-> those values which are given to a func at the time of defination of that func
# arguments-> are the values that are passed to that func during func call

# types of args in func->
# 1)positional 
# 2)keyword 
# 3)default 
# 4)length keyword


#1) positional args-> those args which are defined in the func are always same position at the time of func call those args that are first at the time of func defination and also given first func call 
# eg-> def add(x,y):
    # sum = x+y
    # print("sum",usm)

# add(x=4,y=7)


#2)keyword args=> those args in which values are defined at the time of func def are always same when func is called the only diff b/w positional and keyword args is that we can change position of elements in keyword args but we cannot change number of elements in func
# eg=>
# def func(name , age):
    # print(f"my name is {name}, "my age is {age}")


# func(name="sohan" , age=61)


#! fString-> formating string
# !a=20
# !print(f"my age is {20}")

# 3) default args=> those args in which we give some default val inside func def...while calling that func with no args then that default val is used and if user give some args during func call then that args is used instead of default val
# eg->
# def func(age=88):
#     print(f"age={age}") 

# func()
# func(6)



# def show(name="india"):
#     print("i belongs to",name)


# show("usa")
# show()




#4) Length keyword->those args when we donnot know how many values are passing to the func ..in such case we use length keword args (by astrisk before the parameters so it catchs multiple args at time of func call)
# eg->
# def func(*args):
#     sum=0
#     for x in args:
#         sum+=x
#     return sum

# print(func(1,2,3,4,5))
        





# def func(x="soory u didnot enter any number"):
#     print(f"x={x}")

# if data:
#     func(data)
# else:
#     func()








# import tkinter as tk

# # Create the parent window
# root = tk.Tk()
# root.title("Parent Window")

# # Create the child window
# child = tk.Toplevel(root)
# child.title("Child Window")

# # Position the child window relative to the parent window
# child.geometry("+200+200")

# # Show the windows
# root.mainloop()













import tkinter as tk

# Create the parent window
root = tk.Tk()
root.title("Parent Window")

# Create the first child window
child1 = tk.Toplevel(root)
child1.title("Child Window 1")
child1.geometry("+100+100")

# Create the second child window
child2 = tk.Toplevel(root)
child2.title("Child Window 2")
child2.geometry("+300+300")

# Create the third child window
child3 = tk.Toplevel(root)
child3.title("Child Window 3")
child3.geometry("+500+500")

# Show the windows
root.mainloop()

