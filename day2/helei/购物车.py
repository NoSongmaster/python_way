import os,time
count = 0
buy = 0
shopping_cart = []
lists = [
    ['iphone7',6500],
    ['macbook',12000],
    ['pythonbook',66],
    ['bike',999],
    ['coffee',31]
]
while True:
    user = input("请输入你的用户名：")
    passwd = input("请输入你的密码：")
    with open("lock") as lock:
        for line in lock:
            if user in line:
                exit("你已经被锁定，请联系管理员")
    with open("file") as f:
        for line in f:
            if user in line:
                user_msg = line.strip()
            else:
                exit("没有你的用户信息，去办个会员卡吧！")
    _user_msg = eval(user_msg)
    _user = _user_msg["name"]
    _passwd = _user_msg["passwd"]
    _msg = _user_msg["msg"]
    last_list = _msg[1]
    if _user == user and _passwd == passwd:
        print("你好：%s，欢迎你！" %user)
        print(str.center("上次的购物清单", 50))
        for i, v in enumerate(last_list):
            print("%s\t%s\t%s" % (i, v[0], v[1]))
        print("您的会员卡里还有%s"%_msg[0])
        yue = int(_msg[0])
        break
    elif _passwd != passwd:
        print("密码错误，请重新输入")
        count += 1
    if count == 3:
        with open("lock","w") as lock:
            lock.write(user+"\n")
while True:
    print("Shop_list".center(30,'-'))
    for i, v in enumerate(lists):print("%s\t%s\t%s" % (i, v[0], v[1]))
    num = input("What do you want to buy:")
    if str.isdigit(num):
        num = int(num)
        if len(lists) > num >= 0:
            shopping = lists[num]
            if shopping[1] > yue:
                print("your need %s￥"% (shopping[1] - yue))
            else:
                yue -= shopping[1]
                print("Buy success,add %s ,you have %s￥" % (shopping[0], yue))
                shopping_cart.append(shopping)
                buy += shopping[1]
    elif num == "quit":
        print("Your shopping car list:".center(30,'-'))
        for i, v in enumerate(shopping_cart):
            print("%s\t%s\t%s" % (i, v[0], v[1]))
        print("Your shopping cost %s￥" % buy)
        new_msg = '''['%s', %s]'''%(yue,shopping_cart)
        old_msg = '''%s'''%_msg
        with open("file") as f,open ("file_new","w") as f_new:
            for line in f:
                if user in line:
                    line = line.replace(old_msg,new_msg)
                f_new.write(line)
        os.remove("file")
        os.rename("file_new","file")
        print("三秒后退出程序...")
        time.sleep(5)  # 哈哈哈
        break

