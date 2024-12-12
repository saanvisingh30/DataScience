import numpy as np
a=np.arange(24)
'''print("Array is ")
print(a)
print("Size of array is  ",a.shape)'''
a=np.arange(2,50,2)

print("Array is ")
print(a)
print("Size of array is  ",a.shape)
#b=a.reshape(4,6)
'''b=a.reshape(6,4)
print("Array is ")
print(b)
print("Size of array is  ",b.shape)
'''
b=a.reshape(2,3,4)
print("Array is ")
print(b)
print("Size of array is  ",b.shape)