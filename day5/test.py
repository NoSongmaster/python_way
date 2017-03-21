#liuhao
import hashlib
addr='192.168.1.1'
md = hashlib.md5()
md.update(addr.encode() + '1'.encode() + '3c6e0b8a9c15224a8228b9a98ca1531d'.encode())
md_key = md.hexdigest()
print(md_key)



