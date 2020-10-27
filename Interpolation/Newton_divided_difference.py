import sympy as s

X = [1 , 1.3 , 1.6 , 1.9 , 2.2]
Y = [0.7651977 , 0.6200860 , 0.4554022 , 0.2818186 , 0.1103623]
Xx = 1.5

x = s.Symbol('x')

F = []
F.append(Y)


n = len(Y)

# Calculating Divided difference
for i in range(0 , n):
    d = []
    for j in range(1 , n - i):
        d.append((F[i][j] - F[i][j - 1]) / (X[j + i] - X[j - 1]))
    F.append(d)


print("X:\t\t    " , X)
print("Y:\t\t    " , Y)

print("\n\n\nDivided Difference table is")
for i in range(n):
    print("F[X(i)] to F[X(i+" + str(i) + ")]", F[i])

coeff = []
for i in range(n):
    a = F[i][0]
    coeff.append(a)

# Displaying coefficients

print("\n\n\n\nCoefficients are\n")
for i in range(n):
    print("a" + str(i) , " = " , coeff[i])

P = coeff[0]
for i in range(1 , len(coeff)):
    p = 1
    for j in range(i):
        p *= (x - X[j])
    P += coeff[i] * p

print("\n\nThe expression of p(x) is " , s.simplify(P))
print("\n\nThe value if p(x) is " , P.subs(x , Xx))

