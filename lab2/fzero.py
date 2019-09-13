#from scipy.optimize import fzero
from math import tan
from zero import zero

def FCN(x):
    #eq = (x*x*x) + 2*(x*x) + 10*x - 20
    eq = x - tan(x)
    return eq

x0 = zero(1,2, 2.220446049250313e-16, 1.0e-12, FCN)
print("x0 ", x0)
