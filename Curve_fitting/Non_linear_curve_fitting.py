import numpy as np
import sympy as s


n = 2    # Specify the degree of polynomial
X = [0 , 0.25 , 0.50 , 0.75 , 1.00]
Y = [1.0000 , 1.2840 , 1.6487 , 2.1170 , 2.7183]
Xx = 1.25

m = len(X)

x = s.Symbol('x')

# Getting the coefficinets
Coeff = []
for i in range(n + 1):
    a = s.Symbol('a' + str(i))
    Coeff.append(a)

# Forming the mean squared error equations
E = 0
for i in range(m):
    eqn = Coeff[0]
    for j in range(1 , n + 1):
        eqn += Coeff[j] * (X[i] ** j)
    E += (Y[i] - eqn) ** 2


# Forming n equation by calculating derivative w.r.t coefficients
Equations = []
for i in range(n + 1):
    eqn = s.diff(E , Coeff[i])
    Equations.append(eqn)

# Displaying the equations
print("\n\nEquations to be solved are\n")
for i in range(n + 1):
    print(Equations[i] , " = 0" )

# Coefficients after solving equations are
A = []
for i in range(n + 1):
    A.append(np.power(X , i))
A = np.array(A)

inv = np.linalg.inv(np.dot(A , A.transpose()))
p = np.dot(A , np.reshape(Y , [len(Y) , 1]))

coeff = np.dot(inv , p)

print("\n\nCoefficients are")
for i in range(n + 1):
    print("a" + str(i) + " = " , coeff[i])

P = coeff[0][0]
for i in range(1 , n + 1):
    P += coeff[i][0] * (x ** i)

print("\n\nThe expression of polynomial is " , P)
print("The value of polynomial is " , P.subs(x , Xx))

Error = 0
for i in range(m):
    Error += (Y[i] - P.subs(x , X[i])) ** 2

print('The error is: ' , Error  )










