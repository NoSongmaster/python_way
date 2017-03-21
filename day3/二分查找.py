#liuhao
#return 代表函数的结束，返回函数的结果
#二分查找
#mid 中间
data=range(0,100000000000,3)
def two_1(str_search,data):
    mid=int(len(data)/2)    #找到data列表中间的位置
    if mid ==0:
        if data[mid] ==str_search:
            print("find it ",data[mid])
        else:
            print("not find ")
    elif data[mid]==str_search:
        print("find it ",data[mid])
    elif data[mid] > str_search: #应该去左边查找
        print("find to 左边 ",data[0:mid])
        two_1(str_search,data[0:mid])
    elif data[mid] < str_search:  #应该去右边查找
        print("find to 右边",data[mid:])
        two_1(str_search,data[mid:])

two_1(9999,data)


