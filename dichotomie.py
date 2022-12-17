from math import floor
from math import log
from math import tan

def func(t):
    return tan(t*t) -t                               
def average(x,y):
    return (x+y)/2

x = 0.0
y = 3.0
precision = float(input("Donner la precision : "))
for k in range(floor(log(y-x)-log(precision)/log(2))):
    if(func(x)*func(average(x,y))>0):
            x = average(x,y)
    if(func(x)*func(average(x,y))<0):
            y = average(x,y)  
    else:
        result = average(x,y)  
print(f"Alors resultat est = {result} ") 
    
#plot the root of the function
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,10,100)
y = np.tan(x*x)-x
plt.plot(x,y)
plt.plot(1.5,0,'ro')
plt.show()
                        

               
