# A program that takes a positive floating-point number as input and outputs an approximation of its square root.
# Author: Mantvydas Jokubaitis

# Presetting aproximation tolerance for calculation 
tolerance=0.01
# Formula to calculate sqrt using Newton's method
def sqrt(num):
    x=num
    while abs(x-num*num)> tolerance: 
        num = (num+x/num)/2
    return num

print(round(sqrt(float(input("Please enter a positive number: "))),1))