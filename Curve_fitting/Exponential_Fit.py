from __future__ import print_function
import numpy as np
import sympy as s
from math import log

def print(*args):
    __builtins__.print(*("%.8f" % a if isinstance(a, float) else a for a in args))

# y = a * e ^ b * x

# log(y) = log(a) + b * x
# Y      =  a0    + a1 * X

X = [1 , 1.25 , 1.50 , 1.75 , 2.00]
Y = [5.10 , 5.79 , 6.53 , 7.45 , 8.46]    
Xx = 1.54

x = s.Symbol('x')

m = len(X)

X = np.array(X)
Y = np.array(Y)

Log_X = X
Log_Y = []
for i in range(m):
    Log_Y.append(log(Y[i]))

print("\n\nXi\t\t  Log_Yi\t  Log_Xi^2\t Xi*Log_Yi")
for i in range(m):
    print(Log_X[i] , "\t" , Log_Y[i] , "\t" ,  Log_X[i] ** 2 , "\t" ,  Log_X[i] * Log_Y[i]) 

# Calculating required summations
Log_X_S = np.sum(Log_X) 
Log_Y_S = np.sum(Log_Y)
Log_X_X_S = np.sum(np.power(Log_X , 2))
Log_X_Y_S = np.sum(np.multiply(Log_X , Log_Y))

print("-" * 50)
print(Log_X_S , "\t" , Log_Y_S , "\t" ,  Log_X_X_S , "\t" ,  Log_X_Y_S)
print("-" * 50)

# Calculating coefficient
a0 = (Log_X_X_S * Log_Y_S - Log_X_Y_S * Log_X_S) / (m * Log_X_X_S - Log_X_S ** 2)
a1 = (m * Log_X_Y_S - Log_X_S * Log_Y_S) / (m * Log_X_X_S - Log_X_S ** 2)

print("\n\nCoeffcinets are ")
print("a = " , np.exp(a0))
print("b = " , a1)

P = np.exp(a0) * (2.7182818) ** (a1 * x)
print("\n\nThe expression of polynomial is " , P)
print("The value of polynomial is " , P.subs(x , Xx))