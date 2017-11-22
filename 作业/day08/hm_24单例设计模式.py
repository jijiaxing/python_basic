"""
设计模式
    设计模式是前人工作的总结和提炼，被人们广泛流传的设计模式是针对某一特定问题的成熟解决方案
    使用设计模式是为了可重用代码，让代码更容易被其他人理解，保证代码可靠性
单例设计模式
    目的--让类创建的对象，在系统中只有唯一的一个实例
    每一次执行类名（）返回的对象，内存地址是相同的
"""
"""
__new__方法
    1.在内存中为对象分配空间
    2.返回对象的引用
———init__方法
    1.对象初始化
    2.定义实力属性
解释器在获得对象的引用后，将作为第一个参数，传递给__init__方法
重写__new__方法一定要返回return super().__new__(cls)
否则得不到分配了的空间的引用，就不会调用对象的初始化方法
__new__是一个静态方法，在调用时需要主动传递cls参数

"""

class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        #1.创建对象时，NEW方法自动點用
        print("创建对象分配内存")
        #2.为对象分配空间
        instance = super().__new__(cls)   #new是静态方法
        #3.返回对象的引用
        return instance
    def __init__(self):
        print("播放器初始化")


player = MusicPlayer()
