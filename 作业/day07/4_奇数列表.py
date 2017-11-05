# 4.定义一个函数，返回由n(包含n)以内的奇数或者偶数组成的列表，默认返回全是奇数的列表
def odd_even(n, listbox=True):
    list1 = []
    if listbox:
        for i in range(0, n+1):
            if i % 2 != 0:
                list1.append(i)
    else:
        for i in range(0, n+1):
            if i % 2 == 0:
                list1.append(i)
    return list1

print(odd_even(5,False))
