#面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。
#OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
	def print_score(self):
		print('%s:%s'%(self.name,self.score))
#调用
bart=Student('Wushuang',98)
bart.print_score()

'''
【小结】：
注意到__init__方法的第一个参数永远是self，表示创建的实例本身，
因此，在__init__方法内部，就可以把各种属性绑定到self，
因为self就指向创建的实例本身。
'''
print("-------------")
class Teacher(object):
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def print_age(self):
		print("%s:%s"%(self.name,self.age))
#调用老师对象
t=Teacher('Hanjuan',29)
t.print_age()
