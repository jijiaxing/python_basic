"""
1.定义函数findall，实现对字符串find方法的进一步封装，要求返回符合要求的所有位置的起始下标，
如字符串"helloworldhellopythonhelloc++hellojava"，
需要找出里面所有的"hello"的位置，最后将返回一个元组(0,10,21,29)，
即将h的下标全部返回出来，而find方法只能返回第一个
    (字符串的find方法，返回从左往右找到的第一个符合条件的字符的下标)

"""

ss = "helloworldhellopythonhelloc++hellojava"

"""
思路　一：先找到第一个符合要求的子字符串的下标，存入列表，然后将，字符串ss 剪切
        如　ss 字符串，第一个符合的下标为　0 剪切以后的字符串为：worldhellopythonhelloc++hellojava
        然后循环查找，并剪切

"""


def method_1(ss):
    index_list = []

    #
    cut_len = 0
    while True:

        index = ss.find("hello")
        if index == -1:
            break

        index_list.append(index + cut_len)

        cut_len += index + 5

        ss = ss[index + 5:]

    print(index_list)


"""
思路二　：使用　find 方法，并指定开始查找的下标

"""

def method_2(ss):
    index_list = []

    #
    cur_start = 0
    while True:

        index = ss.find("hello", cur_start)
        if index == -1:
            break

        index_list.append(index)

        cur_start = index + 5

    print(index_list)


method_1(ss)
method_2(ss)
