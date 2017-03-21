#liuhao
import subprocess
# # 执行简单命令
# subprocess.run(['df','-h'])
# # 执行复杂命令，指定不需要python解析。直接扔给shell 终端 执行
# subprocess.run('df -h|grep /dev/sda1',shell=True)
# # 获取执行状态，和返回结果
# a=subprocess.getstatusoutput('dir')
# print(a)

# res=subprocess.Popen("dir",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
# #print(res.stdout.read().decode('gbk')) #标准输出
# print(res.stderr.read())    #错误输出
#

'''
run,shell=True
call,
check_call
getstatusoutput
p=subprocess.Popen()
    stdout =subprocess.PIPE,stderr=....
    env={}
    cwd={}
    preexec_fn      #只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用
p.stdout.read()
p.poll()
p.wait()

p.cominunicate(timeout=3)

'''
a=subprocess.getstatusoutput('dir')
print(a)

