import numpy as np
a=np.zeros(24)
print(a)
print("Size of array ",a.shape)

'''b=a.reshape(6,4)
print(b)
print("Size of array ",b.shape)
'''
b=a.reshape(2,3,4)
print(b)
print("Size of array ",b.shape)
