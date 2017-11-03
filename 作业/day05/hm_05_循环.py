#声明一个字典，结合笔记中3.1中的图片练习觉用的操作
xiaohua = {"name":"花花",
           "age":18,
           "height":150,
           "weight":185}
xiaomei= {"name":"草草",
           "age":19,
           "height":180,
           "weight":186}
#xiaohua.pop("name")
#print(xiaohua)
xiaohua.update(xiaomei)
print(xiaohua)
#xiaohua.keys()
#print(xiaohua.keys())
xiaohua.setdefault("tizhong",18)
print(xiaohua)