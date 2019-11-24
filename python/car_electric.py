from car import Car
#继承
#一个类继承另一个类时，它将自动获得另一个类的所以属性和方法；
#原有的类称为父类，而新类称为子类

#在Car类的基础上创建新类ElectricCar类
class ElectricCar(Car):

    def __init__(self,make,model,year):
        # 电动汽车的独特之处
        # 初始化父类的属性，再初始化电动汽车的特有属性
        super().__init__(make,model,year)
        self.battery_size=80

    def describ_battery(self):
        print('this car has a '+ str(self.battery_size)+ " -kwh battery.")

my_tesla=ElectricCar('tesla','model S',2019)
print(my_tesla.get_descriptive_name())
my_tesla.describ_battery()
