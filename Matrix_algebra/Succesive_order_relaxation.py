import numpy as np
import pandas as pd

(n , TOL , N , omega) = (3 , 0.001 , 15 , 1.25)

x0 = np.ones(shape = n)

a = [[4 , 3 , 0] , [3 , 4 , -1] , [0 , -1 , 4]]
b = [[24] , [30] , [-24]]

a = np.array(a)
b = np.array(b)

pd.options.display.float_format = "{:,.3f}".format

def SOR(n  , TOL , N , a , b , x0 , omega):

    k = 1
    var =  []
    for i in range(n):
        var.append('x' + str(i + 1))

    x = np.zeros(shape = n)
    
    data = []
    data.append([0 , list(x) , 100])

    r = np.zeros(n)

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

            r[i] = b[i] - s - (a[i][i] * x0[i])

            x[i] = x0[i] + ((omega * r[i]) / a[i][i])
            
            
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

SOR(n , TOL , N , a , b , x0 , omega)