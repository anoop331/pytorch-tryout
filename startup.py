import torch
import numpy as np

data = [[1., 2], [3, 4]]
x_data = torch.tensor(data)


np_array = np.array(data)
x_np = torch.from_numpy(np_array)

# print(x_np)


shape = (2, 3,)
rand_tensor = torch.rand(shape)
ones_tensor = torch.ones(shape)
zeros_tensor = torch.zeros(shape)




if torch.cuda.is_available():
    rand_tensor = rand_tensor.to('cuda')
    ones_tensor = ones_tensor.to('cuda')
    zeros_tensor = zeros_tensor.to('cuda')


a = [[1,2,3],[4,5,6]]
b = [[1,4,7],[2,5,8],[3,6,9 ]]

t_a = torch.tensor(a)
t_b = torch.tensor(b)

t_c = t_a @ t_b

t_c.t_()

print(t_c)


