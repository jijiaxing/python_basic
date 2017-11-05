demo_list = [1,2,3]
print("定义列表后的内存地址%d"%id(demo_list))

demo_list.append(999)
demo_list.pop(0)
demo_list.remove(2)
demo_list[0] = 10
print("修改数据后的内存地址%d"%id(demo_list))

demo_dict = {"name":"小明"}
print("定义字典后的内存地址%d"%id(demo_dict))
demo_dict["age"] = 18
demo_dict.pop("name")
demo_dict["name"] = "老王"
print("修改之后的内存地址%d"%id(demo_dict))