from math import *

def func(x):
    return sin(x)

def h_val(i):
    return 1/(2**i)

def forward(x, k, N):
    f = open("lab4/outforward", "w+")
    for i in range(k, N+1):
        h = h_val(i)
        fd = (func(x+h) - func(x))/h
        error = abs(fd-cos(x))/cos(x)
        print("FD: ", fd, " k: ", i, " h: ", h, " error: ", error, "\n")
        f.write("%d %f %f\n" % (i, log(h), log(error)))
    f.close()

def centered(x, k, N):
    f = open("lab4/outcentered", "w+")
    for i in range(k, N+1):
        h = h_val(i)
        cd = (func(x+h) - func(x-h))/(2*h)
        error = abs(cd-cos(x))/cos(x)
        print("CD: ", cd, " k: ", i, " h: ", h, " error: ", error, "\n")
        f.write("%d %f %f\n" % (i, log(h), log(error)))
    f.close()


#forward(1, 5, 30)

centered(1, 5, 30)