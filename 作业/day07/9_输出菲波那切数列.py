#使用递归的方法打印出前n个斐波那契数列  1,1,2,3,5,8 从第3个数开始，每一个数都是前二个之和
#	使用递归时，当n=1时，应当返回一个数值，作为结束条件，而不是继续返回本身

def num(n):
    if n == 1:
        return 1
    elif n==2:
        return 1
    else:
        return num(n-1)+num(n-2)
    print(n)
print(num(5))


    # for i in range(1,n+1):
    #     print(num(i))
print(num(3))