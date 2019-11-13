#函数的参数

#1.1位置参数

def power(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x		
	return s
print(power(5,2))
print("--------------")
#1.2设置默认参数
def enroll(name,gender):
	print('name',name)
	print('gender',gender)

print(enroll('wisjiamg','F'))	
print("--------------")
#如果要继续传入年龄、城市等信息怎么办？
#这样会使得调用函数的复杂度大大增加。
#我们可以把年龄和城市设为默认参数：
def enroll2(name,gender,age=6,city="Shanghai"):
		print('name',name)
		print('gender',gender)
		print('age',age)
		print('city',city)
print(enroll2("wushuang",'F'))
print("--------------")
#1.3设置默认参数
def add_end(L=[]):
	L.append('END')
	return L
print(add_end([1,2,3]))	
print(add_end())
print(add_end())

#定义默认参数要牢记一点：默认参数必须指向不变对象！

print("--------------")
#2.1可变参数
def calc(numbers):
	sum=0
	for n in numbers:
		sum=sum+n*n
	return sum
print(calc([1,2,3]))	
print(calc([1,2,3,5,6]))
print("--------------")
def calc2(*numbers):
		sum=0
		for n in numbers:
			sum=sum+n*n
		return sum
print(calc2(1,2))
print("--------------")
#2.2如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums=[1,2,3]
print(calc2(nums[0],nums[1],nums[2]))

print(calc2(*nums))
#*nums表示把nums这个list的所有元素作为可变参数传进去


print("--------------")
#3.1关键字参数
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)

print(person('Wushuang',30))
#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
#也可以传入任意个数的关键字参数：
print(person('Bob',35,city='Shanghai'))	

#简化的写法：
extra={'city':'Beijing','Job':'Engineer'}
person('Jack',24,**extra)
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
#注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
print("--------------")
#4.1命名关键字参数
def person2(name,age,**kw):
	if 'city' in kw:
		#有city参数
		pass
	if 'job' in kw:
		#有job参数
		pass
	print('name:',name,'age:',age,'other:',kw)

person2("Jack",24,city="Beijing",addr="Chaoyang")

#4.2和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

def person3(name,age,*,city,job):
	print(name,age,city,job)
	
print(person3('Jack',24,city='Beijing',job='Enginner'))







