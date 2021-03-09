# Weekly Task 02 - Body Mass Index Calculator
# Author: Mantvydas Jokubaitis

weight = float(input("Please input your weight in kg: "))
height = int(input("Please input your height in cm: "))/100
BMI = weight / height**2
print("Your BMI is " + str(BMI))

#Adding statements to also advise on BMI health ranges
#https://www.cancer.org/cancer/cancer-causes/diet-physical-activity/body-weight-and-cancer-risk/adult-bmi.html
if BMI < 18.5:
    print("Your BMI is below 18.5, you could be underweight. Please consult your doctor. ")
elif BMI == 18.5 or BMI < 24.9:
    print("You have normal weight BMI")
elif BMI == 25 or BMI < 29.9:
    print("BMI of 25 to 29.9 indicates you might be overweight ")
else : print ("High BMI suggests obesity, please consult your doctor. ")