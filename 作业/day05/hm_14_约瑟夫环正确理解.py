list = []
n = int(input("请输入人数:"))
m = int(input("请输入间隔:"))
m0 = m -1
i=1
while i<n:
    list.append(i)
    i += 1
dead = m0
while len(list) > 1:
    if dead < len(list):
        list.pop(dead)
        dead += m0
        print("杀人")
        print(list)
    else:
        dead -= len(list)


