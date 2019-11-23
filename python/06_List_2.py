#列表由一系列按特定顺序排列的元素组成
bicycles=['trek','cannodale','redline','sepcialized']
print(bicycles)

print('---------访问列表元素-----------')
#访问列表元素
print(bicycles[0])

print('---------使用列表中的各个值---------')
message='My first bicycle was a ' + bicycles[0].title() +  '.'
print(message)

print('--------修改元素------------')
bicycles[0]='trek2'
print(bicycles)

print('--------添加元素------------')
bicycles.append('jat')
print(bicycles)

print('--------del语句 删除元素------------')
#使用del可以删除任何位置的列表元素，前提是知道其索引
del bicycles[0]
print(bicycles)

print('--------pop()方法 删除元素------------')
bic=bicycles.pop()
print(bicycles)
#弹出列表中任何位置处的元素
bic=bicycles.pop(0)
print(bicycles)

print('--------remove()方法 删除元素------------')
bicycles.remove("redline")
print(bicycles)

myliebiao=[1,2,3,4,5,6]
print(myliebiao[0:5])
print(len(myliebiao))
print(['WUSH']*4)
print(3 in [1, 2, 3])

for x in [1, 2, 3]:
    print(x)


#列表截取
L=['baidu','taobao','google']
print(L[1])
print(L[-1])
print(L[-2])

#列表拼接
L2=['pingduoduo','jd']
print(L+L2)
L+=L2
print(L)

#嵌套列表
Q=[['a','b','c'],'123',[4,5,6]]
print(Q)
print(Q[0])
print(Q[0][2])

#Python列表函数&方法
Q1=['1','2','3']
print(max(Q1)) #返回列表元素最大值
print(min(Q1)) #返回列表元素最小值
A1=(4,5,6)     #将元组转换为列表
print(list(A1))

