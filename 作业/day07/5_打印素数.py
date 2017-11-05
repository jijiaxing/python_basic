#5.定义一个函数，打印出n以内的所有的素数
def prime(n):
    list1 = []
    for i in range(0,n+1):
        list = []
        for j in range(1,i+1):
            if i % j == 0:
                list.append(j)
        if len(list)==2:
            list1.append(i)

    return  list1
print(prime(30))

