
import math
def calculator():
    while True:
        print("___WELCOME TO SIMPLE CALCULATOR______")
        print("Here is a list of operations choose whatever you need..")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.power value")
        print("6.sine value")
        print("7.cos value")
        print("8.Tan value")
        print("9.Cot value")
        print("10.Sec value")
        print("11.Cosec value")
        print("12.Square root of a number")
        operator = int(input("enter the number of operation"))
        if operator == 0:
          print("EXIT CALCULATOR...")
          break
    
        if operator in [1,2,3,4,5]:
         n1 = float(input("Enter First number"))
         n2 = float(input("Enter Second number"))
    
        if operator == 1:
           res = n1+n2
           print(f"The Result of {n1} + {n2} :{res}")
        elif operator == 2:
           res = n1-n2
           print(f"The Result of {n1} -{n2} :{res}")
        elif operator == 3:
           res = n1*n2
           print(f"The Result of {n1} x {n2} :{res}")
        elif operator == 4:
           if n2!=0:
             res = n1/n2
             print(f"The Result of {n1} / {n2} :{res}")
           else:
             print("Error: Divsion by zero is not possible..")
        elif operator == 5:
           res = n1 ** n2
           print(f"The Result of {n1} ^ {n2} :{res}")
        elif operator == 6:
          angle = float(input("enter a value in degrees"))
          ra = angle*math.pi/180
          print(f"sin{angle} = {math.sin(ra)}")
        elif operator == 7:
          angle = float(input("Enter the value of angle in degrees"))
          ra = angle*math.pi/180
          print(f"cos{angle} = {math.cos(ra)}")
        elif operator == 8:
          angle = float(input("Enter the value of angle in degrees"))
          ra = angle*math.pi/180
          print(f"tan{angle} = {math.tan(ra)}")
        elif operator == 9:
          angle = float(input("Enter the value of angle in degrees"))
          ra = angle*math.pi/180
          print(f"cot{angle} = {1/math.tan(ra)}")
        elif operator == 10:
          angle = float(input("Enter the value of angle in degrees"))
          ra = angle*math.pi/180
          print(f"sec{angle} = {1/math.cos(ra)}")
        elif operator == 11:
          angle = float(input("Enter the value of angle in degrees"))
          ra = angle*math.pi/180
          print(f"cosec{angle} = {1/math.sin(ra)}")
        elif operator == 12:
           num = float(input("Enter a number"))
           print(f"Square root of a number:",math.sqrt(num))
                      
        else:
          print("Invalid operator number.please enter a valid operator number")
def operation():
    calculator()

    
operation()




