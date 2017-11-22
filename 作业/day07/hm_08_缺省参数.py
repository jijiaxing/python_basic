# 定义函数时，可以给某个参数指定一个默认值，具有默认值得参数就叫做缺省函数
# 调用函数时，如果没有传入缺省参数的值，则在函数内部使用定义函数时指定参数的默认值
# 函数的缺省参数，将常见的值设置为参数的缺省值，从而简化函数的电泳
# 列如：对列表排序的方法
"""
gl_num_list = [6,3,9]
gl_num_list.sort()
print(gl_num_list)
#只有当需要降序排序时，才需要传递“reverse"参数
gl_num_list.sort(reverse=True)
print(gl_num_list)
"""
# 指定函数的缺省函数
# 在参数后面使用赋值语句，可以指定参数的缺省值
"""
def print_info(name,gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s是%s"%(name,gender_text))
    """


# 提示：
# 缺省参数，需要使用最常见的值作为默认值
# 如果一个参数的值不能确定，则不应该设置默认值，具体的数值再点用函数时，由外界传递
# 缺省参数的注意事项：
# 1.缺省参数的定义位置
#    必须保证带有默认值得缺省在参数列表末尾
# 2.调用带有多个缺省参数的函数
#   再调用函数时，如果有多个缺省参数，需要指定参数名，
# 这样解释器才能够知道其对应关系
def print_into(name, title="", gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s%s是%s" % (title, name, gender_text))


# 提示;在指定缺省函数的默认值时，应该使用最常见的值作为默认值

print_into("小明")
print_into("老王", title="班长")
print_into("小美", gender=False)
