import os


# print(os.listdir())
# print(os.getcwd())

if not os.path.exists('./test'):
    os.mkdir("C:\\Users\\Dell\\OneDrive\\Desktop\\New folder\\test")

# os.rename("./test/temp {i+1}", "./test/mian 1")

for i in range(100):
    # os.mkdir(f"./test/mian {i+1}")
    # os.rename(f"./test/mian {i+1}" , f"./test/temp {i+1}")
    os.rmdir(f"./test/mian {i+1}")