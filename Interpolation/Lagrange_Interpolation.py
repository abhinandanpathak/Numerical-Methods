import sympy as s

X = [2 , 2.75 , 4]
Y = [1/2 , 1/2.75 , 1/4 ]
Xx = 3

x = s.Symbol('x')

n = len(Y)

L = []

for k in range(n):
    N = 1
    D = 1
    for i in range(n):
        if(k == i):
            continue

        else:
            N *= (x - X[i])
            D *= (X[k] - X[i])
    L.append(N / D)
print("X:\t\t    " , X)
print("Y:\t\t    " , Y)
print("\n\n")
# Displaying coefficients
for i in range(n):
    print("L_" + str(n - 1) + "_" + str(i) , " = " , s.expand(L[i])) 

# Displaying coefficients
print("\n\n")
for i in range(n):
    print("L_" + str(n - 1) + "_" + str(i) , " = " , L[i].subs(x , Xx))


# Calculating result
P = 0
for i in range(len(L)):
    P += L[i] * Y[i]
 
print("\n\nThe expression of p(x) is " , s.simplify(P))
print("\nThe value of p(x) is " , P.subs(x , Xx))