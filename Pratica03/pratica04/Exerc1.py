from math import sqrt,log,exp
x = float(input())

if x <= 1:
    print(log(x))
elif 1 < x <= 2:
    print(log(10,x)+ sqrt(x))
elif 2 < x <= 5:
    print(x**2 + exp**x)
elif x > 5:
    print(x**x/2 + log(2,x))