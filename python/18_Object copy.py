#创建Dog类
class Dog():
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def sit(self):
		print(self.name.title()+" is now sitting")
	def	roll_over(self):import aiohttp
		print(self.name.title()+" rolled over!")

mydog= Dog("hhah",12)
print(mydog.name)
print(mydog.age)