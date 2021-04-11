# A program that displays a plot of the functions f(x)=x, g(x)=x^2 and h(x)=x^3
# Author: Mantvydas Jokubaitis
import time
import matplotlib.pyplot as plt
import numpy as np

# Setting x values from 0 to 4 in 0.1 intervals
x = np.arange(0,4,0.1)

# Setting required functions 
y1=x
y2=x**2
y3=x**3

# Plotting functions and customising the looks
plt.plot(x, y1, linestyle= "-.", color = "g", label="f(x)=x", animated=False)
plt.plot(x, y2, ":", color="b", label="f(x)=x^2")
plt.plot(x,y3, "-", color="magenta",label="f(x)=x^3")

# Adding legend and title
plt.suptitle("Weekly Task #8")
plt.legend(loc="upper left")
plt.show()
