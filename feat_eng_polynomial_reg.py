import numpy as np
import matplotlib as plt
np.set_printoptions(precision=2)

x = np.arange(0, 20, 1)
y = 1 + x**2

X = x**2

X = X.reshape(-1, 1)
print(f'X shape: {X.shape}, X: {X}')

x = np.arange(0, 20, 1)
y = x**2

X = np.c_[x, x**2, x**3]

print(f'X shape: {X.shape}, X: {X}')


