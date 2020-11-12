from __future__ import print_function
import numpy as np
def print(*args):
    __builtins__.print(*("%.6f" % a if isinstance(a, float) else a for a in args))


# Setting initial parameters
(x0 , xn) = (0 , 2)
h = 0.2
y0 = 0.5
(L , M) = (1 , 0.5*np.exp(2) - 2)

# Calcualting N
N = int((xn - x0) / h)

# Defining the function f(x , y)
def f(x , y):
    return (y - x**2 + 1)

# Defining function for EXACT solution
def F(x):
    return ((x + 1) ** 2) -0.5 * np.exp(x)

# Running loop to calulate
bound = 0
a = x0
print("n\t\txn\t\t\tyn\t\t\tExact Solution\t\tAbsolute Error\t\tUpper Bound")
print(0 , "\t\t" , x0 , "\t\t\t" , y0 , "\t\t" , F(x0) , "\t\t" , np.abs(F(x0) - y0) , "\t\t" , bound)

for n in range(1 , N + 1):

    x_n_1 = x0 + h
    y_n_1 = y0 + h * f(x0 , y0)

    Y_N_1 = F(x_n_1)
    error = np.abs(y_n_1 - Y_N_1)

    bound = ((h * M) / (2 * L)) * (np.exp(L * (x_n_1 - a)) - 1)

    print(n , "\t\t" , x_n_1 , "\t\t" , y_n_1 , "\t\t" , Y_N_1 , "\t\t" , error , "\t\t" , bound)

    x0 = x_n_1
    y0 = y_n_1


