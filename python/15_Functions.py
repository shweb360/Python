import math
#Python内置函数
a=max(1,3,4,2)
print(a)
print("------------")

#数据类型转换
i=int('123')
print(i)
f=float('12.34')
print(f)

#定义函数
def my_abs(x):
	if x>=0:
		return x
	else:
		return -x
print(my_abs(-8))
print("------------")
#返回多个值
def move(x,y,step,angle=0):
	nx=x+step*math.cos(angle)
	ny=y-step*math.sin(angle)
	return nx,ny
#调用
x,y=move(100,100,60,math.pi/6)
print(x,y)
#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
#所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
r=move(100,100,60,math.pi/6)
print(r)

