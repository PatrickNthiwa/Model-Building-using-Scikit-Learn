import numpy as np

arr = np.array([1,2,3,4,5])

print(arr[0])
print(arr[3])
print(arr[4]+arr[3])
print(arr)

arr2=np.array([[1,2,3,4,5],[5,6,7,8,7]])

print("2nd elemnt of first dimensio",arr2[0,1])
print("Access the element on the 2nd row, 5th column:",arr2[1,4])
print(arr2)

# negative indexing to access an array from the end.
arr2=np.array([[1,2,3,4,5],[5,6,7,8,7]])

print("2nd elemnt of last elemt",arr2[0,-1])