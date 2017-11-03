#声明一个元组，转换为列表，修改以后，再转换为元组
shift_tuple = ("xiaobai","xiaomei",18,1.75)
shift_list = list(shift_tuple)
shift_list.append("xiaohua")
shift_list.reverse()
shift_list.pop(1)
teiminal = tuple(shift_list)
print(teiminal)