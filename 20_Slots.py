#1.1创建一个类：
class Student(object):
	pass
#1.2给实例绑定一个属性：
s=Student()
s.name="Wushuang"
print(s.name);

#1.3给实例绑定一个方法
def set_age(self,age):
	self.age=age
from types import MethodType
#给实例绑定一个方法

s.set_age=MethodType(set_age,s)
#调用实例方法
s.set_age(25)
print(s.age)	

#2.0使用__slots_
#但是，如果我们想要限制实例的属性怎么办？
#比如，只允许对Student实例添加name和age属性。
#为了达到限制的目的，Python允许在定义class的时候，
#定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class Student2(object):
	__slots__=('name','age')

s2=Student2()
s2.name="Michael"
s2.age=24

print(s2)	