#6.定义一个函数，接受三个参数，分别为字符串s、数值a1、数值a2，
# 将字符串s从下标a1开始的a2个字符删除，并把结果返回，a2默认值为0
def character(s,a1,a2=0):
     new_str1 = s[0:a1]
     new_str2 = s[(a1+a2):]
     new=new_str1+new_str2
     return new

a ="abcdefg"
print(character(a,2,2))