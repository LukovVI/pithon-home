import numpy as np
n = int(input())
x = int(input())
Z = np.array([float(i == x) for i in range(n)])