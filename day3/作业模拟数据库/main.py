#liuhao
import re
user_database="user_database"
def check_contain_chinese(check_str):
    # 传入 字符 进行判断，是不是汉字
     for ch in check_str:
         if u'\u4e00' <= ch <= u'\u9fff':
             return True
     return False
def output_head(search_list=['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date']):
    # 打印输出头部
    '''
    |-------------|-------------|-------------|-------------|-------------|-------------|
    |   staff_id  |     name    |     age     |    phone    |     dept    | enroll_date |
    |-------------|-------------|-------------|-------------|-------------|-------------|
'''
    show_lang = search_list
    lang = len(show_lang)
    flag = 0
    for i in show_lang:
        if flag < lang:
            print('+'.ljust(14, '-'), end='')
            flag += 1
    print('+')
    print('+', end='')
    for i in show_lang:
        print(i.center(13, ' ') + '+', end='')
    print()
    flag = 0
    for i in show_lang:
        if flag < lang:
            print('+'.ljust(14, '-'), end='')
            flag += 1
    print('+')
def output_body(list):
    print('|', end='')
    for i in list:
        if check_contain_chinese(i):
            print(i.center(13 - len(i), ' ') + '|', end='')
        else:
            print(i.center(13, ' ') + '|', end='')
    print()
def output_tail(search_list=['staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date'],count=0,search_sql=None,flag2=None):
    show_lang = search_list
    lang = len(show_lang)
    flag = 0
    search_first = search_sql.split()[0]
    for i in show_lang:
        if flag < lang:
            print('+'.ljust(14, '-'), end='')
            flag += 1
    print('+')
    print('+',end='')
    if len(search_sql)>(lang-1)*13:
        #print("执行语句".center(9, ' ') + '+  ' + search_sql.center(lang * 13 - 12, ' '))
        print("执行语句".center(9, ' ') + '+  ' + "it's to long".center(lang * 13-14, ' ') +'+')
    else:
        print("执行语句".center(9,' ')+'+'+search_sql.center(lang*13-9,' ')+'+')
    #输出与key相同长度的'-'
    flag = 0
    for i in show_lang:
        if flag < lang:
            print('+'.ljust(14, '-'), end='')
            flag += 1
    print('+')
    if search_first == 'select':
        string='查询到 %d 条数据'%count
        if lang==6:
            print('+' + string.center(lang * 13 - 1, ' ') + '+')
        else:
            print('+' + string.center(lang * 13 - 4, ' ') + '+')
    elif search_first == 'update' or search_first=='Do':

        string='修改了 %d 条数据 staff_id 为 %s'%(count,flag2)
        print('+' + string.center(lang * 13 - 2, ' ') + '+')
    elif search_first == 'delete':
        string = '删除了 %d 条数据 phone 为 %s' % (count, flag2)
        print('+' + string.center(lang * 13 - 2, ' ') + '+')
    elif search_first == 'insert':
        if count==0:
            string = '添加数据失败,电话号码重复'
            print('+' + string.center(lang * 13 - 7, ' ') + '+')
        elif count>0:
            string = '成功添加数据'
            print('+' + string.center(lang * 13, ' ') + '+')
    #输出与key相同长度的'-'
    flag = 0
    for i in show_lang:
        if flag < lang:
            print('+'.ljust(14, '-'), end='')
            flag += 1
    print('+')
    if count>0:
        return 'true'
    else:
        return "false"
def show_user_list():
    #将文件每行处理为列表的一个元素，其中的数据处理为对应的字典格式
    list=[]
    count = 1
    with open(user_database,'r',encoding='utf-8') as f:
        for i in f:
            dict_count = {'staff_id': None, 'name': None, 'age': None, 'phone': None, 'dept': None, 'enroll_date': None}
            dict_count['staff_id']=i.split(',')[0]
            dict_count['name']=i.split(',')[1]
            dict_count['age']=i.split(',')[2]
            dict_count['phone']=i.split(',')[3]
            dict_count['dept']=i.split(',')[4]
            dict_count['enroll_date']=i.split(',')[5].strip('\n')
            list.append(dict_count)
            count+=1
    return list
def check(a,operator,c,dict):
    #此函数进行判断，>,<,=,'like'
    #符合条件返回 i （字典），其它返回None
    user_date=show_user_list()
    if a=="age" or a == 'staff_id':
        if operator =='>':
            if int(dict[a]) > int(c) :
                return dict
        elif operator == '<':
            if int(dict[a]) < int(c):
                return dict
        elif operator == '=':
            if int(dict[a]) == int(c):
                return dict
        if operator == 'like':
             if len(re.findall(c,dict[a]))>0:
                return dict
    elif a in user_date[0]:
        #print(i)
        if operator == '=':
            if dict[a] == c:
                return dict
        if operator == "like":
            if len(re.findall(c,dict[a]))>0:
                return dict
def add_user_list(insert_sql): #传入插入相关的一个列表，格式要求[姓名，年龄，电话，工作，注册时间]
    # 用法：add_user_list("insert into table value(alex,33,11111,teacher,2017-1-1)")
    count=0
    try:
        insert_list=insert_sql.split(' ')
        #print(insert_list[3].split('(')[0])
        if insert_list[0] == 'insert' and insert_list[1] =='into' and insert_list[3].split('(')[0]=='value':
            user_list=insert_list[3].split('(')[1].split(')')[0].split(',')
        else:
            print("请检查语法")
            return
       # print(user_list)
        if type(user_list) is not list:
            exit("请传入一个列表")
        if len(user_list)<5:
            print('''
            输入列表元素，value对应字段 name,age,phone,dept,enroll_date
            for example:
            insert into user_database value(alex,33,11111,teacher,2017-1-1)
            ''')
            return
        with open(user_database,'r+',encoding='utf-8') as f:
            for i in f:#遍历过全部数据，将光标移动到末尾
                num=i.split(',')[0]
                if user_list[2] == i.split(',')[3]:     #对唯一主键phone 进行判断。
                    output_tail(search_sql=insert_sql)
                    return
            num=int(num)+1                   #将staff_id自增
            list_str = str(num)        #list_str,进行组合,
            for i in user_list:
                list_str=list_str+','+str(i)
            f.write(list_str+'\n')
            count+=1
            output_tail(search_sql=insert_sql,count=count)
    except IndexError as a:
        print("请检查数据库文件格式!!!")
def select_search(search_sql):
    search_list=search_sql.split(' ')   #将传入的字符串切割为列表
    count=0
    user_list=show_user_list()          #获取用户信息全部数据
    if search_list[1] == '*':
        search_list[1] = 'staff_id,name,age,phone,dept,enroll_date'
    output_head(search_list[1].split(','))      # 打印输出头部
    for user in user_list:
        pri_list = []       #将要打印的数据添加到其中
        first = search_list[1].split(',')  # 传入字符第二个字段，进行二次切割
        for i in first:
            if i not in user:
                return "输出字段不存在",i
        if len(search_list) ==4  and search_list[2]=='from':
            for i in first:
                pri_list.append(user[i])
            output_body(pri_list)
            count+=1
        else:
            chect_return=check(search_list[5], search_list[6], search_list[7].strip('"').strip("'"), user)
            #print(type(chect_return))
            if type(chect_return) is dict:
                for i in first:
                    pri_list.append(chect_return[i])
                count+=1
                output_body(pri_list)
    output_tail(search_list[1].split(','),count,search_sql)
def delete(delete_sql):
    #delete from user_database where staff_id = 1
    #删除数据库中的数据
    status = []
    count = 1
    temporary=[]    #临时存储
    delete_list = delete_sql.split(' ')
    if delete_list[0] == 'delete' and delete_list[1] == 'from' and delete_list[3] == 'where':
        user_data = show_user_list()
        for i in user_data:
            check_return=check(delete_list[4],delete_list[5],delete_list[6].strip('"').strip("'"),i)
            if type(check_return) is dict:
                temporary.append(i)
                status.append((i['phone']))
        for i in temporary:
            user_data.remove(i)
        with open(user_database,'w+',encoding='utf-8') as f:   #修改数据库文件中的数据
            for i in user_data:
                if i['staff_id'] != count:
                    i['staff_id'] = count
                #因为字典是无序的，所以不能循环去拼接字符
                str_data = str(i['staff_id'])+','+i['name']+','+i['age']+','+i['phone']+','+i['dept']+','+i['enroll_date']+'\n'
                f.write(str_data)
                f.flush()
                count += 1
        lang=len(status)
        return output_tail(count=lang,search_sql=delete_sql,flag2=status)
#update staff_table set dept = "Market" where dept = "IT"
def modify(modify_sql):
    count=0
    flag=[]
    modify_list = modify_sql.split(' ')
    if modify_list[3] == 'phone':
        modify_sql="Do not modify the phone number, can only be deleted and then added"
        output_tail(search_sql=modify_sql)
        return
    elif modify_list[3] == 'staff_id':
        modify_sql="Do not modify the ID! Automatic system modification!!!"
        output_tail(search_sql=modify_sql)
        return
    if modify_list[0] == 'update' and modify_list[2] == 'set' and modify_list[6] == 'where':
        user_data=show_user_list()
        for i in user_data:
            #update user_database set age = 100 where age = 77
            check_return=check(modify_list[7],modify_list[8],modify_list[9].strip('"').strip("'"),i)
            if type(check_return) is dict :
                i[modify_list[3]] = modify_list[5]
                flag.append(i['staff_id'])
                count+=1
    with open(user_database,'w+',encoding='utf-8') as f:
        for i in user_data:
            str_data = str(i['staff_id']) + ',' + i['name'] + ',' + i['age'] + ',' + i['phone'] + ',' + i[
                'dept'] + ',' + i['enroll_date'] + '\n'
            f.write(str_data)
            f.flush()

    output_tail(count=count,search_sql=modify_sql,flag2=flag)
#modify("update staff_table set age = 100 where age = 77")
#delete("delete from user_database where staff_id = '10' ")
#add_user_list("insert into user_database value(alex,33,1213452121,teacher,2017-1-1)")
#select_search("select staff_id,name,age from staff_ble where dept like '实习'")
def main():
    print('''欢迎登陆员工数据库。''')
    while True:
        try:
         sql=input('请输入sql语句 [help]>>').strip()
         if sql =='help':
             print('''
             范例：
             select * from user_database
             select staff_id,name,age from user_database where dept like '实习'
             insert into user_database value(alex,33,11111,teacher,2017-1-1)
             delete from user_database where staff_id > '10'
             update user_database set age = 100 where age = 77
         ''')
         else:
             choice=sql.split(' ')
             msg={"select":[select_search,choice[3]],"insert":[add_user_list,choice[2]],"delete":[delete,choice[2]],"update":[modify,choice[1]]}
             if choice[0] in msg:
                     user_database=msg[choice[0]][1]
                     msg[choice[0]][0](sql)
        except FileNotFoundError as a :
            print("数据库文件不存在:",a)
        except IndexError as a:
            print("请检查sql语句是否正确，请认真参考范例sql")

main()
