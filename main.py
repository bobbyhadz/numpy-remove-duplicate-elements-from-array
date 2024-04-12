# Remove the Duplicate elements from a NumPy Array

import numpy as np

arr = np.array([[3, 3, 5, 6, 7],
                [1, 1, 4, 5, 6],
                [7, 7, 8, 9, 10]])

print(arr)

print('-' * 50)

unique_1d = np.unique(arr)
print(unique_1d) # 👉️ [ 1  3  4  5  6  7  8  9 10]