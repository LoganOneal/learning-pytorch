import torch

# Create a tensor with [a,b] shape
x = torch.Tensor([5,3])
y = torch.Tensor([2,1])
print(x*y)

#create a Tensor full of zeros with defined shape
x = torch.zeros([2,5])
print(x)

#create a Tensor with random values
y = torch.rand([2,5])
print(y)

#change shape or "view" or a tensor
y = y.view([1,10])
print(y)

