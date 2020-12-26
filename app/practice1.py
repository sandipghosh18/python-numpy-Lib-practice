import numpy as np

#differnt operation of numpy library
#ndim is a function which determin about the dimention of the array


#1 dimention array
a= np.array([1,2,3,4,5])
print(a.ndim)

#2 dimention array

a=np.array([(1,2,3),(1,6,5)])
print(a.ndim)

#printing the datatype of an array

a=np.array([("sandip","aditi"),("rakesh","cp")])
print(a.dtype)
print(a.size)

a=np.array([(1,23,44,5,6),(12,11,12,5,6)])
print(a.shape)
print(a.min())
print(a.sum())

a=np.linspace(1,3,5)
print(a)

a= np.linspace(1,3,10)
print(a)

a= np.array([(1,2,3,4,5),(2,4,5,6,7)])
print(a.shape)
print(a.sum(axis=0))
print(a.sum(axis=1))

