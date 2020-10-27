import numpy as np
import pandas as pd

(n , TOL , N) = (3 , 0.001 , 200)

x0 = np.ones(shape = n)

a = [[10 , 5 , 3.75] , [5 , 3.75 , 3.125] , [3.75 , 3.125 , 2.765625]]
b = [[17.536] , [10.9028] , [8.803075]]

a = np.array(a)
b = np.array(b)

pd.options.display.float_format = "{:,.3f}".format

def Gauss_siedel(n  , TOL , N , a , b , x0):

    k = 1
    var =  []
    for i in range(n):
        var.append('x' + str(i + 1))

    x = np.zeros(shape = n)
    
    data = []
    data.append([0 , list(x) , 100])

    while k <= N :

        for i in range(n):
            s = 0
            for j in range(i):
                if(i == j):
                    continue
                else:
                    s += a[i][j] * x[j]
            for j in range(i + 1 , n):
                if(i == j):
                    continue
                else:
                    s += a[i][j] * x0[j]

            x[i] = (-s + b[i]) / (a[i][i])
            
            
        err = np.max(np.abs(x - x0))
        
        data.append([k , list(np.round(x , 4)) , err])

        if (err < TOL):
            print("Number of iteration it took is :" , k)
            print("x = " , np.round(x , 4))
            break

        k += 1

        for i in range(n):
            x0[i] = x[i]

    table = pd.DataFrame(data , columns = ['k' , tuple(var), 'relative error'])
    print(table.to_string(index = 0))
    

    if (k - 1 == N):
        print("Maximum number of iteration exceeded")

Gauss_siedel(n , TOL , N , a , b , x0)
