#liuhao

#共三个版本
#1、低级版，实现调用函数进行密码验证
# def auth(func):
#     def warrper(*args):
#         name=input('input name: ')
#         passwd=input('input passwd: ')
#         if name=='alex' and passwd=='123':
#             print('登录成功')
#             func(*args)
#         else:
#             print('登录失败')
#             return ''
#     return warrper
#
# @auth
# def hello(msg):
#     print("hello ",msg)
# hello('Alex')
#中级版(有参装饰器)，实现采用不同方式进行用户验证
# def auth_deco(auth_type='file'):
#     def auth(func):
#         def warrper(*args,**kwargs):
#             name=input('input name: ')
#             passwd=input('input passwd: ')
#             if auth_type=='file':
#                 if name=='alex' and passwd=='123':
#                     print('登录成功')
#                     func(*args,**kwargs)
#                 else:
#                     print('登录失败')
#             elif auth_type=='ldap':
#                 print("用户验证ldap")
#                 func(*args,**kwargs)
#         return warrper
#     return auth
# auth_type = 'ldap'
# @auth_deco(auth_type)
# def hello(msg):
#     print("hello ",msg)
# auth_type = 'ldap'
# hello('alex')

#高级版，验证一次，不需要一直验证。（）
# import functools
# def auth_deco(auth_type='file'):
#     #@functools.        被装饰函数，help()。还是自己的帮助信息
#     def auth(func):
#         def warrper(*args,**kwargs):
#             '''
#
#             :param args:
#             :param kwargs:
#             :return:
#             '''
#             if auth_type=='file':
#                 name = input('input name: ')
#                 passwd = input('input passwd: ')
#                 if name=='alex' and passwd=='123':
#                     print('登录成功')
#                     func(*args,**kwargs)
#                 else:
#                     print('登录失败')
#             elif auth_type=='ldap':
#                 print("用户验证ldap")
#                 func(*args,**kwargs)
#         return warrper
#     return auth
# auth_type = 'ldap'
# @auth_deco(auth_type)
# def hello(msg):
#     print("hello ",msg)
# @auth_deco(auth_type)
# def hey(msg):
#     print('hey:',msg)
# auth_type = 'ldap'
# hello('贺磊')
# hey('贺磊')

