#练习五：用代码实现，在桌面创建一个文件夹 test ,
# 然后将桌面所有的 txt 复制到 test 文件夹中，（不考虑子文件夹中的txt 文件）
import os

os.mkdir("C:\\Users\\纪加兴\\Desktop\\test")
list_str = os.listdir(r"C:\Users\纪加兴\Desktop")

for i in list_str:
    if i[-4:] == ".txt":
        file = open("C:\\Users\\纪加兴\\Desktop\\%s"%i)   #注意不要放在上面
        file2 = open("C:\\Users\\纪加兴\\Desktop\\test\\%s"%i, "w")
        file2.write(file.read())
        file.close()
        file2.close()






