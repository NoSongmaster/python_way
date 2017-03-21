#liuhao
konglist=[]
list =[
    ['iphone7', 6500],
    ['macbook', 12000],
    ['pythonbook', 66],
    ['bike', 999],
    ['coffee', 31]
]

salary = int(input("your salary>>:"))

while True:
    print("product list".center(50, "-"))
    for i in enumerate(list):
        print(i[0],".",i[1][0],i[1][1])
    shop_num=input("输入商品编号：")
    if shop_num.isdigit():
        shop_num = int(shop_num)
        shop_one = list[shop_num]
        if shop_one[1] > salary:
            print("you need %s" % (shop_one[1] - salary))

        else:
            salary -= shop_one[1]
            konglist.append(shop_one)
            print("added %s into you shopping catr , you current balance is %s" % (shop_one[0], salary))
    elif shop_num == 'quit':
        print("ni have bought below products:")
        for i in konglist:
            print(i)
        print("余额",salary)
        break



