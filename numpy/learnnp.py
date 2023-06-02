import numpy as np;
# passing a list to the arry()method
arr = np.array([1,2,3,4,5])

print(arr)
print (type(arr))

# passing a tuple to the arry()metho
arr1 =np.array((1,2,3,4,67,43))
print(arr1)
print (type(arr1))

print(np.__version__)

# Create a 0-D array with value 42

arr42 =np.array(42)
print(arr42)

# Create a 1-D array containing the values 1,2,3,4,5:

arry1d= np.array([1,2,3,4,5])
print(arry1d)

# Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:

arr2d= np.array([[1,2,3],[5,4,3]])
print(arr2d)

# Create a 3-D array with two 2-D arrays

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3d)

# Check Number of Dimensions? ndim

print(arr.ndim)
print(arr1.ndim)
print(arr2d.ndim)
print(arr3d.ndim)
print(arr42.ndim)

# we can also create an array and give it a number of dimensions using ndmin function

arrdim =np.array([1,23,34,5],ndmin=5)
print(arrdim)

print("Number of dimsnsions is ", arrdim.ndim)