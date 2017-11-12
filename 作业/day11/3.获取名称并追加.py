#练习三：获得桌面所有的文件的名称，追加写入 hello.txt
#		注意：不考虑 子文件夹中的文件
import os

list_str = os.listdir(r"C:\Users\纪加兴\Desktop")

file2 = open(r"C:\Users\纪加兴\Desktop\hello.txt","a")

file2.write(str(list_str))

file2.close()
