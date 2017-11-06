class Person:

    def __init__(self,name,weigh):

        #self.属性=行参
        self.name = name
        self.weigh = weigh
    def run(self):

       print("%s爱跑步"%self.name)
       self.weigh -= 0.5

    def eat(self):
        print("%s是赤火"%self.name)
        self.weigh += 1

    def __str__(self):

        return "我的名字叫%s体重%.2f"%(self.name,self.weigh)

xiaoming = Person("小明",75.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

xiaomei=Person("xiaomei",45)

xiaomei.eat()
xiaomei.run()

print(xiaomei)
print(xiaoming)