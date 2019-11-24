
#Car类long_name=
class Car():
    def __init__(self,make,model,year):
        # 初始化汽车的属性
        self.make=make
        self.model=model
        self.year=year
        # 指定默认值 里程        
        self.odometer=0 

    def get_descriptive_name(self):
        # 返回描述信息
        long_name=str(self.year)+' '+ self.make+' '+self.model
        return long_name.title()
    # 读取里程
    def read_odometer(self):
        print("This car has "+str(self.odometer)+" miles on it")
    # 更新里程
    def update_odometer(self,mileage):
        if mileage>=self.odometer:
            self.odometer=mileage
        else:
            print("You can not roll back an odometer!")
    # 通过方法对属性的值进行递增
    def increment_odometer(self,miles):
        self.odometer+=miles

mycar=Car('BMW','X5',2019)
# 修改属性值
print(mycar.get_descriptive_name())
mycar.read_odometer()

mycar.update_odometer(100)
mycar.read_odometer()

mycar.increment_odometer(200)
mycar.read_odometer()


