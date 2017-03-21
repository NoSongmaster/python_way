#liuhao
#生成一个初始的账户数据，把这个数据，存成一个，以这个账户id为文件名的文件，放在account目录。就行了。程序自己会去这里找
#{""id":12345,money": 24947, "quota": "15000", "name": "liuhao", "status": 0, "password": "123456"}
import os,sys,json

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
account_dir=BASE_DIR+"\\db\\accounts\\"
def make_account(account_id,name,password): #创建一个新的用户
    account_date={"id":account_id,"money":15000,"quota":15000,"name":name,"password":password,"status":0}
    with open(account_dir+str(account_id),'w',encoding='utf-8') as f:
       f.write(json.dumps(account_date))

if __name__ == '__main__':
    make_account(123456,"test",123456)



