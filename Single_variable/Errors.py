true_value  = 0.3926

approximate_value = 0.375

relative_error = 4.5

i = 1

if (i ==  1):
    relative_error = abs((true_value - approximate_value) / (true_value)) * 100
    print("Relative error is " , relative_error , "%")

if (i == 2):
    tv1 = (approximate_value) / (1 - relative_error / 100)
    tv2 = (approximate_value) / (1 + relative_error / 100)
    print("true value is " , tv1)
    print("true value is " , tv2)

if (i == 3):
    ap1 = true_value * (1 - relative_error / 100)
    ap2 = true_value * (1 + relative_error / 100)
    print("true value is " , ap1)
    print("true value is " , ap2)



