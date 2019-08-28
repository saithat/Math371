import math
series = 0
i = 1
while 1:
    #if(abs(pow(-0.9,i+1)/(i+1)) <= 1e-10):
    if(abs(pow(0.3, (2*i))/((2*i))) <= 1e-10):
        print("i is: ", i)
        break
    i = i+1