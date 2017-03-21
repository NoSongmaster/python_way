#liuhao
#注意.下面 遵循字典的格式
import configparser
#生成config对象
config = configparser.ConfigParser()
#写配置文件第一级['DEFAILT']
config["DEFAULT"] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
#
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
#将配置写入文件中
with open('example.ini', 'w') as configfile:
    config.write(configfile)

