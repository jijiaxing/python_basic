# 在控制台输入n组个人信息，每个人有姓名和年龄，将信息存入字典中，将字典存入列表。
# 遍历列表，查找并打印某个人的年龄
i = 0
mlist = []
while i < 2:
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    dict = {}
    dict.setdefault("姓名", name)
    dict.setdefault("年龄", age)
    i += 1
    mlist.append(dict)
print(mlist)
nam1 = input("请输入名字：")
for dict2 in mlist:
    if dict2.get("姓名") == nam1:
        print(dict2.get("年龄"))
print(mlist)
