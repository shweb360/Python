#Python3 集合
'''
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

'''
#创建集合
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)               # 这里演示的是去重功能
print('apple' in basket)    # 快速判断元素是否在集合内

# 下面展示两个集合间的运算.
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
print(a-b)                  # 集合a中包含而集合b中不包含的元素
print(a|b)                  # 集合a或b中包含的所有元素
print(a&b)                  # 集合a和b中都包含了的元素
print(a^b)                  # 不同时包含于a和b的元素

#类似列表推导式，同样集合支持集合推导式
a={x for x in 'abracadabra' if x not in 'abc'}
print(a)

#集合的基本操作
#1、添加元素
thisset = set(("Google", "Runoob", "Taobao"))
thisset.add('Baidu')
print(thisset)

thisset.add("Taobao") #如果元素已存在，则不进行任何操作
print(thisset)

#还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等
thisset.update({1,2,3})
print(thisset) 
thisset.update([1,4],[5,6])
print(thisset) 
thisset.update({'name':'ws'})
print(thisset) 

#2、移除元素
thisset.remove('Google')
print(thisset)
#如果元素不存在，则会发生错误
# thisset.remove('Google2') 
#此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误
thisset.discard('Google3')
#也可以设置随机删除集合中的一个元素
x=thisset.pop()
print(x)

#3、计算集合元素个数
print(len(thisset))

#4、清空集合
thisset.clear()
print(thisset)

thisset = set(("Google", "Runoob", "Taobao"))
print(thisset)
thisset={('a','b'),12}
print(thisset)

var2=0
if var2:
    print('true')
else:
    print('false')
print(123)

age=int(input('请输入你家狗狗的年龄:'))

if age<=0:1
    print('你是在逗我吧')
elif age == 1:
    print('相当于 14 岁的人')  