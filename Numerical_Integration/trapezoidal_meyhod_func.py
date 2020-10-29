from __future__ import print_function
import numpy as np
from trapezoidal_method import trapezoidal

def print(*args):
    __builtins__.print(*("%.8f" % a if isinstance(a, float) else a for a in args))

[a , b] = [0 , 2]

def f(x):

    return 2 / (x**2 + 4)

N = 8

X = np.linspace(a , b , N + 1)

Y = f(X)

n = len(X)
h = (b - a) / N

i = 0
S = 0
while (i < n - 1):
    x = [X[i] , X[i + 1]]
    y = [Y[i] , Y[i + 1]]

    S += trapezoidal(x , y , h)

    i += 1

print("X\t\t  Y")
for i in range(len(X)):
    print(X[i] , "\t" , Y[i])

print("\n\nThe integral of curve is " , S)