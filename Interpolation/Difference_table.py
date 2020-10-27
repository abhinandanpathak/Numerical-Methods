import numpy as np

X = [1 , 2 , 3 , 4 , 5 , 6]
Y = [10 , 30 , 30 , 40 , 50 , 60]

def Forward_diff(X , Y):
    print("Forward difference table\n")

    n = len(Y)

    forward_diff = []
    y = Y
    for i in range(n - 1):
        diff = np.diff(y)
        forward_diff.append(diff)
        y = diff
    

    print("X:     " , X)
    print("Y:     " , Y)
    for i in range(n - 1):
        print("delta_" + str(i + 1) , forward_diff[i])
    return forward_diff


def Backward_diff(X , Y):
    print("\n\n\nBackward difference table\n")
    n = len(Y)
    backward_diff = []
    y = Y
    for i in range (n -1):
        data = -1 * np.diff(y)
        backward_diff.append(data)
        y = data

    print("X:     " , X)
    print("Y:     " , Y)
    for i in range(n - 1):
        print("delta_" + str(i + 1) , backward_diff[i])
    return Forward_diff(X , Y)

if __name__ == "__main__":
    Forward_diff(X , Y)
    Backward_diff(X , Y)


