#liuhao
#三级菜单数据：一共就三层
info={'北京市':{
    '朝阳区':{
        "三里屯":{'这里有很多美女，三里屯？'},
        "海底世界":{'工体富国海底世界，有好多鱼吧'},
        "梨园":{' 京城梨园，这是什么地方？'}},
    '大兴区':{
        "西红门":{'人们说这里都是郊区了，你看呢？西红门？万达？还好吧~'},
        "大商场":{'去过的地方，汇聚,西红门最大，宜家'},
        "鸿坤广场":{'鸿坤广场,好吃的，韩式烤肉，珠宝拍卖'}},
    '昌平区':{
        "单身公寓":{'还是郊区，都是小房子，单身公寓。我来了2月'},
        "大家的感觉":{'一说昌平就想到了落后的郊区。。'}},
    '海淀区':{
        "中关村":{'没去生活工作过，有中关村，好流弊'},
        "西二旗":{'西二旗，我原来在西三旗啊'}}
},
    '内蒙古自治区':{
        '呼和浩特市':{
            "我学习的地方":{'哈哈内蒙首府啊~学习生活。'}},
        '包头市': {
            "我没去过的地方":{'内蒙第二大城市,感觉发展比呼和浩特好'}},
        '巴彦淖尔市':{
            "我成长的地方":{'长大的地方。美丽的湖泊'}}
    },
    '广东省':{
        '东莞市':{
            "帮助":{'好像很出名，不知道它为什么出名~~'}},
        '广州市':{
            "简介":{'又是首府，因为东莞他沾光了。不然我都不知道哦~'}}
    }
}
#开始执行程序。通过循环控制菜单的返回。
while True:
    for i in info:
        print(i)
    choice1=input("请输入你的选择进入的省份[exit\退出]")
    if len(choice1)==0:continue
    if choice1 in info:
        while True:
            for i in info[choice1]:
                print(i)
            choice2 = input("请输入你的选择进入的城市[q\返回\exit\退出]")
            if choice2 in info[choice1]:
                while True:
                    for i in info[choice1][choice2]:
                        print(i)
                    choice3=input('请输入你的选择[q\返回exit\退出]')
                    if choice3 in info[choice1][choice2]:
                        while True:
                            for i in info[choice1][choice2][choice3]:
                                print(i)
                            choice4=input("[q\返回exit\退出]")
                            if choice4=='q':
                                break
                            elif choice4=='exit':
                                exit('执行退出，欢迎下次登陆')
                    if choice3=='q':
                        break
                    elif choice3=='exit':
                        exit('执行退出，欢迎下次登陆')
            elif choice2 == 'q':
                break
            elif choice2=='exit':
                exit('执行退出，欢迎下次登陆')
    elif choice1 == 'exit':
        exit('执行退出，欢迎下次登陆')
