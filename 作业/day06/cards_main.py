from day06 import cards_tools
while True:
    cards_tools.show_menu()
    action = input("请输入你的选择：")
    if action in ["1","2","3"]:

        if action == "1":
            cards_tools.add_cards()
        elif action == "2":
            cards_tools.show_all()
        else:
            cards_tools.search_cards()
    elif action == 0:
        print("欢迎再次使用")
        break
    else:
        print("输入错误，请重新选择")