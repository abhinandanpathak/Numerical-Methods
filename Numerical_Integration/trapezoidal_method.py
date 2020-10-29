X = [7.47 , 7.48 , 7.49 , 7.50 , 7.51 , 7.52]
Y = [1.93 , 1.95 , 1.98 , 2.01 , 2.03 , 2.06]
n = len(X)

h = X[1] - X[0]

def trapezoidal(X , Y , h):

    area = (Y[1] + Y[0]) * (h / 2)

    return area

if __name__ == "__main__":

    i = 0
    S = 0
    while (i < n - 1):
        x = [X[i] , X[i + 1]]
        y = [Y[i] , Y[i + 1]]

        S += trapezoidal(x , y , h)

        i += 1

    print("\n\nThe integral of curve is " , S)




