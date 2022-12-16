#compute the integral of 1/(1+x^2) from 0 to 1 using the trapezoidal rule

import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return 1/(1+x**2)

def trapezoidal(f,a,b,n):
	h = (b-a)/n
	s = 0.5*f(a) + 0.5*f(b)
	for k in range(1,n):
		s += f(a+k*h)
	return h*s

a = 0
b = 1
n = 100
I = trapezoidal(f,a,b,n)
print(I)
#plot the area I computed
x = np.linspace(a,b,n+1)
y = f(x)
plt.plot(x,y)
plt.fill_between(x,y,0)
plt.show()






