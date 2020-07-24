#34
import numpy as np
Z = np.eye(int(input()))

#35
import numpy as np
np.random.seed(42)
Z = np.random.random(tuple(map(int, input().split())))

#36
import numpy as np
np.random.seed(42)
Z = np.random.random(tuple(map(int, input().split())))
print(Z.min())
print(Z.max())

#37
import numpy as np
np.random.seed(42)
Z = np.random.random(tuple(map(int, input().split())))
print(Z.mean())

#38
import numpy as np
np.random.seed(42)
Z = np.random.random(tuple(map(int, input().split())))
all_Z = np.mean(Z, axis=0)
print(min(all_Z))
print(max(all_Z))

#39
import numpy as np
Z = np.ones(tuple(map(int,input().split())))
Z[1:-1, 1:-1] = 0

#40
import numpy as np
Z = np.pad(Z,pad_width=1,mode="constant",constant_values=0)

#41
import numpy as np
Z = np.diag(np.arange(int(input())) + 1, k=0)

#42
import numpy as np
K, num  = map(int, input().split())
Z = np.diag(np.arange(1, num + 1), k=K)

#43
import numpy as np
Z = np.zeros(tuple(map(int, input().split())))
Z[1::2,::2] = 1
Z[::2,1::2] = 1

#44
import numpy as np
print(np.unravel_index(i, Z.shape))