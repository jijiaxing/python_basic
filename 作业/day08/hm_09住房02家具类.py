class Houseitem:

    def __init__(self,name,area):

        self.name = name
        self.area = area

    def __str__(self):

        return "[%s]占地%.2f"%(self.name,self.area)

class House:

    def __init__(self,house_type,area):

        self.house_type = house_type
        self.area = area

        #生于面积
        self.free_area = area
        #家具名称列表
        self.item_list = []
    def __str__(self):

        #python能自动的将一对括号内的代码连接在一起
        return ("户型%s\n总面积：%.2f[剩余：%0.2f]\n家具：%s"
                %(self.house_type,self.area,
                  self.free_area,self.item_list))
    def add_item(self, item):

        self.item_list.append(item.name)
        self.free_area -= item.area

        print("要添加%s"%item)

bed =Houseitem("西蒙斯",4)
chest = Houseitem("衣柜",2)
table = Houseitem("餐桌",1.5)

print(bed)
print(chest)
print(table)

#2.创建房子对象
my_home = House("两市一厅",60)

my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)
