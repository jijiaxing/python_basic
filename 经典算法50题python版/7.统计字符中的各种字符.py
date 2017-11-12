#【程序7】   题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。  
# 数字和其它字符的个数.程序分析：利用while语句,条件为输入的字符不为 '\n '.  
a = "11123abt\t \t\t %%%%"
count=0
count1=0
count2=0
for i in a:
    if i.isdecimal():
        count+=1
    if i.isalpha():
        count1+=1
    if i.isspace():
        count2+=1
print(count)
print(count1)
print(count2)
print(len(a))
print(len(a)-count-count1-count2)