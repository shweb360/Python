#???
class Dog():
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def run(self):
		print('The dog name is '+self.name)
		print('The dog age is '+str(self.age))

#??????
mydog=Dog('erha',2)
#????
mydog.name
#????
mydog.run()