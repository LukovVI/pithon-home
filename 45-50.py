#45
import numpy as np
Z = (Y - np.mean (Y)) / (np.std (Y))
Z = np.around(Z, 2)

#46
import numpy as np
Z = np.dot(A, B)

#47
if A.shape[1] == B.shape[0]:
    Z = np.dot(A, B)
else:
    Z = "Упс! Что-то пошло не так..."

#48
Z[(3 < Z) & (Z < 9)] *= -1

#49
Z = np.copysign(np.ceil(np.abs(A)), A)

#50
Z = np.intersect1d(A, B)
