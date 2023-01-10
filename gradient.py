#Gradient descent algorithm to find the minimum error between the liniear regression and the data points

import numpy as np
import matplotlib.pyplot as plt
#data points
x = np.array([1,2,3,3.7,2,1,5.3,8.7,10,7])
y = np.array([2,4,6,8,10,12,14,16,18,20])

#learning rate
lr = 0.01
#number of iterations
n = 1000
#initial slope and intercept

m = 0
c = 0
#number of data points
N = len(x)

#gradient descent algorithm

for i in range(n):
    y_pred = m*x + c
    D_m = (-2/N)*sum(x*(y-y_pred))
    D_c = (-2/N)*sum(y-y_pred)
    m = m - lr*D_m
    c = c - lr*D_c

#plotting the data points and the line of best fit

plt.scatter(x,y)
plt.plot([min(x),max(x)],[min(y_pred),max(y_pred)],color='red')
plt.show()
