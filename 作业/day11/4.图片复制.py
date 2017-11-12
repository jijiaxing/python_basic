#练习四：用代码实现，将桌面的某一图片文件，复制一份。（图片自己打，名称自己定）
#提示：图片是二进制文件，读写时要用 rb  wb  如  f1 = open("xxx.jpg","rb")   f2 = open("xxx2.jpg","wb")
file = open("C:\\Users\\纪加兴\\Desktop\\dog.jpg","rb")
file2 = open("C:\\Users\\纪加兴\\Desktop\\dog2.jpg","wb")


text = file.read()
file2.write(text)

file.close()
file2.close()