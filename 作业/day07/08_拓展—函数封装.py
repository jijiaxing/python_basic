#1.定义函数findall，实现对字符串find方法的进一步封装，
# 要求返回符合要求的所有位置的起始下标，如字符串"helloworldhellopythonhelloc++hellojava"，
# 需要找出里面所有的"hello"的位置，最后将返回一个元组(0,10,21,29)，即将h的下标全部返回出来，
# 而find方法只能返回第一个
#(字符串的find方法，返回从左往右找到的第一个符合条件的字符的下标



"""
此种方法过于针对此提，不太适合大部分呢
list=[]
list1=[]
def findall(n):
       while len(n) != 0:  #9-13行可以用string.split("hello")代替
           m = n.partition("hello")
           list.append(m[0])
           n=m[2]
       print(list)
       for i in range(0,len(list)):
           if i==0:
               list1.append(len(list[0]))
           else:
               sum = 0
               for j in list[0:i+1]:
                   if len(j) == 0:
                       index = len(j)
                   else:
                       index = len(j) + 5
                   sum += index
               list1.append(sum)
       print(list1)
n = "helloworldhellopythonhelloc++hellojava"
findall(n)
"""
"""
def findall(f_string, string):
    list_index = []
    length = len(f_string)
    num = 0
    while True:
        index = string.find(find_string)
        if index == -1:
            list_index.append(index)
            break
        else:
            list_index.append(index + num)
            num = num + (index + length)
            string = string[(index + length):]
    if -1 in list_index:
        list_index.remove(-1)
    tuple_index = tuple(list_index)
    if len(tuple_index) == 0:
        return "没有找到寻找的字符串"
    else:
        return tuple_index

find_string = "o"
old_string = "helloworldhellopythonhelloc++hellojava"
print(findall(find_string, old_string))
"""