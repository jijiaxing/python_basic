#练习二：将第一题中创建的文件，复制一份，名称为 hello2.txt
file = open(r"C:\Users\纪加兴\Desktop\hello.txt")
file2 = open(r"C:\Users\纪加兴\Desktop\hello2.txt","w")


text = file.read()
file2.write(text)

file.close()
file2.close()