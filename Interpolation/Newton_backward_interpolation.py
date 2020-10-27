import sympy as s
from Difference_table import Forward_diff
from math import factorial

X = [1 , 1.05 , 1.10 , 1.15 , 1.20 , 1.25]
Y = [0.682689 , 0.706282 , 0.728668 , 0.749856 , 0.769861 , 0.788700]
Xx = 1.235

x = s.Symbol('x')

f_diff = Forward_diff(X , Y)


h = X[1] - X[0]

n = len(Y) 

coeff = []
coeff.append(Y[n - 1])

for i in range(1 , n):
    l = len(f_diff[i - 1])
    a  = (f_diff[i - 1][l - 1] / (factorial(i) * (h**i)))
    coeff.append(a)

# Displaying coefficients

print("\n\n\n\nCoefficients are\n")
for i in range(n):
    print("a" + str(i) , " = " , coeff[i])



u = (x - X[n - 1]) / h


# Calcualting P(x)
P = 0
for k in range(1 , n):
    U = u
    for i in range(1 , k):
        U *= (u + i)
    l = len(f_diff[k - 1])
    P += (U * f_diff[k - 1][l - 1]) / factorial(k)
P = P + Y[n - 1]

print("\n\nThe expression of p(x) is " , s.simplify(P))
print("\nThe value of p(x) is " , P.subs(x , Xx))
