card_list = []


def show_menu():
    print("*" * 50)
    print("欢迎使用【名片管理系统】v1.0")
    print()
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print()
    print("0.退出系统")
    print("*" * 50)


def add_cards():
    name_str = input("姓名：")
    tel_str = input("电话:")
    qq_str = input("QQ:")
    address_str = input("邮箱:")
    card_dict = {"name": name_str,
                 "tel": tel_str,
                 "qq": qq_str,
                 "address": address_str}
    card_list.append(card_dict)
    print("添加成功")


def show_all():
    if len(card_list) > 0:
        print("-" * 50)
        # 打印表头
        for head in ["姓名", "电话", "QQ", "邮箱"]:
            print(head, end="\t\t")
        print("")
        # 打印分割线
        print("=" * 50)
        for card_dict in card_list:
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],
                                            card_dict["tel"],
                                            card_dict["qq"],
                                            card_dict["address"]))
    else:
        print("没有名片")
        return


def search_cards():
    print("*" * 50)
    print("搜索名片")
    find_name = input("请输入查询人的姓名：")
    for card_dict in card_list:

        if card_dict["name"] == find_name:

            # 打印表头
            for head in ["姓名", "电话", "QQ", "邮箱"]:  # 注意此种形式
                print(head, end="\t\t")
            print("")
            # 打印分割线
            print("=" * 50)
            #           for card_dict in card_list:   #注意这里不能再用遍历要不然会有两个结果
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name"],  # 直接打印就可以
                                            card_dict["tel"],
                                            card_dict["qq"],
                                            card_dict["address"]))
            print("-" * 50)
            deal_card(card_dict)  # 减少一个函数的代码量，传递给另一个函数去对查询的个人信息进行处理
            break
    else:
        print("查无此人")


def deal_card(card_dict):
    """
    :param card_dict: 将上面字典的信息交给另一个函数来对个人信息进行处理
    """
    action_str = input("请选择你的操作"
                       "[1]修改 [2] 删除[0]返回上级菜单")
    if action_str == "1":
        card_dict["name"] = input_card_info(card_dict["name"], "请输入姓名：")
        card_dict["tel"] = input_card_info(card_dict["tel"], "请输入电话：")
        card_dict["qq"] = input_card_info(card_dict["qq"], "请输入qq：")
        card_dict["address"] = input_card_info(card_dict["address"], "请输入邮箱：")
        print("%s名片修改成功" % card_dict["name"])

    elif action_str == "2":
        card_list.remove(card_dict)
        print("删除成功")
def input_card_info(dict_value, tip_message):
    """
    输入名片信息
    :param dict_value: 字典原有值
    :param tip_message: 输入提示信息
    :return: 如果输入，返回输入内容，否则返回字典原有值
    """
    # 1.提示用户输入内容
    result = input(tip_message)
    if len(result) > 0:
        return result  # 要学会对return的理解运用
    else:
        return dict_value
