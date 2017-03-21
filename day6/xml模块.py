#liuhao

import xml.etree.ElementTree as ET

tree = ET.parse("test.xml")
root = tree.getroot()
#打印根节点
print(root.tag)
#遍历xml文档
# for child in root:  #找到子节点
#     print(child.tag, child.attrib)  #打印子节点的名称和属性
#     for i in child:
#         print(i.tag,i.text,i.attrib) #打印child下的子节点的名称和文本信息，属性
#只遍历year 节点，自动向下遍历打印
# for node in root.iter('year'):
#     print(node.tag,node.text)
#修改和删除xml文档内容
tree = ET.parse("test.xml")  #获取源xml文件
root = tree.getroot()
# 修改
for node in root.iter('year'):  #通过iter获取到year节点
    new_year = int(node.text) + 1   #将获取到的年份加1
    node.text = str(new_year)       #节点的文本内容只能保存str格式
    node.set("updated", "yes")    #增加一个属性, 赋值
tree.write("test_modify.xml")       #将修改后的文件保存到一个xml文件中

# 删除node
for country in root.findall('country'): #从根中查找到 标签country
    rank = int(country.find('rank').text)   #获取到contry标签的rank标签的文本信息值
    if rank > 50:                           #判断他的大小
        root.remove(country)                #如果大于50 删除这个country标签

tree.write('output.xml')                #保存到output.xml