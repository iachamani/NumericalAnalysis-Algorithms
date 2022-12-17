#function to solve linear system with using Householder transformation
#input: matrix A, vector b
#output: vector x
import numpy as np
import sys
def QRmethod(A,b):
    #QR decomposition
    Q,R = np.linalg.qr(A)
    #solve Rx=Q^Tb
    x = np.linalg.solve(R,np.dot(Q.T,b))
    return x

# Test the function QRmethod
A = np.array([[1,1,1],[6,-4,5],[5,2,2]])
#check if A is invertible
if np.linalg.det(A) == 0:
    print("A is not invertible")
    sys.exit()
b = np.array([2,31,13])
x = QRmethod(A,b)
#the solution is is (3,-2,1)
print(x)



