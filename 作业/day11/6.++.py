import os
def dirlist(path, allfile):
    filelist = os.listdir(path)
    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dirlist(filepath, allfile)
        else:
            files = open("C:\\Users\\纪加兴\\Desktop\\hellofilelist.txt", "a")
            files.write(filepath+filename+"\n")
            files.close()
dirlist("C:\\Users\\纪加兴\\Desktop\\abc\\", [])


