class Gun:

    def __init__(self,modle):

        #1.枪的型号
        self.modle = modle

        #2.子弹的数量
        self.bullet_count = 0
    def add_bullet(self,count):

        self.bullet_count += count
    def shoot(self):

        #1.判断子弹数量
        if self.bullet_count <= 0:
            print("[%s]没有子弹了..."%self.modle)
            return
        #2.发射子弹-1
        self.bullet_count -= 1
        #3.提示发射信息
        print("[%s]图图图...[%d]"%(self.modle,self.bullet_count))

class Soldier:

    def __init__(self,name):

        self.name = name

       #新并没有枪记住不知道属性是什么的时候就用none
        self.gun = None

    def fire(self):

        #1.判断是否有枪  is用于判断两个变量引用对象是否同一个 ==用于判断引用变量的直是否相等
        if self.gun is None:   #  注意别丢：标记
            print("[%s]还没有枪"%self.name)
            return
        #2.高喊口号
        print("冲啊///[%s]"%self.name)

        #3.装天子弹

        self.gun.add_bullet(50)
        #4.
        self.gun.shoot()

#1.创建强对象
ak47 = Gun("Ak47")
#ak47.add_bullet(50)
#ak47.shoot()

#2.创建许三多
xusanduo = Soldier("许三多")
xusanduo.gun = ak47
xusanduo.fire()
print(xusanduo.gun)