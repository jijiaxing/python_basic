#练习七：实现文件夹的复制功能，
import os
os.mkdir("F:\\abc")
dirName = ""
def dirlist(path, dirName):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            os.mkdir("F:\\abc\\%s" % filename)
            dirlist(filepath, filename)
        else:
            file = open(filepath, "rb")
            file2 = open("F:\\abc\\%s\\%s" %(dirName,filename), "wb")
            file2.write(file.read())
            file.close()
            file2.close()
    return dirName
dirName = dirlist(r"F:\666\\",dirName)
print(dirName)


