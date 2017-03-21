#liuhao
'''logging模块'''
'''
debug()
info()
warning()
error()
critical
'''
import logging
#最简单用法
logging.warning("user [alex] attempted wrong password more than 3 times")
logging.critical("server is down")
#日志保存到log文件中，日志保存级别
logging.basicConfig(filename='123.log',filemode='a',level=logging.INFO)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

