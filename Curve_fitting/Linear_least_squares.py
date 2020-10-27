from __future__ import print_function
import numpy as np
import sympy as s


def print(*args):
    __builtins__.print(*("%.8f" % a if isinstance(a, float) else a for a in args))


X = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]
Y = [1.3 , 3.5 , 4.2 , 5.0 , 7.0 , 8.8 , 10.1 , 12.5 , 13.0 , 15.6]
Xx = 1.5

x = s.Symbol('x')

m = len(Y)

print("\n\nXi\t Yi\t\tXi^2\t Xi*Yi")
for i in range(m):
    print(X[i] , "\t" , Y[i] , "\t" ,  X[i] ** 2 , "\t" ,  X[i] * Y[i]) 

# Calculating required summations
X_S = np.sum(X) 
Y_S = np.sum(Y)
X_X_S = np.sum(np.power(X , 2))
X_Y_S = np.sum(np.multiply(X , Y))

print("-" * 50)
print(X_S , "\t" , Y_S , "\t" ,  X_X_S , "\t" ,  X_Y_S)
print("-" * 50)

# Calculating coefficient
a0 = (X_X_S * Y_S - X_Y_S * X_S) / (m * X_X_S - X_S ** 2)
a1 = (m * X_Y_S - X_S * Y_S) / (m * X_X_S - X_S ** 2)

print("\n\nCoeffcinets are ")
print("a0 = " , a0)
print("a1 = " , a1)

P = a0 + a1 * x
print("\n\nThe expression of polynomial is " , P)
print("The value of polynomial is " , P.subs(x , Xx))