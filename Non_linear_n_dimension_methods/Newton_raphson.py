import numpy as np
import pandas as pd
import sympy as s 

(n , TOL , N) = (2 , 0.001 , 10)

x = s.Symbol('x')
y = s.Symbol('y')

f1 = x ** 2 + x * y  + y ** 2 - 7
f2 = x ** 3 + y ** 3 - 9

def F(x0):
    x = s.Symbol('x')
    y = s.Symbol('y')
    f1 = x ** 2 + x * y  + y ** 2 - 7
    f2 = x ** 3 + y ** 3 - 9
    f = f1.subs([(x , x0[0]) , (y , x0[1])])
    g = f2.subs([(x , x0[0]) , (y , x0[1])])

    return [[f] , [g]]

def Jacobian(x0):
    x = s.Symbol('x')
    y = s.Symbol('y')
    f1 = x ** 2 + x * y  + y ** 2 - 7
    f2 = x ** 3 + y ** 3 - 9
    F = s.Matrix([f1,f2])
    return F.jacobian([x , y]).subs([ (x , x0[0]) , (y , x0[1])])


x0 = [1.5 , 0.5]
x0 = np.array(x0)

k = 1

data = [[0 , list(x0.reshape(n)) , 100]]

while k <= N:

    F_k = F(x0)
    J = Jacobian(x0)
    J = np.array(J , dtype = float)

    delta_x = -1 * np.dot(np.linalg.inv(J) , F_k)

    x = x0.reshape(2 , 1) + delta_x

    err = np.max(np.abs(delta_x))

    data.append([k , list(x.reshape(n)) , err])

    if err < TOL :
        print("Number of iteration it took is " , k)
        print(x)
        break
    
    for i in range(n):
        x0[i] = x[i]
        
    k += 1

for i in range(len(data)):
    print(data[i])

if (k - 1 == N):
    print("Maximum number of iteration is reached")




