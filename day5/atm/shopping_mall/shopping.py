#liuhao
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.chdir(BASE_DIR+'\\atm')
sys.path.append(os.getcwd())
from atm.core import main
from core import logger
from core import auth

#@auth   #通过验证获取account_id
@auth.auth_api
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
        for a,i in enumerate(shop_list):        #打印购物车列表
            print(a,i[0].ljust(12,' '),i[1])
        len(shop_list)
        choice_num=input("请输入商品编号：[q/退出]").strip()  #
        if len(choice_num) == 0: continue
        if choice_num.isdigit() and int(choice_num)<len(shop_list): #判断输入的编号是数字，并且在商品列表的范围内
            choice_num=int(choice_num)
            shop_cart.append(shop_list[choice_num])     #将购买的物品加入购物车
            for i in shop_cart:
                shop_cart_money+=i[1]               #记录购物的金额
            print("您将%s加入购物车,购物车账单金额为：%s"%(shop_list[choice_num][0],shop_cart_money))
        if choice_num == 'q':   #执行退出程序
            for i in shop_cart:         #循环计算购物的总金额
                shop_cart_money+=i[1]
            for i in shop_cart:         #循环商品名称
                shop_mingcheng.append(i[0])
            set1=set(shop_mingcheng)    #去掉重复的
            for i in set1:              #统计购买商品的各类物品个数
                msg+=i+','+str(shop_mingcheng.count(i))+"个"+','+'单价为:'+str(shop_dic[i])+';' #拼接成字符串 msg

            # msg_list.append(msg)
            return msg,shop_cart_money      #将msg和总额返回给支付页面

if __name__ == '__main__':
    shop_data=shop()        #调用购物车程序
    if shop_data[1] == 0: exit()    #判断是否购物
    choice=input("是否确认付款:[y/n]")    #是否要进行付款
    if choice=='n':print("欢迎下次光临")
    elif choice=='y':   #确认付款
        msg=shop_data[0]            #切割获取msg
        shop_money=shop_data[1]     #切割获取总金额
        account_id=login()          #通过装饰器验证用户登录。获取用户信息
        if account_id is not False: #如果验证通过
             flag=main.payment_api(account_id,str(shop_money),msg)  #调用支付接口
             if flag:   #如果支付成功
                print("本次消费了 %s ,购买了:%s"%(shop_money,msg))
        else:print("欢迎下次光临")





