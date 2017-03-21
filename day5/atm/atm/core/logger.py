#!_*_coding:utf-8_*_
#__author__:"Alex Li"

'''
handle all the logging works
'''

import logging
from conf import settings

def logger(log_type):

    #create logger
    logger = logging.getLogger(log_type)    #创建一个实例，设置日志类型
    logger.setLevel(settings.LOG_LEVEL)     #设置日志级别


    # create console handler and set level to debug
    ch = logging.StreamHandler()        #屏幕输出
    ch.setLevel(settings.LOG_LEVEL)     #输出日志级别

    # create file handler and set level to warning
    log_file = "%s/log/%s" %(settings.BASE_DIR, settings.LOG_TYPES[log_type])   #拼接日志位置
    fh = logging.FileHandler(log_file)  #文件记录
    fh.setLevel(settings.LOG_LEVEL)     #文件记录级别
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')   #日志记录格式

    # add formatter to ch and fh
    ch.setFormatter(formatter)  #屏幕输出日志格式
    fh.setFormatter(formatter)  #文件日志记录格式

    # add ch and fh to logger
    logger.addHandler(ch)   #
    logger.addHandler(fh)

    return logger   #返回设置好日志实例
    # 'application' code
    '''logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')'''

