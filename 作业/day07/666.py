# 请输入正方形的边长，用户输入边长后，打印 正方形，然后，显示 提示
"""
def square(n):
    if n == 1:
        print("*")
    else:
        i = 1
        num=n
        while i <= n:
            if i == 1 or i == n:
                j = 1
                while j <= n:
                    print("*", end="  ")
                    j += 1
                print("")
            else:
                print("*"+"  "*()+"*")
            i += 1
square(5)
"""#有问题
def square(n):
    if n == 1:
        print("*")
    else:
        i = 1
        while i <= n:
            if i==1 or i==n:
                print("*  "*5)
            else:
                a=len("*  "*5)
                print("*"+" "*(a-2*len("*  ")+2)+"*")
            i += 1
def triangle(n):
        i = 1
        while i <= n:
            if i==1:
                print(" "*+(2*n-2)+"*")
            elif i<n:
                print(" "*+(2*(n+1-i)-2)+"*"+" "*(4*(i-1)-1)+"*")
            else:
                print("*   "*n)
            i += 1
#square(5)
triangle(8)