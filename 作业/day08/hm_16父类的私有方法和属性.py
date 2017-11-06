class A():
    def __init__(self):

        self.num1 = 100
        self.__num2 = 200

    def __test(self):

        print("私有方法%d%d"%(self.num1,self.__num2))
    def test(self):
        print("共有方法%d"%self.__num2)
class B(A):

    def demo(self):

        #1.调用弗雷私有属性，不能调用父亲的私有属性或方法
        #print("私有属性%d"%self.__num2)
        print("子类方法%d"%self.num1)

#创建子类对
b = B()
print(b)
b.demo()
print(b.num1)
b.test()
#外界不鞥访问对象私有属性和方法