from __future__ import print_function
import numpy as np
def print(*args):
    __builtins__.print(*("%.6f" % a if isinstance(a, float) else a for a in args))


# Setting initial parameters
(t0 , tn) = (0 , 2)
h = 0.2
y0 = 0.5
(L , M) = (1 , 0.5*np.exp(2) - 2)

# Calcualting N
N = int((tn - t0) / h)

# Defining the function f(t , y)
def f(t , y):
    return (y - t**2 + 1)

# Defining function for EXACT solution
def F(t):
    return ((t + 1) ** 2) -0.5 * np.exp(t)

# Used in calculating upper bound
bound = 0
a = t0      

print("n\t\ttn\t\t\tyn\t\t\tExact Solution\t\tAbsolute Error\t\tUpper Bound")
print(0 , "\t\t" , t0 , "\t\t\t" , y0 , "\t\t" , F(t0) , "\t\t" , np.abs(F(t0) - y0) , "\t\t" , bound)

# Running loop to calculate
for n in range(1 , N + 1):

    # Calculating next values
    t_n_1 = t0 + h
    y_n_1 = y0 + h * f(t0 , y0)

    # Calculating exact solution
    Y_N_1 = F(t_n_1)

    # Calculating absolute error
    error = np.abs(y_n_1 - Y_N_1)

    # Calculating upper bound
    bound = ((h * M) / (2 * L)) * (np.exp(L * (t_n_1 - a)) - 1)

    # Displaying the result of each iterations
    print(n , "\t\t" , t_n_1 , "\t\t" , y_n_1 , "\t\t" , Y_N_1 , "\t\t" , error , "\t\t" , bound)

    # Updating the parameters
    t0 = t_n_1
    y0 = y_n_1


