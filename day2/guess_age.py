#liuhao
count=0
while count<3:
    age=25
    guess_age=int(input("请尝试猜一下alex的年龄~有惊喜啊！").strip())
    if guess_age ==25:
        print("你好牛啊，真的猜出来了。你们是不是搞基呀？")
        break
    elif guess_age >25:
        print("你也太坏了，alex年纪有那么大吗？")

    elif guess_age<25:
        print("你猜的太小啦~")
    count+=1




