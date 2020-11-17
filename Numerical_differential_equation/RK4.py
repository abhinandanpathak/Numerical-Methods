from __future__ import print_function
import numpy as np
def print(*args):
    __builtins__.print(*("%.6f" % a if isinstance(a, float) else a for a in args))


# Setting initial parameters
(t0 , tn) = (0 , 2)
h = 0.2
y0 = 0.5

# Defining function for EXACT solution
def F(t):
    return ((t + 1) ** 2) -0.5 * np.exp(t)

# Defining the function f(t , y)
def f(t , y):
    return (y - t**2 + 1)

# Calcualting N
N = int((tn - t0) / h)

# Defining the function T(t0 , y0)
def T(t0 , y0 , h):
    k1 = h * f(t0 , y0)
    k2 = h * f(t0 + h / 2 , y0 + k1 / 2)
    k3 = h * f(t0 + h / 2 , y0 + k2 / 2)
    k4 = h * f(t0 + h , y0 + k3)

    return (k1 , k2 , k3 , k4)


print("n\t\ttn\t\t\tyn\t\t\tExact Solution\t\tAbsolute Error")
print(0 , "\t\t" , t0 , "\t\t\t" , y0 , "\t\t" , F(t0) , "\t\t" , np.abs(F(t0) - y0))

# Running loop to calculate
for n in range(1 , N + 1):

    # Calculating next values
    t_n_1 = t0 + h
    (k1 , k2 , k3 , k4) = T(t0 , y0 , h)
    y_n_1 = y0 + (k1 + 2*k2 + 2*k3 + k4) / 6

    # Calculating exact solution
    Y_N_1 = F(t_n_1)

    # Calculating absolute error
    error = np.abs(y_n_1 - Y_N_1)

    # Displaying the result of each iterations
    print(n , "\t\t" , t_n_1 , "\t\t" , y_n_1 , "\t\t" , Y_N_1 , "\t\t" , error)

    # Updating the parameters
    t0 = t_n_1
    y0 = y_n_1


