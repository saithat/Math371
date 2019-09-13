from sympy import *

def newton(a, TOL, maxIT):
    n = 0
    x = symbols('x')
    eq = x - tan(x)
    #eq_1 = diff(eq,x)
    eq_1 = 1 - (sec(x)*sec(x))
    x_0 = 0
    x_0 = a
    x_1 = 0
    while n < maxIT:
        n = n+1
        x_1 = x_0 - (eq.subs(x, x_0)/eq_1.subs(x, x_0))
        print("eq: ", eq)
        print("eq_1 ", eq_1)
        print("x_0 ", x_0)
        print("x_1 ", x_1)
        #print("f(x_0): ", eq.subs(x, x_0))
        #print("f'(x_0): ", eq_1.subs(x, x_1))
        if (abs((x_1-x_0)) < TOL):
            return print("Root: ", x_1, " residual: ", 0.0-eq.subs(x, x_1), " iterations: ", n, " \n")
        #eq = eq_1
        x_0 = x_1

newton(98.95006,1e-9, 20)