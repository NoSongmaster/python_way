#liuhao
import login.login
@login.login.auth_user
def shop():
    shop_cart=[]
    shop_list=[['iphone7',5288],
               ['mac Pro',13888],
               ['ipad mini4',2888],
               ['kindle',799],
               ['coffe',38]
               ]
    while True:
        #输入工资并进行判断，
        salary=input("请输入工资:").strip()
        if  len(salary)==0:continue
        try:
            salary=int(salary)
            break
        except ValueError as e:
            print("输入错误，重新输入！例：12000")
            continue

    while True:
        print('商品_列表'.center(30,'#'))
        for i in enumerate(shop_list):
            print(i[0],i[1][0].ljust(12,' '),i[1][1])
        len(shop_list)
        choice_num=input("请输入商品编号：[q/退出]").strip()
        if len(choice_num) == 0: continue
        if choice_num=='q':break
        if choice_num.isdigit() and int(choice_num)<len(shop_list): #判断输入的编号是数字，并且在商品列表的范围内
            choice_num=int(choice_num)
            pay="\033[1;31;40m 未成功 \033[0m "
            if salary >shop_list[choice_num][1]:        #判断工资是否足够支付购买物品
                shop_cart.append(shop_list[choice_num][0])
                salary-=shop_list[choice_num][1]
                pay='\033[1;33;47m 成功 \033[0m'
            print("您购买%s%s,剩余金额为：%s"%(shop_list[choice_num][0],pay,salary))

        else:
            print('输入错误')
            continue
    print(shop_cart)
    set1=set(shop_cart)
    print("购物车已购商品：")
    for i in set1:
        print(i,"\033[1;34;43m",shop_cart.count(i),"个","\033[0m")
    #print("打印购物列表\033[1;34;43m %s \033[0m"%shop_cart)

shop()