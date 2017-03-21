#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao
#读取配置文件
import configparser
config=configparser.ConfigParser()
#使用内置的方法去读取配置文件
config.read('example.ini')
value1=config.get('DEFAULT','compression')
value2=config.get('topsecret.server.com','host port')
print(value1)
print(value2)
