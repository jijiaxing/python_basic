#题目：输入三个整数x,y,z，请把这三个数由小到大输出。
num_list= []
for m in range(1,4):
    num = input("请输入数字：")
    num_list.append(num)
i=0
while i < len(num_list):
    j=i
    while j<len(num_list):
        if num_list[i] < num_list[j]:
            temp = num_list[i]
            num_list[i]=num_list[j]
            num_list[j]=temp
        j+=1
    i+=1
print(num_list)