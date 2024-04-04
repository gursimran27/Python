# write a program to interchange the first and last element in a list
# list = [1,2,3,4,5]
# temp = list[0]
# list[0]= list[4]
# list[4]=temp
# print(list)



#! WAP to find the max of two numbers?
# a=10
# b=20

# if(a>b):
#     print('a is max')
# else:
#     print('b is max')


# !WAP to reverse a string 
# s = 'world'
# print(s[::-1])
# print(s[-1:-6:-1])


# !write a program in python to print even length word in a string?
# s='gursimran'
# print(s[1:9:2])

# !create a list of tuples from a given list having number and its cube in each tuple?
 
# list = [1,2,3]
# result=[]
# for i in range (len(list)):
#     result.append((i+1)**3)

# print(result)


# !write a program a remove items from a set
# set={4,1,4,2}
# set.remove(1)
# print(set)

# !write a program to find the size of a set and max and min in set
# s = set((2,9,-1,4,2))
# print(len(s))
# print(max(s))
# print(min(s))


#! write a python program to swap two elements in a string

# a="gursimran"
# b= "python programming is fun!"
# temp = a
# a=b
# b = temp
# print(a) 
# print(b) 

# write a program to remove all the duplicate from a string 
s = 'gursimran'








def func(x="soory u didnot enter any number"):
    print(f"x={x}")


try:
    data = int(input("enter an integer number"))
    func(data)

except ValueError:
    func()


