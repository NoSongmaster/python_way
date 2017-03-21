#liuhao
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from ATM.core.auth import auth
from ATM.core.transaction import payment_api

@auth   #通过验证获取account_id
def login():
    pass
def shop():
    shop_mingcheng=[]
    shop_cart=[]
    msg=''
    msg_list=[]
    shop_list=[['iphone7',5288],
               ['mac Pro',13888],
               ['ipad mini4',2888],
               ['kindle',799],
               ['coffe',38]
               ]
    shop_dic={'iphone7':5288,
               'mac Pro':13888,
               'ipad mini4':2888,
               'kindle':799,
               'coffe':38
              }
    while True:
        shop_cart_money = 0
        print('商品_列表'.center(30,'#'))
        for a,i in enumerate(shop_list):
            print(a,i[0].ljust(12,' '),i[1])
        len(shop_list)
        choice_num=input("请输入商品编号：[q/退出]").strip()
        if len(choice_num) == 0: continue
        if choice_num.isdigit() and int(choice_num)<len(shop_list): #判断输入的编号是数字，并且在商品列表的范围内
            choice_num=int(choice_num)
            pay="\033[1;31;40m 未成功 \033[0m "
            shop_cart.append(shop_list[choice_num])
            pay='\033[1;33;47m 成功 \033[0m'
            for i in shop_cart:
                shop_cart_money+=i[1]
            print("您将%s加入购物车,购物车账单金额为：%s"%(shop_list[choice_num][0],shop_cart_money))
        if choice_num == 'q':
            for i in shop_cart:
                shop_cart_money+=i[1]
            for i in shop_cart:
                shop_mingcheng.append(i[0])
            set1=set(shop_mingcheng)
            for i in set1:
                msg+=i+','+str(shop_mingcheng.count(i))+"个"+','+'单价为:'+str(shop_dic[i])+';'

            # msg_list.append(msg)
            return msg,shop_cart_money

if __name__ == '__main__':
    shop_data=shop()
    if shop_data[1] == 0: exit()
    choice=input("是否确认付款:[y/n]")
    if choice=='n':print("欢迎下次光临")
    elif choice=='y':
        msg=shop_data[0]
        shop_money=shop_data[1]
        account_id=login()
        if account_id is not False:
            flag=payment_api(account_id,shop_money,msg)
            if flag:
                print("本次消费了 %s ,购买了:%s"%(shop_money,msg))
        else:print("欢迎下次光临")





