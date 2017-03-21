#liuhao

#序列化： 内存---> 字符串
#反序列化：字符串--->内存
'''pickle序列化'''
import pickle
account={
    'id':575163273,
    "credit":15000,
    "balance":8000,
    "expire_date":"2020-5-20",
    "password":"123456"
}
f=open("account.db",'wb')
#f.write(pickle.dumps(account))
pickle.dump(account,f)
f.close()


