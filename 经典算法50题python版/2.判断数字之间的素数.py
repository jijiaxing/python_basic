#题目：判断101-200之间有多少个素数，并输出所有素数。  
##程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，  
#则表明此数不是素数，反之是素数。
def is_su_shu(num):
    chu_shu = 2
    while chu_shu < num:
        if num % chu_shu == 0:
            return False
        chu_shu +=1
    return True
sushu = []
for num in range(2,100):
    if is_su_shu(num):
        sushu.append(num)
print(sushu)
