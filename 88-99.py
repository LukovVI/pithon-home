#88
import re
print(re.split('[^a-z]', input().lower()))

#89
s = input().split()
n = []
for i in s:
    n.append(i[0])
print(*n)

#90
import numpy as np
M = []
R = []
for i in range(int(input())):
    *m, r = list(map(float, input().split()))
    M.append(m)
    R.append(r)
M1 = np.array(M)
v1 = np.array(R)
if np.linalg.det(M1):
    print(*np.linalg.solve(M1, v1))
else:
    print("Матрица системы вырожденная")

#91
a, b = list(map(int, input().split()))
if b<=a and a%2 == b%2:
    print(*[(a+b)//2, (a-b)//2])
else:
    print("Такой класс не существует")

#92
def f(x):
    return x**2+2*x+1

#93
def g(x):
    return int(f(x))

#94
def S(x):
    return (25 + 10 * 5 ** (1 / 2)) ** (1 / 2) / 4 * x ** 2 * 12 + 20 * (a * a * 3 ** (1 / 2) * 3 / 2)
def S_ceil(x):
    return int(S(x) + 0.99)

#95
def f(x):
    return (x+a)**2-b
def g(x):
    return abs(f(x))

#96
from scipy.optimize import golden
def f(x):
    return (x+a)**2-b
def g(x):
    return abs(f(x))
min_f = f(golden(f, brack = (-10, -4)))
min_g = g(golden(g, brack = (-10, -4)))
print(min_f, min_g)

#97
print(round(100/int(input()), 1), "%", sep = "")

#98
import random
n = int(input())
m = int(input())
dice = [0, 1]
results = [[random.choice(dice) for i in range(n)] for j in range(10000)]
results = list(map(sum, results))
print(round(100*results.count(m)/len(results), 1), "%", sep = "")

#99
L = int(input())
M = int(input())
dice = list(range(1, L+1))
results = [1 for i in range(400000) if not random.choice(dice) in range(L-M, M)]
print(str(round(sum(results)/4000, 1))+"%")
