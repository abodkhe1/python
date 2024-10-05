# encapsulation
# polymorphism
class Car:
    
    totalCar=0
 
    def __init__(self, brand, model):
        self.__brand=brand
        self.model=model
        Car.totalCar+=1
        
    def fullName(self):
        return f"{self.__brand} {self.model}"
    
    def getBrand(self):
        return self.__brand
    
    def fuelType(self):
        return 'Disel'
                
class electrictClass(Car):
    def __init__(self, brand, model, baterysize):
        super().__init__(brand, model)
        self.baterysize:baterysize
        
    def fuelType(self):
        return 'electric'
    
    
    
    
    
    
    
myCar=Car('Mahindra', 'Thar')
# print(myCar.brand)
print(myCar.fullName())
print(Car.totalCar)
tesla=electrictClass('Mahindra', 'Thar', '85kwh')

# print(tesla.fullName())
# print(tesla.getBrand())

# _________________________________________



