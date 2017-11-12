import os
# 把某个目录下的所有文件遍历出来
def dirlist(path, allfile):# C:\\Users\\纪加兴\\Desktop\\
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:
            allfile.append(filepath)
    return allfile
print(dirlist("C:\\Users\\纪加兴\\Desktop\\", []))
ok = dirlist("C:\\Users\\纪加兴\\Desktop\\", [])
i = 0
while i < 1:
    for name in ok:
        files = open("C:\\Users\\纪加兴\\Desktop\\hellofilelist.txt","a")
        s = name+"\n"
        files.write(s)
        files.close()
    i += 1
