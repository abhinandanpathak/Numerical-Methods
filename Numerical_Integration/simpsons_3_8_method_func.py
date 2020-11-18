from __future__ import print_function
import numpy as np
from simpsons_3_8_method import simpsons_3_8

def print(*args):
    __builtins__.print(*("%.8f" % a if isinstance(a, float) else a for a in args))

[a , b] = [0 , 2]

def f(x):

    return 2 / (x**2 + 4)

N = 9

X = np.linspace(a , b , 9 + 1)
Y = f(X)

if __name__ == "__main__":

    n = len(X)
    h = (b - a) / N

    i = 0
    S = 0
    while (i < (n - 2)):
        x = [X[i] , X[i + 1] , X[i + 2] , X[i + 3]]
        y = [Y[i] , Y[i + 1] , Y[i + 2] , Y[i + 3]]

        S += simpsons_3_8(x , y , h)
        
        i += 3
    
    print("X\t\t  Y")
    for i in range(len(X)):
        print(X[i] , "\t" , Y[i])
    
    print("\n\nThe integral of curve is " , S)

