
#注意事项：如果父类中存在同名的属性或者方法时尽量避免使用多继承
#python中针对类提供了一个内置属性，可以查看顺序__mro__
class A:
    def test(self):
        print("t")
class B:
    def demo(self):
        print("d")
class C(A,B):

    pass
c= C()
c.test()
c.demo()
print(C.__mro__)