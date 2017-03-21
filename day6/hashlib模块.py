#liuhao
import hashlib
# m = hashlib.md5()   #声明一个实例
# m.update(b'hello')
# print(m.hexdigest())    #输出一段md5值 16进制
# m.update(b' my name is alex')   #相当于两段字符串拼接，进行做md5
# print(m.hexdigest())
# m2 =hashlib.md5()
# m2.update(b'hello my name is alex') #验证拼接后的，进行md5验证
# print(m2.hexdigest())   #此处会发现----两次校验后的值是一样的
# print(m2.digest())#二进制的
#SHA加密
hash=hashlib.sha1() #谷歌破解了sha1 加密方式
hash.update(b'admin')
print(hash.hexdigest()) #16进制 加密值
hash=hashlib.sha256()   #sha256 加密方式
hash.update(b'admin')
print(hash.hexdigest())
hash=hashlib.sha512()   #sha512 加密方式
hash.update(b'admin')
print(hash.hexdigest())

#hmac  碉堡了 ,网络消息验证
import hmac
#前面是key 后面是内容
h=hmac.new('天王盖地虎'.encode(),'宝塔镇河妖'.encode())
print(h.hexdigest())
#对方有key 。会收到内容和加密后的值。
#对方直接使用key+ 内容 进行加密，对应得数据，一致---数据未被篡改








