#A3
import numpy as np

a = np.array([[1,1,1]])

k = np.array([[1,1,1],
              [1,1,1],
              [1,1,1]])
r=np.convolution(a,k)
