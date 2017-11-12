#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，
# 几个数相加有键盘控制。  
# .程序分析：关键是计算出每一项的值。  
m = int(input("请输入一个数字："))
n = int(input("请输入几个数字相加："))
sum=0
for i in range(1,n+1):
    a=str(m)
    b=a*i
    sum+=int(b)
    print(sum)
print(sum)