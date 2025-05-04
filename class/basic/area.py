class calculateArea:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def perimeter(self):
        return (self.length+self.breadth)*2
    def area(self):
        return self.length*self.breadth
length=float(input("Enter length: "))
breadth=float(input("Enter breadth: 23"))
rect=calculateArea(length,breadth)

print(f"Area: {rect.area()}")
print(f"Perimeter: {rect.perimeter()}")


        