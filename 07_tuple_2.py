#创建元组
tup=(1,2,3)
print(tup)
print(type(tup))
#空元组
tup1=()

#访问元组
tup2 = (1, 2, 3, 4, 5, 6, 7 )
print(tup2[2:5])

#修改元组
t1=(6,7,8)
t2=('a','b','c')
# 以下修改元组元素操作是非法的
# t1[0]=100
#元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
t3=t1+t2
print(t3)

#将列表转换为元组
list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1=tuple(list1)
print(tuple1)