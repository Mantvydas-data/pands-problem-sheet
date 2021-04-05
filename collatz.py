# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
# The program terminates if the current value is one.
# Author: Mantvydas Jokubaitis

#Function collatz runs till input num is not equal to 1
def collatz(num):
     while num!= 1:
    # checking if number is an even number, if so dividing by 2
        if num % 2 == 0:
            num /= 2
               # if number id odd, multiply by 3 an ddd 1.
        else:
            num = num*3 + 1
        numlist.append(int(num))

num = int(input("Please input positive integer: "))
numlist = [num,]
collatz(num)
print(numlist)