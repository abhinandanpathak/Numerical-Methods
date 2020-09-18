import math as m
import pandas as pd

(p0 , p1 , p2 , TOL , N) = (0.5 , 1 , 1.5 , 0.00001 , 14)

def f(x):
    return (x ** 4) - (3 * (x ** 3)) + (x ** 2) + x + 1


def Mullers(p0 , p1 , p2 , TOL , N):

    h1 = p1 - p0
    h2 = p2 - p1
    delta1 = (f(p1) - f(p0)) / h1
    delta2 = (f(p2) - f(p1)) / h2
    d = (delta2 - delta1) / (h2 + h1)
    
    i = 3


    data = []
    pd.options.display.float_format = "{:,.10f}".format

    data.append([0 , p0 , f(p0)])
    data.append([1 , p1 , f(p1)])
    data.append([2 , p2 , f(p2)])
    while i <= N:
        b = delta2 + h2 * d
        D = (b ** 2 - 4 * f(p2) * d) ** 0.5

        if (abs(b - D) < abs(b + D)):
            E = b + D
        else:
            E = b - D

        h = (-2 * f(p2)) / E
        p = p2 + h

        if(abs(h) < TOL):
            print("Solution is " , p)
            break

        p0 = p1
        p1 = p2
        p2 = p
        h1 = p1 - p0
        h2 = p2 - p1
        delta1 = (f(p1) - f(p0)) / h1
        delta2 = (f(p2) - f(p1)) / h2
        d = (delta2 - delta1) / (h2 + h1)
        

        data.append([i , p2 , f(p2)])
        i += 1

    table = pd.DataFrame(data , columns = ['n' , 'pn' , 'f(pn)'])
    print(table.to_string(index = 0))


    if(i -1 == N):
        print("Solution failed after {} iterations".format(N))
     
Mullers(p0 , p1 , p2 , TOL , N)