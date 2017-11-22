 # 1.定义一个函数 input_pwd() ，函数中提示用户输入密码，要求密码为 6位 数字，
	# 	如果用户输入不是数字，抛出异常 “非法字符，请输入6 位数字”，
	# 	如果密码长度不为 6 ，抛出异常 "密码长度不对，请输入 6 位数字"


def input_pwd():
    pwd = input("请输入密码：")
    if len(str(pwd)) != 6:

        ex = Exception("密码长度不够，请输入六位数字")
        raise ex
    if not pwd.isdecimal():
        raise Exception("非法字符")
# try:
#     input_pwd()
# except ValueError:
#     print("非法错误，请输入六位数字")

input_pwd()