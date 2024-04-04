
# self->this pointer
# __init__->constructor

# class school:
#     board = "CBSE" #class attribute shared by all instances of classes
#     def __init__(self,schoolName): #constructor
#         self.schoolName = schoolName
#     def display(self):
#         print(self.schoolName," ",self.board)
    


# obj = school("DPS")
# obj2 = school("St Joseph's Convent School")
# obj.display()
# obj2.display()
        

# !single inheritance
# class stu(school):
#     def __init__(self, schoolName , name):
#         self.name = name
#         school.__init__(self , schoolName) # it will call the constructor of school class

#     def show(self):
#         print(self.name)
#         super().display()


# obj1 = stu("SGH", "aman")
# obj1.show()


# ! multilevel inheritance
# class stuID(stu):
#     def __init__(self, schoolName, name , id):
#         self.id = id
#         stu.__init__(self ,schoolName, name)
    
#     def show(self):
#         print(self.id)
#         super().show()
#         super().display()


# obj = stuID("DPS", "guri" , 2124129)
# obj.show()





# !multiple inheritance
# class Company:
#     def __init__(self, compName ):
#         self.compName = compName

#     def show(self):
#         print(self.compName)


# class Car:
#     def __init__(self, model):
#         self.model= model
    
#     def show1(self):
#         print(self.model)
 

# class year(Company , Car):
#     def __init__(self, year , model ,  company):
#         Company.__init__(self ,company)
#         Car.__init__(self , model )
#         self.year = year
#     def dispaly_all(self):
#             print(self.year , self.compName , self.model)
#             super().show()
#             self.show1()


# a= int(input("enter the year of manufacture"))
# b=input("enter the car name")
# c=input("enter the company name")
# obj = year(a, b , c )
# obj.dispaly_all()
# obj.show1()



# WAP to create vehical class and display the attri milage , car name , speed...
# class Vehical:
#     def __init__(self):
#         name = input("enter car name")
#         speed = int(input("enter the max speed of ur car"))
#         milage = float (input ("Enter your current mileage "))
#         self.carName = name
#         self.speed = speed
#         self.milage = milage

#     def showDetails(self):
#         print(f"car name={self.carName}  max speed of car {self.speed} milage of ur car{self.milage}")


# obj = Vehical()
# obj.showDetails()