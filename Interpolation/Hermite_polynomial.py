import sympy as s

X = [1.3 , 1.6 , 1.9]
Y = [0.620086 , 0.4554022 , 0.2818186]
Y_der = [-0.52220232 , -0.5698959 , -0.5811571]
Xx = 1.5

x = s.Symbol('x')

# Step 1
# Calculating lagrange polynomial
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

print("Lagrange polynomial")
for i in range(n):
    print("L_" + str(n - 1) + "_" + str(i) , " = " , s.expand(L[i])) 

print("\nLagrange polynomial derivative")
for i in range(n):
    print("L_der_" + str(n - 1) + "_" + str(i) , " = " , s.expand(s.diff(L[i] , x)))


print("\n\nLagrange polynomial values")
for i in range(n):
    print("L_" + str(n - 1) + "_" + str(i) , " = " , L[i].subs(x , Xx)) 

print("\nLagrange polynomial derivative values")
for i in range(n):
    print("L_der_" + str(n - 1) + "_" + str(i) , " = " , (s.diff(L[i] , x).subs(x , Xx)))

# Step 2
# Defining parameters for Hermite polynomial
A = []
B = []
C = []
D = []
for i in range(n):
    a = -2 * s.diff(L[i] , x).subs(x , X[i])
    b = 1 + 2 * X[i] * s.diff(L[i] , x).subs(x , X[i])
    c = 1
    d = -1 * X[i]
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

# step 3
# Calculating hermite polynomial
H = []
H_cap = []
for i in range(n):
    h = (A[i] * x +  B[i]) * (L[i] ** 2)
    h_cap = (C[i] * x + D[i]) * (L[i] ** 2)
    H.append(s.expand(h))
    H_cap.append(s.expand(h_cap))

# Dispalying the coefficient
print("\n\n")
for i in range(n):
    print("H_" + str(n-1) + "_" + str(i) + " = " , H[i])
    print("\n")
    print("H_cap_" + str(n-1) + "_" + str(i) + " = " , H_cap[i])
    print("\n")

# Step 5
# Forming the polynomial
P = 0
for i in range(n):
    P += Y[i] * H[i] + Y_der[i] * H_cap[i]


# Displaying the result
print("\n\nThe expression of p(x) is " , s.simplify(P))
print("\nThe value of p(x) is " , P.subs(x , Xx))