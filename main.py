# Creating Tensors with PyTorch 

import torch

tensor_od = torch.tensor(1)   		# A scalar ( aka tensor with just a number )
tensor_1d = torch.tensor([1,2,3])   # A Vector ( aka a tensor with a list making it 1 dimensional )
tensor_2d = torch.tensor([ 
						  [1, 2],
						  [3, 4]
						])         # Matrix ( aka a tensor with 2 dimension aka array of arrrays )
						
tensor_3d = torch.tensor([
							[
							  [1, 2],
							  [3, 4]
							],
							[ [5, 6],
							  [7, 8]
							]
                         ])			# A 3d matrix ( an array containing arrays that contain arrays.