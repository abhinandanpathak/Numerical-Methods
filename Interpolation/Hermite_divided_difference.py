import sympy as s

X = [1.3 , 1.6 , 1.9]
Y = [0.620086 , 0.4554022 , 0.2818186]
Y_der = [-0.5220232 , -0.5698959 , -0.5811571]
Xx = 1.5

x = s.Symbol('x')

n = len(X)

# Forming Z
Z = []
for i in range(n):
    Z.append(X[i])
    Z.append(X[i])

# Calculating divided difference
F = []
f = []
for i in range(n):
    f.append(Y[i])
    f.append(Y[i])

F.append(f)


# Calculating Divided difference
for i in range(2*n - 1):
    d = []
    if(i == 0):
        for j in range(1 , 2*n - i):
            if((j - 1) % 2 == 0):
                d.append(Y_der[int((j - 1) / 2)])
            else:    
                d.append((F[i][j] - F[i][j - 1]) / (Z[j + i] - Z[j - 1]))
    else:
        for j in range(1 , 2*n - i):
            d.append((F[i][j] - F[i][j - 1]) / (Z[j + i] - Z[j - 1]))
    
    F.append(d)


print("X:\t\t    " , X)
print("Y:\t\t    " , Y)
print("Y_der\t\t    " , Y_der)

print("\n\n\nDivided Difference table is")
print("Z:\t\t    " , Z)
for i in range(2*n):
    print("F[Z(i)] to F[Z(i+" + str(i) + ")]", F[i])


# Forming a polymomial
P = F[0][0]
for i in range(1 , len(F)):
    d = 1
    for j in range(i):
        d *= (x - Z[j])
    P += F[i][0] * d


# Displaying the result
print("\n\nThe expression of p(x) is " , s.simplify(P))
print("\nThe value of p(x) is " , P.subs(x , Xx))