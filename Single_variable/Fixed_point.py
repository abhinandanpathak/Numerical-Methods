import pandas as pd

(p0 , TOL , N) = (1.5 , 0.0001 , 30)

def g(x):
    return 0.5 * ((10 - (x ** 3)) ** 0.5)

data = []
pd.options.display.float_format = "{:,.10f}".format

def Fixed_point(p0 , TOL , N):
    i = 1
    while i <= N:
        p = g(p0)

        data.append([i , p0 , p , abs(p - p0)])

        if(abs(p - p0) < TOL):
            print("Value of p is : " , round(p , 10))
            break
        i = i + 1
        p0 = p
    
    table = pd.DataFrame(data , columns = ['n' , 'p0' , 'p1' , 'relative error'])
    print(table.to_string(index = 0))


    if (i - 1 == N):
        print("Method failed after {} iterations".format(N))

Fixed_point(p0 , TOL , N)