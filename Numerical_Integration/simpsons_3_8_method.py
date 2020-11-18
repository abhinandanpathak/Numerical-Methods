X = [0 , 0.25 , 0.50 , 0.75 , 1.00 , 1.25 , 1.50 , 1.75 , 2.00 , 2.25]
Y = [0.5 , 0.4923 , 0.4706 , 0.4384 , 0.4 , 0.3596 , 0.32 , 0.2832 , 0.25 , 0.2314]
n = len(X)

h = X[1] - X[0]

def simpsons_3_8(x , y , h):

    area = (y[0] + 3*y[1] + 3*y[2] + y[3]) * (3 * h / 8)

    return area

if __name__ == "__main__":

    i = 0
    S = 0
    while (i < (n - 2)):
        x = [X[i] , X[i + 1] , X[i + 2] , X[i + 3]]
        y = [Y[i] , Y[i + 1] , Y[i + 2] , Y[i + 3]]

        S += simpsons_3_8(x , y , h)
        
        i += 3

    print("\n\nThe integral of curve is " , S)