# # import sys

# # # print(sys.argv)
# # # print("\n")
# # # # 1st argument is the name of this script, so we start from index=2


# # # argc = len(sys.argv)
# # # print(argc)

# # # for x in range(argc):
# # #     print(f"argument {x}=> {sys.argv[x]}")


# # print(sys.stdin())



# class myException(Exception):
#     def __init__(self,message):
#         self.message = message
#     def __str__(self):
#         return (repr(self))


# # assert 10<9, "not less"


# try:
#     raise myException("test")
# except myException as e:
#     print(e.message)




# import pickle

# # fileObj = open("pikle.pkl", "wb")
# # uploadData = pickle.dump(
# #     {
# #         "name" :"guri",
# #         "age":35,
# #     },
# #     fileObj
# # )

# fileObj2 = open("pikle.pkl","rb")
# print(pickle.load(fileObj2))










# print(dir("hi"))
# class test:
#     a=10
#     kjsadgpojwag=354
#     def test():
#         pass
#     pass

# obj= test()
# print(dir(obj))




help(print)