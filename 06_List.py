#序列是Python中最基本的数据结构
list1=['Google','Runoob',1997,2017];
list2=[1,2,3,4,5];
list3=["a","b","c","d"];

#访问列表中的值
print(list1)
print(list1[0])

#更新列表
print("第三个元素：",list1[2])
list1[2]=2001
print("更新后的第三个元素为：",list1[2])

#删除列表元素
del list1[2]
print("删除第三个元素：",list1)

names=['Tom','Jack','Tony']
print(names)