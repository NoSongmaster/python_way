#liuhao
import pickle
'''pickle反序列化'''
f=open("account.db",'rb')
#acount=pickle.loads(f.read())
account=pickle.load(f)
print(account)
f.close()