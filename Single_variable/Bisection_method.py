import pandas as pd

(a , b , TOL , N) = (0 , 1 , 0.01 , 4)

def f(x):
    return (x ** 3) + (4 * x * x) - 10

data = []
pd.options.display.float_format = "{:,.10f}".format

def bisection(a , b , N = 100 , TOL = 10 ** -5):
    n = 1
    while n <= N:
        p = a + (b - a) / 2

        data.append([n , a , b , p , f(p) , (b - a) / (2 * p)])
        
        if(f(p) == 0 or ((b - a) / 2) < TOL):
            print("Root occurs at {}".format(round(p , 10)))
            break

        
        
        if(f(a) * f(p) < 0):
            b = p
        else:
            a = p
        
        n += 1
    
    table = pd.DataFrame(data , columns = ['n' , 'an' , 'bn' , 'p' , 'f(p)' , 'relative error'])
    print(table.to_string(index = 0))

    
    if(n - 1 == N):
        print("Method failed after {} iterations".format(N))


bisection(a , b , N , TOL)   


