import numpy as nu
M2 = M1
M2[-2, :] = nu.sin(M2[-2, :]*nu.pi/6)
M2[:, -2] = nu.e**M2[:, -2]