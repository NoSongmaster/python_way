#liuhao
''''''
'''
递归特性;
1、必须有一个明确的结束条件
2、每次进入更深一层递归时，问题规模相比上次递归都应有所减少
3、递归效率不高，递归层次过多会导致栈溢出（2）
'''
def cacl(n):
    print(n)
    if int(n/2) >0:
            n=cacl(int(n/2))
    return n

print(cacl(10))
