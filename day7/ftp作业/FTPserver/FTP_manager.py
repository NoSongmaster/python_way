#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
import json,os,sys,hashlib
def run():
    #user_database = os.path.dirname(__file__)+'/'+'users'+'/'
    user_database=os.path.dirname(os.path.abspath(sys.argv[0]))+'/'+'users'+'/'
    print(user_database)
    while True:
        md5=hashlib.md5()
        name=input('create your acount:')
        if len(name)==0:continue
        elif os.path.isfile(user_database+name):
            print('用户已经存在')
            continue
        passwd=input('create your passwd:')
        if len(passwd)==0:continue
        passwd=passwd.encode(encoding='utf-8')
        md5.update(passwd)
        quota_size=input('enter your quota_size[b]:')
        if len(quota_size)==0:continue
        user_dir = os.path.dirname(os.path.abspath(sys.argv[0]))+'/'+'user_file/'+name
        os.mkdir(user_dir)
        user_dict={
                   'name':name,
                   'passwd':md5.hexdigest(),
                   'quota_size':int(quota_size),
                   'use_quota':0
                   }

        with open(user_database+name,'w',encoding='utf-8') as f:
            f.write(json.dumps(user_dict))
        break


if __name__ == '__main__':
    run()
