#liuhao
'''
ATM 执行程序
'''

import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core.main import run

if __name__ == '__main__':
    run()