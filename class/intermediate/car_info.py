class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.mileage=0
        
    def drive(self,km):
        if km<0 :
            print("The distance must be positive")
            return
        else:
            self.mileage += km
            print(f"Driving {km}km. Total mileage is {self.mileage}")
        
        
    def display_info(self):
        print("Car Details:")
        print(f"Name: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Mileage: {self.mileage} km")
        
#Create class object
car1 = car("Toyota","Camry",2021)
car1.display_info()
car1.drive(150)
car1.drive(20)