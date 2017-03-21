#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
#修改配置文件
import configparser
#生成一个config对象
config=configparser.ConfigParser()
#读取配置文件
config.read('example.ini')
#创建一个新的配置选项
# config.set("DEFAULT",'name','liuhao')  #两种设置的方式
config['DEFAULT']['name']='liuhao'
#将配置重新写入到配置文件
with open('example.ini', 'w') as configfile:
    config.write(configfile)