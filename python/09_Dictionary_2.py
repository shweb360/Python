'''
字典是另一种可变容器模型，且可存储任意类型对象。
键必须是唯一的，但值则不必。
值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
'''

#创建字典
dict={'name':'tom','age':18}
print(dict)

#访问字典里的值
print(dict['name'])

#修改字典
dict['age']=20
print(dict)

#删除字典元素
#能删单一的元素也能清空字典，清空只需一项操作。显示删除一个字典用del命令
dict = {'name': 'Runoob', 'Age': 7, 'Class': 'First'}
del dict['name'] # 删除键 'name'
# dict.clear()     # 清空字典
# del dict         # 删除字典

print(str(dict))