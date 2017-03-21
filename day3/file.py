#liuhao


f=open("test",'rb')
print(f.read().decode("utf-8"))
f.close()

f=open("test1",'wb')
f.write("哈哈哈".encode("utf-8"))
f.close()

