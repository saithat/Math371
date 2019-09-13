from scipy.optimize import fzero
from math import tan

def FCN(x):
    eq = (x*x*x) + 2*(x*x) + 10*x - 20
    #eq = x - tan(x)
    return eq

x0 = fsolve(FCN, )