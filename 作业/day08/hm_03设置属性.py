class Cat:
    def __init__(self,name):
        self.name =name

    def eat(self):
        print("%s爱吃鱼"%self.name)
    def drink(self):
        print("%s要喝水"%self.name)

tom = Cat("大蓝猫")
tom.drink()
tom.eat()
print(tom)
