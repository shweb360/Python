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
#多态
