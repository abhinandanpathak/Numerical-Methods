import pandas as pd
import math as m
import sympy as s

(p0 , TOL , N) = (1.5 , 0.0000001 , 30)

data = []
pd.options.display.float_format = "{:,.10f}".format
def f(x):
    return (x ** 3) + (4 * x ** 2) - 10

def f_der(x0):
    x = s.Symbol('x')
    y = (x ** 3) + (4 * x ** 2) - 10
    return float(s.diff(y , x).subs(x , x0))

def f_der2(x0):
    x = s.Symbol('x')
    y = (x ** 3) + (4 * x ** 2) - 10
    return float(s.diff(s.diff(y , x) , x).subs(x , x0))


def Modified_newtons(p0 , TOL , N):
    i = 1
    
    data.append([0 , p0, 10])

    while i <= N:
        p = p0 - ((f(p0) * f_der(p0)) / ((f_der(p0) ** 2) - (f(p0) * f_der2(p0))))

        data.append([i , p , abs(p - p0)])

        if(abs(p - p0) < TOL):
            print("solution is " , round(p , 10))
            break

        i += 1

        p0 = p
    
    table = pd.DataFrame(data , columns = ['n' , 'pn' , 'relative error'])
    print(table.to_string(index = 0))

    if(i - 1 == N):
        print("Method failed after {} iterations".format(N)) 


Modified_newtons(p0 , TOL , N)