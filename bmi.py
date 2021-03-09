# Weekly Task 02 - Body Mass Index Calculator
# Author: Mantvydas Jokubaitis

weight = float(input("Please input your weight in kg: "))
height = int(input("Please input your height in cm: "))/100
BMI = weight / height**2
print("Your BMI is " + str(BMI))
print( height)