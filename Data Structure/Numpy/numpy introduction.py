import numpy as np
# myarr=np.array([[1,2,2,34,5]],np.int8)
#
# # Shape
# size=myarr.shape
# # print(size)
# # dtype
# type=myarr.dtype
# # print(type)
# # Array Creation
# # 5 ways of creating the array:
# # 1 First way
# listArray=np.array([[1,2,3],[1,23,4],[4,56,7]])
# #
# dict=np.array({34,23,23})
# print(dict)

# 2nd Way Using Formula
# .zeros
# zeros=np.zeros((2,5))
# print(zeros )

# .arange
# rng=np.arange(15)
# print(rng)
# linspace
# lspace=np.linspace(0,2,10)
# print(lspace)

# empty()
# empty=np.empty((4,6))
# print(empty)
# empty_like
# emp_like=np.empty_like(listArray)
# print(emp_like)

# Important
# array=np.arange(100)
# array.resize((4,25))
# print(array)
# # ravel
# a=array.ravel()
# print(a)


# Numpy Axis
# 1d  --> [1,2,3,4,5,6,7]===1 Axis[0]
# 2d --->   [[1,2],[2,3],[3,4]]  ===2 axis[ ]

x=[[1,2,3],[4,5,6],[7,8,9]]
ar=np.array(x)
# Sum according to axis 0
a=ar.sum(axis=0)
# print(a)
# Transpose
b=ar.T
# print(b)
# flat
for i in ar.flat:
     print(i)
#
# Array ndim
n=ar.ndim
# print("dim",n)

# n bytes
byte=ar.nbytes
# print("Byte",byte)


# get Max Index
a=ar.argmax()
# print("Max",a)

# get Min Element
a=ar.argmin()
# print("Min",a)

# get sort the Array
a=ar.argsort(axis=0)
# print("Sort",a)

a=ar.argsort(axis=1)
# print("Sort",a)

ar=ar.ravel()
# print(ar)
arr=ar.reshape((3,3))
# print(arr)

# Operation on Numpy Array
arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
sum=arr+arr2
# print("{}+{}={}".format(arr,arr2,sum))

# where
a=np.where(arr>5)
print(a)