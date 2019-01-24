class Car():
    def __init__(self,make,model,year):
        '''初始化描述汽车的属性'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        #super().__init__(make,model,year)
        self.battery_size = 70

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' +self.model
        return long_name.title()

    def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print("This car has" + str(self.odometer_reading) + "miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles


    def describe_battery(self):
    	print("This car has a " + str(self.battery_size) + "-kwh battery.")



class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()