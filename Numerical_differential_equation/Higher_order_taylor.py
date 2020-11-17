from __future__ import print_function
import numpy as np
import sympy as s
from math import factorial
def print(*args):
    __builtins__.print(*("%.6f" % a if isinstance(a, float) else a for a in args))


# Setting initial parameters
(t0 , tn) = (0 , 2)
h = 0.2
y0 = 0.5
n = 4

t , y = s.symbols('t y')
f = y - t**2 + 1
# Manually enter the derivatives
der1 = f
der2 = y - t**2 + 1 - 2*t
der3 = y - t**2  -2*t - 1
der4 = y - t**2 - 2*t - 1

der = [der1 , der2 , der3 , der4]

# Defining function for EXACT solution
def F(x):
    return ((x + 1) ** 2) -0.5 * np.exp(x)

# Calcualting N
N = int((tn - t0) / h)


# Defining the function T(t , y , h , n)
def T(t0 , y0 , h , n):

    T = der[0]
    for i in range(1 , n):
        T += ((h ** i) * (der[i])) / (factorial(i + 1))
    
    return T.subs([(t , t0) , (y , y0)])




print("n\t\ttn\t\t\tyn\t\t\tExact Solution\t\tAbsolute Error")
print(0 , "\t\t" , t0 , "\t\t\t" , y0 , "\t\t" , F(t0) , "\t\t" , np.abs(F(t0) - y0) )

# Running loop to calculate
for i in range(1 , N + 1):

    # Calculating next values
    t_n_1 = t0 + h
    y_n_1 = float (y0 + h * T(t0 , y0 , h , n))

    # Calculating exact solution
    Y_N_1 = F(t_n_1)

    # Calculating absolute error
    error = np.abs(y_n_1 - Y_N_1)

    # Displaying the result of each iterations
    print(i , "\t\t" , t_n_1 , "\t\t" , y_n_1 , "\t\t" , Y_N_1 , "\t\t" , error)

    # Updating the parameters
    t0 = t_n_1
    y0 = y_n_1
