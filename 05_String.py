#Python 访问字符串中的值

var1='Hello World'
var2='Runoob'
print('var1[0]',var1[0])
print('var2[1:5]',var2[1:5])

#Python字符串更新
print("已更新字符串：",var1[:6]+"wushuang")

#Python字符串运算符
a="Hello"
b="Python"

print("a+b输出结果：",a+b)
print("a*2输出结果：",a*2)
print("a[1]输出结果：",a[1])
if("H" in a):
	print("H 在变量 a中")
else:
	print("H 不在变量 a 中")
	
#Python字符串格式化
print("小米 %s %d"%('xiaoming',10))