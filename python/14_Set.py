#set和dict类似，也是一组key的集合，
#但不存储value。由于key不能重复，所以，在set中，没有重复的key。

#要创建一个set，需要提供一个list作为输入集合：
s=set([1,2,3])
print(s)
print("-----------")
#注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。。

#重复元素在set中自动被过滤：

st=set([1,1,2,2,3,3])
print(st)
print("-----------")

#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
st.add(3)
print(st)
print("-----------")

#通过remove(key)方法可以删除元素：
st.remove(3)
print(st)
print("-----------")

#set可以看成数学意义上的无序和无重复元素的集合，
#因此，两个set可以做数学意义上的交集、并集等操作：
s1=set([1,2,3])
s2=set([2,3,4])
print(s1&s2)
print(s1|s2)
print("-----------")

#不可变对象
#list进行操作
a=['c','b','a']
a.sort()
print(a)
a2='abc'
a2.replace('a','A')
print(a2)
