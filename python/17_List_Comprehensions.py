#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
#1.1
L=list(range(1,11))
print(L)
print("-------------------")
#1.2,如果要生成[1x1, 2x2, 3x3, ..., 10x10]
L2=[]
for x in range(1,11):
	L2.append(x*x)
print(L2)
print("-------------------")
#1.3 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
L3=[x*x for x in range(1,11)]
print(L3)

#1.4 for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d={'x':'A','y':'B','z':'C'}
for k,v in d.items():
	print(k,'=',v)
	
