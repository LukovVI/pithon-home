import math
def L(x):
    L = math.sin(math.pi*x/2)/x
    return L
print (round(L(10000000), 3))