#!/usr/bin/env python
# -*- coding:utf-8 -*-
#liuhao

try:
    names=['alex','liuhao']
    names[sasa]
except IndexError as e:
    print(e)
except Exception as e:
    print(e)
    exit()
else:
    print('什么错都没有')
finally:
    print('无论有没有错都执行')

print('keep going')
