#liuhao

#import 导入
'''点的左边必须是包'''
#错误示范：import glance.db.models.register_models
import glance.db.models as e
#glance.db.models.register_models("mysql")
e.register_models("mysql")



#from ... import 导入
'''需要注意的是from后import导入的模块，必须是明确的一个不能带点，
否则会有语法错误，如：from a import b.c是错误语法
'''
from glance.db import models