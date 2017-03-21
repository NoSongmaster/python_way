#liuhao
#打印 0-9
for i in range(10):
    if i==5:
        for i in range(10):
            print("inloop:",i)
            if i ==5:
                break
        continue
    print('outloop:',i)