#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import shelve
path= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)
from modules.campus_class import Campus
from conf.setting import DATABASE
from modules import view
def creat_campus(): # 初始化数据库
    if os.path.exists(DATABASE['path']+'.bak') \
            and os.path.exists(DATABASE['path']+'.dat') \
            and os.path.exists(DATABASE['path']+'.dir'):
        pass
    else:

        def creat_campus():    # 创建初始化学校
            f = shelve.open(DATABASE['path'])
            campus1 = Campus('北京','中国北京')
            f[campus1.school_name] = campus1
            print(campus1.course_dict)
            campus2 = Campus('上海','中国上海')
            f[campus2.school_name] = campus2
            f.close()

if __name__ == '__main__':
    creat_campus()
    view.run()


