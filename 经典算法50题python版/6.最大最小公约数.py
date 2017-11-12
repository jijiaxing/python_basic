#题目：输入两个正整数m和n，求其最大公约数和最小公倍数。  
# 程序分析：利用辗除法。  
# *在循环中，只要除数不等于0，用较大数除以较小的数，将小的一个数作为下一轮循环的大数，
# *取得的余数作为下一轮循环的较小的数，如此循环直到较小的数的值为0，返回较大的数，
# *此数即为最大公约数，最小公倍数为两数之积除以最大公约数。
def gongbeishu(m,n):# 24 32
    # if n!=0:
    #     gongbeishu(n, m % n)
    # else:
    #     print(m)
    # return m
   #print(n)
    while n != 0:
        gongbeishu(n,m%n)
        break
    if n == 0:
        print(m)
    return   m           #注意返回
def fonfbei(m,n):
    a = gongbeishu(m,n)
    print((m*n)/a)

fonfbei(24,32)


