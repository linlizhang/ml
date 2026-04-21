import numpy as np
import time

a = np.zeros(4)
print(f"np.zeros(4): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

a = np.zeros((4,))

print(f"np.zeros(4,): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

a = np.random.random_sample(4)

print(f"np.random.random_sample: a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

a = np.arange(4.)

print(f"np.arange(4,): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

a = np.random.rand(4)

print(f"np.random.rand(4,): a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

a = np.array([5, 4, 3, 2])

print(f"np.array: a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

a = np.array([5.0, 4, 3, 2])

print(f"np.array: a = {a}, a shape = {a.shape}, a data type = {a.dtype}")

a = np.array([1, 2, 3, 4, 5])

print(f"a   : {a}")

b = -a
print(f"b   : {b}")


b = np.sum(a)
print(f"b = np.sum(a): {b}")

b = np.mean(a)
print(f"b = np.mean(a): {b}")

b = a**2
print(f"b = np.mean(a**2): {b}")

a = np.array([1, 2, 3, 4, 5])
b = np.array([-1, -2, 3, 4, 5])
print(f"Binary operators work element wise: {a + b}")

a = np.array([1, 2, 3, 4])
b = np.array([-1, 4, 3, 2])

c = np.dot(a, b)
print(f"NumPy 1-D np.dot(a, b) = {c}, np.dot(a, b).shape = {c.shape}")

c = np.dot(b, a)
print(f"numpy 1-D np.dot(b, a) = {c}, np.dot(b, a).shape = {c.shape}")

a = np.zeros((1, 5))
print(f"a shape = {a.shape}, a = {a}")

a = np.arange(6).reshape(-1, 2)

print(f"a.shape: {a.shape}, \na = {a}")

print(f"\na[2, 0].shape: {a[2,0].shape}, \na[2,0] = {a[2,0]}")

print(f"a[2].shape: {a[2].shape}, \na[2] = {a[2]}")

a = np.arange(20).reshape(-1, 10)
print(f"a = \n{a}")

print("a[0, 2:7:1] = \n", a[0, 2:7:1], ", a[:, 2:7:1].shape=", a[:, 2:7:1].shape)