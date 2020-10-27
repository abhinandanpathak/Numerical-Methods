X = [1 , 1.05 , 1.10 , 1.15 , 1.20 , 1.25]
Y = [0.682689 , 0.706282 , 0.728668 , 0.749856 , 0.769861 , 0.788700]

n = len(Y)

h = X[1] - X[0]

#################################################################
# TWO POINT APPROXIMATION

print("\n\nTwo point approximation of derivative")
print("\nx0\tForward Difference f'(x0)")

Forward_difference = []
Backward_difference = []

for i in range(n - 1):
    FD = (Y[i + 1] - Y[i]) / h
    Forward_difference.append(FD)

for i in range(1 , n):
    BD = (Y[i] - Y[i - 1]) / h
    Backward_difference.append(BD)

for i in range(n - 1):
    print(X[i] , "\t" , Forward_difference[i])

print("\nx0\tBackward Difference f'(x0)")

for i in range(1 , n):
    print(X[i] , "\t" , Backward_difference[i - 1])


#################################################################
#THREE POINT APPROXIMATION

print("\n\nThree point approximation")

Right_end = []

for i in range(n - 2):
    re = (-3 * Y[i] + 4 * Y[i + 1] - Y[i + 2]) / (2 * h)
    Right_end.append(re)

print("\nx0\tRight end approximation f'(x0)")

for i in range(n - 2):
    print(X[i] , "\t" , Right_end[i])



Mid_Point = []

for i in range(1 , n - 1):
    m = (Y[i + 1] - Y[i - 1]) / (2 * h)
    Mid_Point.append(m)

print("\nx0\tMid_point approximation f'(x0)")

for i in range(1 , n - 1):
    print(X[i] , "\t" , Mid_Point[i - 1])



Left_end = []

for i in range(2 , n):
    le = (3 * Y[i] - 4 * Y[i - 1] + Y[i - 2]) / (2 * h)
    Left_end.append(le)

print("\nx0\tLeft end approximation f'(x0)")

for i in range(n - 2):
    print(X[i + 2] , "\t" , Left_end[i])



#################################################################
# FIVE POINT APPROXIMATION
print("\n\nFive point approximation")

Right_end = []

for i in range(n - 4):
    re = (-25 * Y[i] + 48 * Y[i + 1] -36 * Y[i + 2] + 16 * Y[i + 3] - 3 * Y[i + 4]) / (12 * h)
    Right_end.append(re)

print("\nx0\tRight end approximation f'(x0)")

for i in range(n - 4):
    print(X[i] , "\t" , Right_end[i])



Mid_Point = []

for i in range(2 , n - 2):
    m = (Y[i - 2] -8 * Y[i - 1] + 8 * Y[i + 1] - Y[i + 2]) / (12 * h)
    Mid_Point.append(m)

print("\nx0\tMid_point approximation f'(x0)")

for i in range(2 , n - 2):
    print(X[i] , "\t" , Mid_Point[i - 2])



Left_end = []

for i in range(4 , n):
    le = (25 * Y[i] - 48 * Y[i - 1] + 36 * Y[i - 2] - 16 * Y[i - 3] + 3 * Y[i - 4]) / (12 * h)
    Left_end.append(le)

print("\nx0\tLeft end approximation f'(x0)")

for i in range(n - 4):
    print(X[i + 4] , "\t" , Left_end[i])




#################################################################
# THREE POINT APPROXIMATION FOR SECOND DERIVATIVE

print("\n\nThree point approximation for second derivative")
MID_POINT_SD = []

for i in range(1 , n - 1):
    ss = (Y[i - 1] - 2 * Y[i] + Y[i + 1]) / (h * h)
    MID_POINT_SD.append(ss)

print("\nx0\tMid Point approximation f''(x0)")

for i in range(1 , n - 1):
    print(X[i] , "\t" , MID_POINT_SD[i - 1])

