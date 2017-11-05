#如果在函数中需要修改全局变量，需要使用global进行

num = 10
def demo1():
    print("demo1"+"-"*50 )
    #global关键字，告诉编辑器num是一个全局变量
    global num
   
    num = 100
    print(num)
def demo2():
    print("demo2"+"-"*50)
    print(num)
demo1()
demo2()
print("over")