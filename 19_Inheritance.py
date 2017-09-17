#继承和多态
#1.1
class Animal(object):
	def run(self):
		print("Animal is running...")

class Dog(Animal):
	def run(self):
		print("Dog is running")

class Cat(Animal):
	def run(self):
		print("Cat is running")

#调用
dog=Dog()
dog.run()

cat=Cat()
cat.run()	

#继承好处：子类获得了父类的全部功能
#多态:即一个引用变量倒底会指向哪个类的实例对象，
#该引用变量发出的方法调用到底是哪个类中实现的方法，
#必须在由程序运行期间才能决定
