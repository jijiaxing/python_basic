#练习 1 ：声明一个列表，将笔记中1.2 列表常用操作中列出的方法都执行一遍
name = ["xiaobai","xiaoming","xiaohua"]

name2 = ["xiaomei","xiaoda"]

name.append("yida")
print(name)
name.extend(name2)
print(name)
print(name2.index("xiaomei"))
name.insert(1,"mengniu")
print(name)
name.remove("xiaobai")
print(name)
name.pop()
print(name)
name.sort()
print(name)
#name.clear()
#print(name)
name.reverse()
print(name)
