from __future__ import print_function
import numpy as np
from simpsons_1_3_method import simpsons_1_3

def print(*args):
    __builtins__.print(*("%.8f" % a if isinstance(a, float) else a for a in args))

[a , b] = [0 , 2]
N = 8

def f(x):

    return 2 / (x**2 + 4)

X = np.linspace(a , b , N + 1)
Y = f(X)

if __name__ == "__main__":

    n = len(X)

    h = (b - a) / N
    
    i = 0
    S = 0
    while (i < (n - 2)):
        x = [X[i] , X[i + 1] , X[i + 2]]
        y = [Y[i] , Y[i + 1] , Y[i + 2]]

        S += simpsons_1_3(x , y , h)
        
        i += 2

    print("X\t\t  Y")
    for i in range(len(X)):
        print(X[i] , "\t" , Y[i])
    print("\n\nThe integral of curve is " , S)

