#!/usr/bin/env python
# -*- coding:utf-8 -*-

head_list=["num","name","age","phone","job","time"]
# ###########  读取文件  ###########
# 读入数据返回数据的列表
def read_file(path):
    date = []
    with open(path,encoding='utf-8') as f:
        for line in f:
            line = line.strip()  # 去除字符串末尾的"\n"
            line = line.split(",")  # 字符串变为列表
            date.append(line)  # 把所有用户信息读取到内存，放入列表中
    return date


# ###########  写入文件  ###########
def write_file(path, date):
    with open(path,mode="w", encoding='utf-8') as f:
        for line in date:
            line=",".join(line)+"\n"
            f.write(line)


# #########  num重新复制  ##########
def re_list():
    date=read_file("date")
    count=1
    new_date=[]
    for line in date:
        line[0]="{}".format(count)
        new_date.append(line)
        count+=1
    return new_date


# ##  判断用户查询输入的格式是否正确  ##
def input_if(string):
    if len(string) == 8:     # 判断列表的长度
        options = string[0]   # select
        return_value = string[1]   # name
        from_key = string[2]   #     form
        lists = string[3]     # date
        where_key = string[4]  #   where
        conditions_key = string[5]  # age
        symbol = string[6] # >
        value = string[7]  # 22
        return_value = return_value.split(",")
        # update,delete,install暂时用不到
        if options not in ["select","update","delete","install"] or from_key != "from" or where_key != "where":
            exit("关键字错误")
        for line in return_value:
            if line not in head_list and line != "*":
                exit("返回元素错误")
        if conditions_key not in head_list:
            exit("条件元素不存在")
        return True
    else:
        print("输入元素个数错误！")
        return False



# #############  查询  #############
# 测试语句
# select name,age,phone from date where num > 5
def select(input_date):
    input_date = input_date.split(" ")    # 把用户的输入变为列表，默认中间必须为一个空格
    if input_if(input_date):
        options = input_date[0]  # select
        return_value = input_date[1]  # name
        from_key = input_date[2]  # form
        lists = input_date[3]  # date
        date = read_file(lists)  # 需要完善，没有做表是否存在判断
        where_key = input_date[4]  # where
        conditions_key = input_date[5]  # age
        symbol = input_date[6]  # >
        value = input_date[7].strip('"')  # 22  # 去除条件中的双引号
        return_value = return_value.split(",")
        return_list=[]
        where_id = head_list.index(conditions_key)
        if symbol == ">":  # 判断给定条件       ###################    >
            for line in date:
                if int(line[where_id]) > int(value):
                    return_list.append(line)
                else:
                    continue
        if symbol == "<":  # 判断给定条件       ###################    <
            for line in date:
                if int(line[where_id]) < int(value):
                    return_list.append(line)
                else:
                    continue
        if symbol == "=":  # 判断给定条件       ###################    ==
            for line in date:
                if line[where_id] == value:
                    return_list.append(line)
                else:
                    continue
        if symbol == "like":
            for line in date:
                if value in line[where_id]:
                    return_list.append(line)
                else:
                    continue
        if return_list:
            finsh_input=[]
            finsh2_input = []
            for line in return_value:
                if line == "*":
                    for line in return_list:
                        finsh2_input.append(line)
                        print("\t".join(line))
                else:
                    for lines in return_list:
                        finsh_input.append(lines[head_list.index(line)])
            for i in range(len(finsh_input)//len(return_value)):
                finsh2_input.append(finsh_input[i::len(finsh_input)//len(return_value)])
                print("\t".join(finsh_input[i::len(finsh_input)//len(return_value)]))
            print("数量统计：",len(finsh2_input))
            return finsh2_input
        else:
            return False
    else:
        return False


# #############  增加  #############
# 测试语句
# insert into date ("name","age","phone","job","time") values ("李啸宇","22","13564081679","学生","2017/1/1")
# insert into date ("name","age","phone","time","job") values ("李啸宇","22","13564080679","2017/1/1","学生")
def insert(input_date):
    date = input_date.split(" ")
    # 判断insert语句格式
    if len(date) == 6:
        list0 = date[0]  # install
        list1 = date[1]  # into
        list2 = date[2]  # date
        list3 = date[3]  # key_1
        list4 = date[4]  # value
        list5 = date[5]  # key 2
        num = []  # 用于放，value值的位置信息
        re_value = []  # 用户存放排序后的插入数据
        if list0 == "insert" and list1 == "into" and list4 == "values":
            list3 = eval(list3)
            list5 = eval(list5)
            if len(list3) == 5 and len(list5) == 5:  # 判断用户输入的元素个数
                for line in list3:
                    if line in head_list:
                        continue
                    else:
                        print("输入的元素名错误")
                        break
                for line in list3:
                    value_num = head_list.index(line)
                    num.append(value_num)
                for i in range(5):
                    list5_n = list5[num.index(i + 1)]
                    re_value.append(list5_n)       # 通过整理后的数据，没有user_id，后续处理。
                one_test=re_value[2]
                one_string="select * from {} where phone = {}".format(list2,one_test)
                if select(one_string):
                    print("键值重复")
                else:
                    date=read_file(list2)
                    user_num=str(len(date)+1)  # 查找文件中元素个数，加一后
                    re_value.insert(0,user_num)  # 插入元素的num到新增数据的首部
                    date.append(re_value)
                    write_file(list2, date)
            else:
                print("元素个数错误")
        else:
            print("输入有误")


# #############  更新  #############
# update date set name = new_date where age = 22
# update date set phone = 13564081679 where age = 22
def update(input_date):
    date = input_date.split(" ")
    # 判断长度
    if len(date) == 10:
        list_0 = date[0]    # update   key
        list_1 = date[1]    # date
        list_2 = date[2]    # set   key
        list_3 = date[3]    # name
        list_4 = date[4]    # =
        list_5 = date[5]    # new_date
        list_6 = date[6]    # where   key
        list_7 = date[7]    # age
        list_8 = date[8]    # =
        list_9 = date[9]    # 22
        if list_0 == "update" and list_2 == "set" :
            select_string="select * from {} {} {} {} {}".format(list_1,list_6,list_7,list_8,list_9)
            print("要修改的数据为：")
            select_date=select(select_string)
            if list_3 in head_list and list_4 == "="and list_3 != "num":
                # 改phone的参数
                if list_3 == "phone" and len(select_date) == 1:
                    select_string="select * from {} {} {} {} {}".format(list_1,list_6,list_3,list_4,list_5)
                    if select(select_string) == False:  # 修改phone的值，先查询表里有没有phone值为修改值的。如果为False。可以修改。
                        for line in select_date:
                            line[head_list.index(list_3)] = list_5
                        date = read_file(list_1)
                        i = 0
                        for line in select_date:
                            for lines in date:
                                if line[0] == lines[0]:
                                    date[int(lines[0]) - 1] = select_date[i]
                                    i += 1
                                    break
                        write_file(list_1, date)
                    elif list_7 == "phone":  # 查询和修改项都为phone，
                        for line in select_date:
                            line[head_list.index(list_3)] = list_5
                        date = read_file(list_1)
                        i = 0
                        for line in select_date:
                            for lines in date:
                                if line[0] == lines[0]:
                                    date[int(lines[0]) - 1] = select_date[i]
                                    i += 1
                                    break
                        write_file(list_1, date)
                    elif len(select_string) ==1:
                        print(select_date[0])

                    else:
                        print("不能修改")

#################################################################################
                elif list_3 != "phone":
                    for line in select_date:
                        line[head_list.index(list_3)] = list_5
                    date=read_file(list_1)
                    i = 0
                    for line in select_date:
                        for lines in date:
                            if line[0] == lines[0]:
                                date[int(lines[0])-1] = select_date[i]
                                i += 1
                                break
                    write_file(list_1, date)
                else:
                    print("数据无法修改。")
            else:
                print("关键字不存在或修改的参数为num")
    else:
        return 1  # 长度错误，返回值为1


# #############  删除  #############
# 测试语句
# delete from date where num < 5
def delete(input_date):
    select_string=["select","*"]
    input_date = input_date.split(" ")  # 把用户的输入变为列表，默认中间必须为一个空格
    select_string.extend(input_date)
    select_string.remove("delete")
    date = read_file(select_string[3])
    select_string=" ".join(select_string)
    select_list=select(select_string)
    for line in select_list:
        if line in date:
           date.remove(line)
    write_file("date",date)
    date=re_list()
    write_file("date",date)

# ############  主函数  ############
while True:
    list_dict={"select":select,"insert":insert,"delete":delete,"update":update}
    input_date=input("输入你要进行查询的语句")
    input_date_if= input_date.split(" ")
    if input_date_if[0] in list_dict:
        list_dict[input_date_if[0]](input_date)
    else:
        continue
