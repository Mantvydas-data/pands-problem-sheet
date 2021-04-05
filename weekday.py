# A program that outputs whether or not today is a weekday.
# Author: Mantvydas Jokubaitis

import datetime

x = datetime.datetime.now()
y = int(x.strftime("%w"))

if y < 6:
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")
