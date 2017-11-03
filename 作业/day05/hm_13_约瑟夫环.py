import random
list=[]
n = int(input("请输入一个数："))
while n!= 0:
    list.append(n)
    n -= 1
k = random.randint(0,len(list)-1)
m = random.randint(k+1,len(list)-1)
list.pop(m)
keep = m - k
print(keep)
while len(list)>1:
    i=0

    while i!=keep:
        i += 1
        if len(list)>keep:
            list.pop(i)
            print(list)

    if len(list)<=keep:

        count=keep-len(list)

        list.pop(count%len(list))
        print(list)
