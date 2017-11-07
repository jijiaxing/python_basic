# 定义一个People类，使用People类，创建一个mayun对象后，添加company属性，
# 值是"阿里巴巴"；创建一个wangjianling对象，添加company属性，值是"万达集团
class People:
    def __init__(self,name):
        self.name = name
        self.company = None
    def __str__(self):
        return ("我的名字是[%s],公司有【%s]"%(self.name,self.company))
mayun = People("马云")
mayun.company ="哈里巴巴"
print(mayun)
wangjianlin = People("王健林")
wangjianlin.company = "万达集团"
print(wangjianlin)
