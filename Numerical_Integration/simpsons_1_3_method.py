X = [0 , 0.25 , 0.50 , 0.75 , 1.00 , 1.25 , 1.50 , 1.75 , 2.00]
Y = [0.5 , 0.4923 , 0.4706 , 0.4384 , 0.4 , 0.3596 , 0.32 , 0.2832 , 0.25]
n = len(X)

h = X[1] - X[0]

def simpsons_1_3(x , y , h):

    area = (y[0] + 4*y[1] + y[2]) * (h / 3)

    return area


if __name__ == "__main__":

    i = 0
    S = 0
    while (i < (n - 2)):
        x = [X[i] , X[i + 1] , X[i + 2]]
        y = [Y[i] , Y[i + 1] , Y[i + 2]]

        S += simpsons_1_3(x , y , h)
        
        i += 2

    print("\n\nThe integral of curve is " , S)