from math import floor
from math import log
from math import tan

def func(t):
    return tan(t*t) -t                               
def average(x,y):
    return (x+y)/2

x = float(input("Enter le nombre de la borne a :"))
y = float(input("Enter le nombre de la borne b :"))
precision = float(input("Donner la precision : "))
for k in range(floor(log(y-x)-log(precision)/log(2))):
    if(func(x)*func(average(x,y))>0):
            x = average(x,y)
    if(func(x)*func(average(x,y))<0):
            y = average(x,y)  
    else:
        result = average(x,y)  
print(f"Alors resultat est = {result} ")                               

               
