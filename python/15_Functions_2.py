'''
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，
而 list,dict 等则是可以修改的对象。
'''
# 参数
# 以下是调用函数时可使用的正式参数类型：
# 必需参数
# 关键字参数
# 默认参数
# 不定长参数

# 必需参数
def printMe( str ):
	print( str )
#调用
printMe("wush")
print("=========")

#关键字参数
def printInfo( name , age ):
	print('姓名：',name)
	print('年龄:',age)
	return
#调用
printInfo( age=20 , name='wush' )
print("=========")

#默认参数
def printM(name,age=18):
	print('姓名：',name)
	print('年龄:',age)
#调用
printM("Jack")
print("=========")


#不定长参数
#加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数
def printB(agr,*varTuple):
	print("agr:",agr)
	print("varTuple:",varTuple)

printB(1,2,3,4,5)
printB(1)
printB(2,3,4,5)
#加了两个星号 ** 的参数会以字典的形式导入
def printZ(agr,**varDic):
	print("agr:",agr)
	print("varDic:",varDic)
printZ(1,name='wu',address='SH')
#如果单独出现星号 * 后的参数必须用关键字传入。
def f(a,b,*,c):
	return a+b+c
f(1,2,c=4)

#匿名函数
sum=lambda a,b,c: a+b+c
print(sum(1,2,3))