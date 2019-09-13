import math
N = int(input("Enter N terms to compute: "))
series = 0
for i in range(1,N):
    #series A
    #series += pow(-0.9,i)/i
    #if(abs(pow(-0.9,i)/i) < 1e-10):
    #    print("N is: ", i)
    #series B
    series += pow(0.310345, (2*i)-1)/((2*i)-1)
    if(abs(pow(0.310345, (2*i)-1)/((2*i)-1)) < 1e-10):
        print("N is: ", i)

#series A
#series = -series
#series B
series = series * 2

true_value = math.log(1.9)

error = true_value - series


print("N: ", N, " sum: ", series, " error: ", error)

