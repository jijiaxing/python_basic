class Cat:
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫要喝水")


#创建猫对象
tom = Cat()
tom.eat()
tom.drink()

print(tom)
#将16进制地址变成10进制地址
addr = id(tom)
print("%d"%addr)

"""
地址格式16>10
0x7f29895d2b00
139816374971136
"""