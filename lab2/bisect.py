import math

def bisect(a, b, TOL, maxIT):
    n = 0
    while n <= maxIT:
        #print("a: ", a, "b: ", b, "\n")
        n = n+1
        mid = (a+b)/2
        Fa = FCN(a)
        Fb = FCN(b)
        Fmid = FCN(mid)

        print(n, "\t",mid, "\t", Fmid, "\t",(b-a), "\n")
        #print("Fa: ", Fa, " Fb", Fb, "\n")

        if ((Fmid == 0) | ((b-a)/2 < TOL)):
            return print("DONE:root=",mid, "residual=", (0-Fmid), "in", n, "iters\n")
                                                                                                                                                                                                                              
        if((Fb < 0) & (Fmid > 0) | ((Fb > 0) & (Fmid < 0))):
            a = mid
        else:
            b = mid
    print("Convergence failed\n")

def FCN(x):
    eq = (x*x*x) + 2*(x*x) + 10*x - 20
    #eq = 1.3-x
    return eq

bisect(1, 2, 1e-12, 100)