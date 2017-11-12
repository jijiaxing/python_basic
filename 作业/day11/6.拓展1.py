##将桌面所有的文件的完整名称，写入 hello3.txt ,考虑桌面中子文件夹中的情况
#			完整名称即，路径加名称


import os
location = os.getcwd()
list_all = os.listdir("C:\\Users\\纪加兴\\Desktop\\")
print(list_all)
for x in list_all:
    path = location+"/"+x
    print(path)
    file = open("hello3.txt", "a")
    file.write(path + "\n")
    file.close()



