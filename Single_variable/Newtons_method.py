import pandas as pd
import math as m
import sympy as s

(p0 , TOL , N) = (-0.5 , 0.00001 , 30)

data = []
pd.options.display.float_format = "{:,.7f}".format
def f(x):
    return m.cos(m.pi * (x + 1) / 8) + 0.148 * x - 0.9062

def f_der(x0):
    x = s.Symbol('x')
    y = s.cos(s.pi * (x + 1) / 8) + 0.148 * x - 0.9062
    return float(s.diff(y , x).subs(x , x0))


def newtons(p0 , TOL , N):
    i = 1
    
    data.append([0 , p0, 10])

    while i <= N:
        p = p0 - (f(p0) / f_der(p0))

        data.append([i , p , abs(p - p0)])

        if(abs(p - p0) < TOL):
            print("solution is " , round(p , 10) , "after" , i , "iterations")
            break

        i += 1

        p0 = p
    
    table = pd.DataFrame(data , columns = ['n' , 'pn' , 'relative error'])
    print(table.to_string(index = 0))

    if(i - 1 == N):
        print("Method failed after {} iterations".format(N)) 


newtons(p0 , TOL , N)