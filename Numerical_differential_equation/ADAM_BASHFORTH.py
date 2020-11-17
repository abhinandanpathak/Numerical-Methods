from __future__ import print_function
import numpy as np
def print(*args):
    __builtins__.print(*("%.7f" % a if isinstance(a, float) else a for a in args))


# Setting initial parameters
(t0 , tn) = (0.0 , 2)
h = 0.2
k = 3
y = ()
t = ()
if(k == 1):
    (y0 , y1) = (0.5 , 0.829293)
    y = (y0 , y1)
    t = (t0 , t0 + h)
elif(k == 2):
    (y0 , y1 , y2) = (0.5 , 0.829293 , 1.214076)
    y = (y0 , y1 , y2)
    t = (t0 , t0 + h , t0 + 2 * h)
else:
    y0 , y1 , y2 , y3 = (0.5 , 0.829293 , 1.214076 , 1.648922)
    y = (y0 , y1 , y2 , y3)
    t = (t0 , t0 + h , t0 + 2*h , t0 + 3*h)


# Defining function for EXACT solution
def F(t):
    return ((t + 1) ** 2) -0.5 * np.exp(t)

# Defining the function f(t , y)
def f(t , y):
    return (y - t**2 + 1)

# Calcualting N
N = int((tn - t0) / h)

# Defining the function T(t0 , y0)
def T(t , y , h , k):
    if(k == 1):
        T_approx = (3 * f(t[1] , y[1]) - f(t[0] , y[0])) / 2
    
    elif(k == 2):
        T_approx = (23 * f(t[2] , y[2]) - 16 * f(t[1] , y[1]) + 5 * f(t[0] , y[0])) / 12
    else:
        T_approx = (55 * f(t[3] , y[3]) - 59 * f(t[2] , y[2]) + 37 * f(t[1] , y[1]) - 9 * f(t[0] , y[0]) ) / 24

    return T_approx

print("n\t\ttn\t\t\tyn\t\t\tExact Solution\t\tAbsolute Error")
if(k == 1):
    print(0 , "\t\t" , t[0] , "\t\t" , y[0] , "\t\t" , F(t[0]) , "\t\t" , np.abs(F(t[0]) - y[0]))
    print(1 , "\t\t" , t[1] , "\t\t" , y[1] , "\t\t" , F(t[1]) , "\t\t" , np.abs(F(t[1]) - y[1]))
elif(k == 2):
    print(0 , "\t\t" , t[0] , "\t\t" , y[0] , "\t\t" , F(t[0]) , "\t\t" , np.abs(F(t[0]) - y[0]))
    print(1 , "\t\t" , t[1] , "\t\t" , y[1] , "\t\t" , F(t[1]) , "\t\t" , np.abs(F(t[1]) - y[1]))
    print(2 , "\t\t" , t[2] , "\t\t" , y[2] , "\t\t" , F(t[2]) , "\t\t" , np.abs(F(t[2]) - y[2]))
else:
    print(0 , "\t\t" , t[0] , "\t\t" , y[0] , "\t\t" , F(t[0]) , "\t\t" , np.abs(F(t[0]) - y[0]))
    print(1 , "\t\t" , t[1] , "\t\t" , y[1] , "\t\t" , F(t[1]) , "\t\t" , np.abs(F(t[1]) - y[1]))
    print(2 , "\t\t" , t[2] , "\t\t" , y[2] , "\t\t" , F(t[2]) , "\t\t" , np.abs(F(t[2]) - y[2]))
    print(3 , "\t\t" , t[3] , "\t\t" , y[3] , "\t\t" , F(t[3]) , "\t\t" , np.abs(F(t[3]) - y[3]))


# Running loop to calculate
for n in range(k + 1 , N + 1):

    # Calculating next values
    t_n_1 = t[len(t) - 1] + h
    y_n_1 = y[len(y) - 1] + h * T(t , y , h , k)

    # Calculating exact solution
    Y_N_1 = F(t_n_1)

    # Calculating absolute error
    error = np.abs(y_n_1 - Y_N_1)

    # Displaying the result of each iterations
    print(n , "\t\t" , t_n_1 , "\t\t" , y_n_1 , "\t\t" , Y_N_1 , "\t\t" , error)

    # Updating the parameters
    if(k == 1):
        y = (y[1] , y_n_1)
        t = (t[1] , t_n_1)
    elif(k == 2):
        y = (y[1] , y[2] , y_n_1)
        t = (t[1] , t[2] , t_n_1)
    else:
        y = (y[1] , y[2] , y[3] , y_n_1)
        t = (t[1] , t[2] , t[3] , t_n_1)



