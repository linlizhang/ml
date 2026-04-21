import torch

x = torch.zeros(3, 2)

# print(x)
# print(x.type())

y = torch.tensor([[1, 2, 3],
                  [4, 10, 6],
                  [7, 8, 9]])

# to go to the next row (dim 0), skip 3 elements
assert y.stride(0) == 3

# to go to the next column (dim 1), skip 1 element in storage
assert y.stride(1) == 1

print(y.stride(1))
r, c = 1, 2
index = r * y.stride(0) + c * y.stride(1)

assert index == 5

assert y[1,1] == 10


v = y.view(1, 3, 3)

print(v)

t = torch.tensor([[1, 2, 3],[4, 5, 6]])

assert t.size() == (2, 3)



