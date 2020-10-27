import sympy as s
from Difference_table import Forward_diff
from math import factorial

X = [1 , 1.02 , 1.04 , 1.06 , 1.08]
Y = [0.242 , 0.2371 , 0.2323 , 0.2275 , 0.2227]
Xx = 1.015

x = s.Symbol('x')

f_diff = Forward_diff(X , Y)

h = X[1] - X[0]

coeff = []
coeff.append(Y[0])

n = len(Y)

for i in range(1 , n):
    a  = (f_diff[i - 1][0] / (factorial(i) * (h**i)))
    coeff.append(a)

# Displaying coefficients

print("\n\n\n\nCoefficients are\n")
for i in range(n):
    print("a" + str(i) , " = " , coeff[i])
    

u = (x - X[0]) / h

# Calcualting P(x)
P = 0
for k in range(1 , n):
    U = u
    for i in range(1 , k):
        U *= (u - i)
    P += (U * f_diff[k - 1][0]) / factorial(k)
P = P + Y[0]

print("\n\nThe expression of p(x) is " , s.simplify(P))
print("\n\nThe value of p(x) is " , P.subs(x , Xx))