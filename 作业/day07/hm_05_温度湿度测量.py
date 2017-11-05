def measure():

    print("开始测量")
    temp = 39
    wetness = 10
    print("测量结束")

    return temp,wetness
result = measure()
print(result)
#再利用元祖返回温度的同时，也能够返回湿度,括号可以省略
#注意：变量的数量需要和元组中的数量保持一致
result = temp,wetness=measure()