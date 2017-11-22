#练习七：实现文件夹的复制功能，
import os
def dirlist(path, dirName):
    if not os.path.isdir(dirName):#判段abc文件夹是否存在
        os.mkdir(dirName)
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        copypath = os.path.join(dirName, filename)
        if os.path.isdir(filepath):
            os.mkdir(copypath)
            dirlist(filepath, copypath)
        else:
            file = open(filepath, "rb")
            file2 = open(copypath, "wb")
            file2.write(file.read())
            file.close()
            file2.close()
dirName = dirlist(r"F:\666\\", "F:\\abc\\")
print(dirName)


