import numpy as np

# Slice elements from index 1 to index 5 from the following array:
arr = np.array([1,2,3,4,5,6,7,8,9,5,3])

print(arr[1:5])

# Slice elements from index 4 to the end of the array

print(arr[4:])

# Slice elements from the beginning to index 4 (not included):
print(arr[:4])

# Slice from the index 3 from the end to index 1 from the end:
print(arr[-3:-1])

# Return every other element from index 1 to index 5:

print(arr[1:5:2])

# Return every other element from the entire array:

print(arr[::2])

arr11 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# From the second element, slice elements from index 1 to index 4 (not included):
print(arr11[1,1:4])

# From both elements, return index 2:
print(arr11[0:2,2])