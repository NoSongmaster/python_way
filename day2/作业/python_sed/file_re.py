#liuhao
#liuhao
import sys,re
#先做一个备份，file.old
try:
    flag=[]      #标记进行替换的行号
    value_old=sys.argv[1]
    value_new=sys.argv[2]
    file_name=sys.argv[3]
    with open(file_name, 'r', encoding='utf-8') as f_new:
        with open(file_name+'.old','w+',encoding='utf-8')as f_old:
            for i in f_new:
                f_old.write(i)
    with open(file_name+'.old','r',encoding='utf-8') as f_old:
        with open(file_name, 'w+', encoding='utf-8') as f_new:
            for num,key in enumerate(f_old):
                print(re.match(value_old,key).group())
                if re.match(value_old) is True:
                    #print("正在替换第%s行,原内容为：%s" % (num+1, key))
                    key=re.sub(value_old,value_new,key)
                    flag.append(num+1)
                f_new.write(key)
    if len(flag)==0:
        print('文件内没有匹配到%s字段,未进行替换'%sys.argv[1])
    else:print('脚本对以下行号进行了替换：',flag)
except IndexError as e:
    print('''
    [使用方法：python %s argv[1] argv[2] argv[3] ]

    范例： python %s old_str new_str filename
    注意：请切换到，程序文件所在目录执行。
    '''%(sys.argv[0],sys.argv[0]))
except FileNotFoundError as e:
    print("文件%s不存在,请确认"%sys.argv[3])

