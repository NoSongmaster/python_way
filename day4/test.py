def msg(msg1,name,age=0,*args,**kwargs):
    """
    打印输入的所有字符串
    """
    print(msg1,name,age)
    print(kwargs)

msg('msg','name',age1='12121')