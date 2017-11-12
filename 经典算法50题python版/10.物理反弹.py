#【程序10】 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半
#再落下，求它在   第10次落地时，共经过多少米？第10次反弹多高？

def high(h):
    i=1
    sum=0
    while i<=10:
        sum+=h
        h= h/2
        i+=1
    print(sum)
    print(h)
high(100)