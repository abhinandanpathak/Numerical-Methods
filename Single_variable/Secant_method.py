import pandas as pd
import math as m

(p0 , p1 , TOL , N) = (0.5 , m.pi / 4 , 0.0000001 , 30)

data = []
pd.options.display.float_format = "{:,.10f}".format
def f(x):
    return m.cos(x) - x


def secant(p0 , p1 , TOL , N):
    i = 2
    q0 = f(p0)
    q1 = f(p1)

    data.append([0 , p0, 10])
    data.append([1 , p1 , 10])
    while i <= N:
        p = p1 - (q1 * (p1 - p0) / (q1 - q0))

        data.append([i , p , abs(p - p1)])

        if(abs(p - p1) < TOL):
            print("solution is " , round(p , 10))
            break

        i += 1

        p0 = p1
        p1 = p
        q0 = q1
        q1 = f(p)
    
    table = pd.DataFrame(data , columns = ['n' , 'pn' , 'relative error'])
    print(table.to_string(index = 0))

    if(i - 1 == N):
        print("Method failed after {} iterations".format(N)) 


secant(p0 , p1 , TOL , N)