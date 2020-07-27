#51
np.seterr(divide="ignore")

#52
import numpy as np
Z = np.arange(input(), input(), dtype='datetime64[D]')

#53
import numpy as np
a, b = map(int, input().split())
k = int(input())
Z = np.array([list(map(float, range(k, k+b)))] * a)

#54
import numpy as np
a, b = map(int, input().split())
k = int(input())
Z = np.array([[float(k+i) for j in range(b)] for i in range(a)])

#55
import numpy as np
Z = np.array(list(map(float, V)))

#56
import numpy as np
s = int(input())
S = int(input())
n = (S - s)/(int(input())+1)
Z = np.around(np.arange(s+n, S, n), 3)

#57
import numpy as np
s = int(input())
S = int(input())
f = int(input())
n = S**(1/(f-1))
Z = np.around(np.array([n**i for i in range(f)]), 3)

#58
import numpy as np
np.random.seed(seed = int(input()))
Z = np.sort(np.random.sample(int(input())))
