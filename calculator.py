import random
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error"
    return x/y
while(1):
    
    print("Select operation:")
    print("1. Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")
    print("5 Exit")

    choice = input("Enter the choice(1-5):")

    if choice == '5':
        print("You chose to exit the program.")
        print("Quitting")
        break

    if choice not in ['1', '2', '3', '4']:
        print("Invalid input")
        continue
    
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter first number: "))

    if choice == '1':
        print("Result:",add(num1,num2))
    elif choice == '2':
        print("Result:",add(num1,num2))
    elif choice == '3':
        print("Result:",add(num1,num2))
    elif choice == '4':
        print("Result:",add(num1,num2))
  
        
