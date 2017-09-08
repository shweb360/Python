#字典是另一种可变容器模型，且可存储任意类型对象。
#字典的每个键值(key=>value)对用冒号(:)分割，
#每个对之间用逗号(,)分割，

#创建字典
dict={'Alic':'123','Beth':'456','Cecil':'789'}
dict1={'abc':456}
dict2={'ws':'123','abc':123,98.6:36}
print(dict)
print(dict1)
print(dict2)

#访问字典里的值
print('dict[Alic]:',dict['Alic'])

#修改字典
dict['Alic']=100; #更新
dict['Beth']=200;
print('dict[Alic]:',dict['Alic']);
print('dict[Beth]:',dict['Beth']);

#删除字典元素
del dict['Alic'] # 删除键 'Name'
dict.clear() #清空
del dict
print(dict);