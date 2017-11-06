class Houseitem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地%.2f" % (self.name, self.area)


# 创建家具
bed = Houseitem("西蒙斯", 4)
chest = Houseitem("衣柜", 2)
table = Houseitem("餐桌", 1.5)

print(bed)
print(chest)
print(table)
