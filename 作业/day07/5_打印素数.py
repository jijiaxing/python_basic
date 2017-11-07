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

"""

def is_su_shu(num):
  
    # 当一个数只能被　１　和　他自己整数时，他就是　素数
    # :param num:
    # :return:
    
    chu_shu = 2
    while chu_shu < num:
        if num % chu_shu == 0:  #判断中间有没有2—num中有没有可以被整除的如果有就不是素数
            # 说明整除了
            return False
        chu_shu +=1
    # 循环结束，说明都没有被整除，则是素数
    return True
def find_all_sushu(n):
    
    # 打印　Ｎ　以内的　所有的　素数
    # :param n:
    # :return:
  
    sushu = []
    while n > 0:
        if is_su_shu(n):
            sushu.append(n)
        n -= 1
    print(sushu)
find_all_sushu(100)

"""